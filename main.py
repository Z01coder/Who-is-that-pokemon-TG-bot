from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import aiohttp
import random
import asyncio
import os
import logging
from pathlib import Path
from typing import Optional, Tuple

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Определяем путь к файлу .env относительно расположения скрипта
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

# Загружаем переменные окружения из .env файла
if ENV_FILE.exists():
    load_dotenv(dotenv_path=ENV_FILE)
    logger.info(f"Загружен файл .env из {ENV_FILE}")
else:
    logger.warning(f"Файл .env не найден по пути {ENV_FILE}, пробую загрузить из текущей директории")
    load_dotenv()

# Получаем токен бота из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error(f"BOT_TOKEN не найден в переменных окружения. Проверьте файл .env по пути {ENV_FILE}")
    logger.error(f"Текущая рабочая директория: {os.getcwd()}")
    logger.error(f"Файл .env существует: {ENV_FILE.exists()}")
    if ENV_FILE.exists():
        logger.error(f"Содержимое .env файла: {ENV_FILE.read_text(encoding='utf-8')[:50]}...")
    raise ValueError("BOT_TOKEN не найден в переменных окружения. Проверьте файл .env")

# Создаём экземпляры бота и диспетчера с хранилищем состояний
storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=storage)

# Базовый URL PokeAPI
POKEAPI_URL = "https://pokeapi.co/api/v2"

# Определяем состояния для FSM
class PokemonStates(StatesGroup):
    waiting_for_pokemon_name = State()

# Кнопки меню
menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Поиск покемона", callback_data="search_pokemon"),
        InlineKeyboardButton(text="Случайный покемон", callback_data="random_pokemon")
    ]
])

async def get_pokemon_info(name_or_id) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Получает информацию о покемоне по имени или ID из PokeAPI.
    
    Args:
        name_or_id: Имя покемона (str) или его ID (int/str)
        
    Returns:
        Кортеж (имя, типы, спрайт) или (None, None, None) в случае ошибки
    """
    try:
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(f"{POKEAPI_URL}/pokemon/{name_or_id}") as response:
                if response.status == 200:
                    data = await response.json()
                    # Возвращаем данные: имя, типы, изображение
                    name = data['name'].capitalize()
                    # Применяем capitalize() к каждому типу отдельно
                    types = ", ".join([t['type']['name'].capitalize() for t in data['types']])
                    sprite = data['sprites']['front_default']
                    logger.info(f"Успешно получена информация о покемоне: {name}")
                    return name, types, sprite
                elif response.status == 404:
                    logger.warning(f"Покемон не найден: {name_or_id}")
                    return None, None, None
                else:
                    logger.error(f"Ошибка API при запросе покемона {name_or_id}: статус {response.status}")
                    return None, None, None
    except asyncio.TimeoutError:
        logger.error(f"Таймаут при запросе покемона: {name_or_id}")
        return None, None, None
    except aiohttp.ClientError as e:
        logger.error(f"Ошибка клиента при запросе покемона {name_or_id}: {e}")
        return None, None, None
    except Exception as e:
        logger.error(f"Неожиданная ошибка при запросе покемона {name_or_id}: {e}", exc_info=True)
        return None, None, None

@dp.message(Command(commands=["start", "help"]))
async def start_handler(message: types.Message):
    """Обрабатывает команды /start и /help"""
    try:
        logger.info(f"Пользователь {message.from_user.id} ({message.from_user.username}) запустил бота")
        await message.answer(
            "Привет! Я PokeAPI бот. Выберите действие:",
            reply_markup=menu_kb
        )
    except Exception as e:
        logger.error(f"Ошибка в start_handler: {e}", exc_info=True)
        await message.answer("Произошла ошибка. Попробуйте позже.")

@dp.callback_query(lambda c: c.data == "search_pokemon")
async def search_pokemon_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Запрашивает у пользователя имя покемона"""
    try:
        await callback_query.answer()
        await state.set_state(PokemonStates.waiting_for_pokemon_name)
        logger.info(f"Пользователь {callback_query.from_user.id} начал поиск покемона")
        await callback_query.message.answer("Введите имя или ID покемона:")
    except Exception as e:
        logger.error(f"Ошибка в search_pokemon_handler: {e}", exc_info=True)
        await callback_query.answer("Произошла ошибка. Попробуйте позже.", show_alert=True)

def validate_pokemon_input(text: str) -> Tuple[bool, Optional[str]]:
    """
    Валидирует введенное пользователем имя или ID покемона.
    
    Args:
        text: Введенный текст
        
    Returns:
        Кортеж (валидно ли, сообщение об ошибке или None)
    """
    if not text:
        return False, "Пожалуйста, введите имя или ID покемона."
    
    text = text.strip()
    
    if len(text) > 50:
        return False, "Имя покемона слишком длинное. Максимум 50 символов."
    
    # Проверяем, является ли ввод числом (ID) или допустимым именем
    if text.isdigit():
        pokemon_id = int(text)
        if pokemon_id < 1 or pokemon_id > 1010:
            return False, "ID покемона должен быть от 1 до 1010."
    else:
        # Проверяем, что имя содержит только буквы, цифры, дефисы и пробелы
        if not all(c.isalnum() or c in ('-', ' ') for c in text):
            return False, "Имя покемона может содержать только буквы, цифры, дефисы и пробелы."
    
    return True, None

@dp.message(PokemonStates.waiting_for_pokemon_name)
async def get_pokemon_by_name(message: types.Message, state: FSMContext):
    """Обрабатывает введенное имя покемона"""
    try:
        name_or_id = message.text.strip()
        
        # Валидация входных данных
        is_valid, error_message = validate_pokemon_input(name_or_id)
        if not is_valid:
            await message.answer(error_message)
            return
        
        name_or_id = name_or_id.lower()
        logger.info(f"Пользователь {message.from_user.id} ищет покемона: {name_or_id}")
        
        name, types, sprite = await get_pokemon_info(name_or_id)
        await state.clear()
        
        if name:
            await message.answer_photo(
                photo=sprite,
                caption=f"Имя: {name}\nТипы: {types}",
                reply_markup=menu_kb
            )
            logger.info(f"Покемон {name} успешно найден для пользователя {message.from_user.id}")
        else:
            await message.answer(
                "Извините, я не смог найти такого покемона.",
                reply_markup=menu_kb
            )
    except Exception as e:
        logger.error(f"Ошибка в get_pokemon_by_name: {e}", exc_info=True)
        await state.clear()
        await message.answer(
            "Произошла ошибка при поиске покемона. Попробуйте позже.",
            reply_markup=menu_kb
        )

@dp.callback_query(lambda c: c.data == "random_pokemon")
async def random_pokemon_handler(callback_query: types.CallbackQuery):
    """Выбирает случайного покемона"""
    try:
        await callback_query.answer()
        random_id = random.randint(1, 1010)  # Диапазон ID покемонов в PokeAPI
        logger.info(f"Пользователь {callback_query.from_user.id} запросил случайного покемона (ID: {random_id})")
        name, types, sprite = await get_pokemon_info(random_id)
        if name:
            await callback_query.message.answer_photo(
                photo=sprite,
                caption=f"Имя: {name}\nТипы: {types}",
                reply_markup=menu_kb
            )
            logger.info(f"Случайный покемон {name} успешно отправлен пользователю {callback_query.from_user.id}")
        else:
            await callback_query.message.answer(
                "Не удалось получить данные о покемоне. Попробуйте еще раз.",
                reply_markup=menu_kb
            )
    except Exception as e:
        logger.error(f"Ошибка в random_pokemon_handler: {e}", exc_info=True)
        await callback_query.answer("Произошла ошибка. Попробуйте позже.", show_alert=True)
        try:
            await callback_query.message.answer(
                "Произошла ошибка при получении случайного покемона. Попробуйте позже.",
                reply_markup=menu_kb
            )
        except Exception:
            pass

async def main():
    """Основная функция для запуска бота"""
    try:
        logger.info("Запуск бота...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Критическая ошибка при запуске бота: {e}", exc_info=True)
        raise
    finally:
        await bot.session.close()
        logger.info("Бот остановлен")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)
