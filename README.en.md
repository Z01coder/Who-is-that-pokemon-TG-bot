<!-- Improved compatibility of Back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>



<!-- LANGUAGE SWITCHER -->
<div align="right">
  <strong>Language:</strong> <a href="README.en.md">English</a> | <a href="README.md">Русский</a>
</div>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Who is that Pokemon TG-Bot</h3>

  <p align="center">
    Telegram bot for searching and getting information about Pokemon via PokeAPI
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the Project

![Preview](assets/1a.webp)

![Demo](assets/1.gif)

Who is that Pokemon TG-Bot is a Telegram bot that uses [PokeAPI](https://pokeapi.co/) to get information about Pokemon. The bot allows users to search for Pokemon by name or ID, get random Pokemon, and view their images with type information.

<details>
  <summary><strong>Project Goals and Objectives</strong></summary>

**Goals:**
* Create a functional Telegram bot for working with PokeAPI
* Demonstrate integration with external API through asynchronous requests
* Implement a user-friendly interaction interface
* Ensure reliable error handling and data validation

**Key Tasks:**
* Integrate the bot with PokeAPI to get Pokemon data
* Implement Pokemon search by name or ID
* Add a function to get a random Pokemon
* Implement FSM (Finite State Machine) for dialog management
* Implement user input validation
* Set up logging for all bot operations
* Ensure error handling and timeouts when making API requests
* Use environment variables for secure token storage

</details>

<details>
  <summary><strong>Results</strong></summary>

**Implemented Functionality:**
* Search Pokemon by name or ID (from 1 to 1010)
* Get random Pokemon from PokeAPI database
* Send Pokemon images with type information
* Interactive menu with inline buttons
* User input validation (length, format, ID range checks)
* API error and timeout handling
* Logging of all bot operations
* Dialog state management through FSM

**Created Components:**
* Main `main.py` file with bot logic
* `get_pokemon_info()` function for asynchronous requests to PokeAPI
* `PokemonStates` state class for dialog management
* `validate_pokemon_input()` validation function for input checking
* Command and callback query handlers
* Logging system with file and console output

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



### Built With

Main technologies and libraries used in the project:

* [![Python][Python-badge]][Python-url]
* [![Aiogram][Aiogram-badge]][Aiogram-url]
* [![Aiohttp][Aiohttp-badge]][Aiohttp-url]
* [![PokeAPI][PokeAPI-badge]][PokeAPI-url]

Additional dependencies:
* `aiogram>=3.2.0` - modern asynchronous framework for creating Telegram bots
* `aiohttp>=3.9.1` - asynchronous HTTP library for API requests
* `python-dotenv>=1.0.0` - for managing settings through environment variables

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- GETTING STARTED -->
<details>
  <summary><strong>Getting Started</strong></summary>

Instructions for installing and running the project locally.

### Prerequisites

To work with the project, you need to install:

* Python 3.x
  ```sh
  # Check Python version
  python --version
  ```

### Installation

Below are instructions for installing and configuring the bot.

1. Clone the repository
   ```sh
   git clone https://github.com/Z01coder/Who-is-that-pokemon-TG-bot.git
   cd Who-is-that-pokemon-TG-bot
   ```

2. Create a virtual environment (recommended)
   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root
   ```sh
   # Create a .env file and add:
   BOT_TOKEN=your_bot_token_from_BotFather
   ```

5. Get a bot token:
   - Open Telegram and find [@BotFather](https://t.me/BotFather)
   - Send the `/newbot` command and follow the instructions
   - Copy the received token to the `.env` file

6. Run the bot
   ```sh
   python main.py
   ```

7. Open Telegram and find your bot by the name you specified when creating it

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<details>
  <summary><strong>Usage</strong></summary>

The bot provides the following commands and functionality:

### Main Commands:

1. **`/start` or `/help`**
   - Starts the bot and shows the main menu
   - Displays inline buttons for action selection

2. **🔍 Search Pokemon**
   - Bot requests Pokemon name or ID
   - Supports search by name (e.g., "pikachu", "charizard")
   - Supports search by ID (from 1 to 1010)
   - Sends Pokemon image with information about its types

3. **🎲 Random Pokemon**
   - Bot automatically selects a random Pokemon from the database
   - Sends image and information about the Pokemon
   - Does not require user input

### Features:

- **Input Validation**: checking the correctness of name or ID before API request
- **Error Handling**: informative messages when Pokemon is not found or API errors occur
- **Timeouts**: protection against hanging when network problems occur (10 second timeout)
- **Logging**: all operations are logged to `bot.log` file for debugging
- **Asynchrony**: fast operation thanks to asynchronous API requests

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

<details>
  <summary><strong>Show completed development stages</strong></summary>

### Completed Stages:

- [x] **Stage 1: Basic Project Structure**
  - [x] Creating main `main.py` file with bot logic
  - [x] Setting up aiogram (Bot, Dispatcher, MemoryStorage)
  - [x] Initializing bot and dispatcher with state storage

- [x] **Stage 2: PokeAPI Integration**
  - [x] Implementing asynchronous `get_pokemon_info()` function for API requests
  - [x] Setting up timeouts for HTTP requests (10 seconds)
  - [x] Handling various API response status codes (200, 404, errors)
  - [x] Extracting data: name, types, Pokemon sprite

- [x] **Stage 3: FSM (Finite State Machine) for Dialog Management**
  - [x] Creating `PokemonStates` state class with name waiting state
  - [x] Implementing state switching when selecting Pokemon search
  - [x] Clearing states after operations complete

- [x] **Stage 4: Command and Callback Query Handling**
  - [x] Implementing `/start` and `/help` command handlers
  - [x] Creating inline buttons for navigation (search, random Pokemon)
  - [x] Handling callback queries for action selection

- [x] **Stage 5: Pokemon Search Functionality**
  - [x] Implementing search handler by name or ID
  - [x] Supporting search both by name (string) and by ID (number)
  - [x] Sending Pokemon image with type information

- [x] **Stage 6: Random Pokemon Functionality**
  - [x] Implementing random ID generation (from 1 to 1010)
  - [x] Getting and sending random Pokemon information
  - [x] Handling errors when getting random Pokemon

- [x] **Stage 7: Input Data Validation**
  - [x] Creating `validate_pokemon_input()` function for input checking
  - [x] Checking name length (maximum 50 characters)
  - [x] Validating ID (range from 1 to 1010)
  - [x] Checking name format (only letters, numbers, hyphens, spaces)
  - [x] Informative validation error messages

- [x] **Stage 8: Error and Exception Handling**
  - [x] Handling `asyncio.TimeoutError` on request timeouts
  - [x] Handling `aiohttp.ClientError` on client errors
  - [x] Handling general exceptions with logging
  - [x] Informative error messages to users

- [x] **Stage 9: Operation Logging**
  - [x] Setting up logging system with file and console output
  - [x] Logging bot startup and user actions
  - [x] Logging successful and failed API requests
  - [x] Logging errors with full information (exc_info)

- [x] **Stage 10: Managing Settings Through Environment Variables**
  - [x] Integrating `python-dotenv` library for working with `.env` file
  - [x] Moving bot token to environment variables
  - [x] Handling missing `.env` file or token
  - [x] Informative configuration error messages

- [x] **Stage 11: User Interface Improvements**
  - [x] Creating convenient menu with inline buttons
  - [x] Sending Pokemon images with captions
  - [x] Returning menu after each operation
  - [x] Handling callback queries with confirmation

- [x] **Stage 12: Code Documentation**
  - [x] Adding docstrings to functions
  - [x] Describing parameters and return values
  - [x] Comments on key code sections

</details>

### Planned Improvements:

- [ ] Caching PokeAPI requests to reduce load
- [ ] Additional Pokemon information (stats, abilities, evolutions)
- [ ] Pokemon search history for each user
- [ ] Favorite Pokemon with save capability
- [ ] Commands for getting extended information (stats, abilities)
- [ ] Multi-language interface support
- [ ] Unit tests for main functions
- [ ] Integration tests for checking API work
- [ ] Setting up CI/CD pipeline for automatic testing
- [ ] Adding commands for getting Pokemon evolution information
- [ ] Implementing pagination for viewing Pokemon list
- [ ] Adding Pokemon comparison (stats, types)

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- CONTACT -->
## Contact

* [![GitHub][GitHub-badge]][GitHub-url]
* [![Gmail][Gmail-badge]][Gmail-url]
* [![Telegram][Telegram-badge]][Telegram-url]

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I express my sincere gratitude to [Zerocoder](https://zerocoder.ru/) University and its entire team for creating an inspiring and professional educational environment. For training "IT-astronauts" at the Zerocoder "cosmodrome".

Special thanks to:

[Kirill Pshinnik](https://kpshinnik.ru/), the university director, for inspiring achievements;

Teachers [Nina Stefantsova](https://neural-courses.ru/teacher/nina-stefancova/), [Maxim Vershinin](https://neural-courses.ru/teacher/maksim-vershinin/), and [Darya Bobrovskaya](https://neural-courses.ru/teacher/darya-bobrovskaya/) — for deep knowledge, patience, and willingness to always help;

Nikita Murkin, course curator, for clear organization and mentoring;

Elizaveta, manager, for care, efficiency, and constant goodwill.

Thanks to you, this project became possible!

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Aiogram-badge]: https://img.shields.io/badge/Aiogram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[Aiogram-url]: https://docs.aiogram.dev/
[Aiohttp-badge]: https://img.shields.io/badge/Aiohttp-2C5F8D?style=for-the-badge&logo=aiohttp&logoColor=white
[Aiohttp-url]: https://docs.aiohttp.org/
[PokeAPI-badge]: https://img.shields.io/badge/PokeAPI-EF5350?style=for-the-badge&logo=Pokemon&logoColor=white
[PokeAPI-url]: https://pokeapi.co/
[GitHub-badge]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/Z01coder
[Gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[Gmail-url]: mailto:zolotuxin.alexey@gmail.com
[Telegram-badge]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://t.me/AZVXAN

