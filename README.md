<img width="381" alt="Screenshot 2023-06-13 at 12 34 04 AM" src="https://github.com/shukurullo2004/krill_lotin_tg-bot/assets/113255469/71d4d605-1258-4235-90db-91547b59cd83">



Krill-Lotin Telegram Bot
This Telegram bot allows you to convert text between the Cyrillic and Latin alphabets. It can transliterate text from Cyrillic to Latin or vice versa based on user input.

Table of Contents
Installation
Usage
Bot Commands
Contributing
License
Installation
To use the Krill-Lotin Telegram Bot, follow these steps:

Clone the repository to your local machine:

shell
Copy code

git clone https://github.com/<your-username>/krill-lotin-telegram-bot.git

Install the required dependencies by running the following command in the project directory:

shell
Copy code

pip install -r requirements.txt

Obtain a Telegram Bot Token from the BotFather on Telegram. Make sure you have created a bot and obtained the token.

Replace the TOKEN variable in the main.py file with your own Telegram Bot Token:

python
Copy code

TOKEN = '<YOUR_TELEGRAM_BOT_TOKEN>'

Run the bot using the following command:

shell
Copy code
python main.py
Usage
Once the bot is up and running, you can interact with it on Telegram.
Search for @krill_lotin_shukurullo_bot in the Telegram app and start a chat with it. The bot will respond to the following commands:

/start: Displays a welcome message and prompts you to enter text.
Any text message: The bot will convert the text between Cyrillic and Latin alphabets based on its current format.
Bot Commands
The Krill-Lotin Telegram Bot supports the following commands:

/start: Displays a welcome message and prompts the user to enter text.
Contributing
Contributions to this project are welcome. If you find any issues or want to suggest improvements, please open an issue or submit a pull request. Here's how you can contribute:

Fork the repository.
Create a new branch for your feature or bug fix:
shell
Copy code
git checkout -b feature/your-feature-name
Make your changes and commit them:
shell
Copy code
git commit -m 'Add some feature'
Push the changes to your forked repository:
shell
Copy code
git push origin feature/your-feature-name
Open a pull request in this repository, describing your changes and referencing the related issue if applicable.
License
This project is licensed under the MIT License.

