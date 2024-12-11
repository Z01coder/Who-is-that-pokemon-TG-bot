from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import aiohttp
import random
import asyncio

# Устанавливаем токен вашего бота
BOT_TOKEN = "токен_вашего_бота"

# Создаём экземпляры бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Базовый URL PokeAPI
POKEAPI_URL = "https://pokeapi.co/api/v2"

# Кнопки меню
menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Поиск покемона", callback_data="search_pokemon"),
        InlineKeyboardButton(text="Случайный покемон", callback_data="random_pokemon")
    ]
])

async def get_pokemon_info(name_or_id):
    """Получает информацию о покемоне по имени или ID из PokeAPI"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{POKEAPI_URL}/pokemon/{name_or_id}") as response:
            if response.status == 200:
                data = await response.json()
                # Возвращаем данные: имя, типы, изображение
                name = data['name'].capitalize()
                types = ", ".join([t['type']['name'] for t in data['types']]).capitalize()
                sprite = data['sprites']['front_default']
                return name, types, sprite
            else:
                return None, None, None

@dp.message(Command(commands=["start", "help"]))
async def start_handler(message: types.Message):
    """Обрабатывает команды /start и /help"""
    await message.answer(
        "Привет! Я PokeAPI бот. Выберите действие:",
        reply_markup=menu_kb
    )

@dp.callback_query(lambda c: c.data == "search_pokemon")
async def search_pokemon_handler(callback_query: types.CallbackQuery):
    """Запрашивает у пользователя имя покемона"""
    await callback_query.message.answer("Введите имя или ID покемона:")

    @dp.message()
    async def get_pokemon_by_name(message: types.Message):
        name_or_id = message.text.lower()
        name, types, sprite = await get_pokemon_info(name_or_id)
        if name:
            await message.answer_photo(
                photo=sprite,
                caption=f"Имя: {name}\nТипы: {types}"
            )
        else:
            await message.answer("Извините, я не смог найти такого покемона.")

@dp.callback_query(lambda c: c.data == "random_pokemon")
async def random_pokemon_handler(callback_query: types.CallbackQuery):
    """Выбирает случайного покемона"""
    random_id = random.randint(1, 1010)  # Диапазон ID покемонов в PokeAPI
    name, types, sprite = await get_pokemon_info(random_id)
    if name:
        await callback_query.message.answer_photo(
            photo=sprite,
            caption=f"Имя: {name}\nТипы: {types}"
        )
    else:
        await callback_query.message.answer("Не удалось получить данные о покемоне.")

async def main():
    """Основная функция для запуска бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
