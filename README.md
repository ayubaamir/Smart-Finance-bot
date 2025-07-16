# Smart-Finance-bot
A smart Telegram bot using Google Gemini to process payments on The Open Network
# Smart Finance Bot ('Fin') for Telegram

An AI-powered Telegram bot designed to simplify crypto transactions on the TON blockchain. Built with Python and integrated with Google's Gemini AI, 'Fin' allows users to execute payments and get information using natural language commands.

## Key Features

- *Natural Language Processing:* Understands plain English commands for both payments and general queries.
- *Intelligent Transaction Parsing:* Automatically extracts the recipient's address, amount, and reason from a single sentence.
- *Secure Payment Links:* Generates ton://transfer links, ensuring users confirm all transactions securely in their own wallets.
- *AI-Powered Assistance:* Answers questions about the TON ecosystem, DeFi, and general finance topics.
- *Easy to Deploy:* Can be run easily using Replit and requires minimal setup.

## How to Set Up

To run this bot yourself, follow these steps:

1.  *Clone the Repository:*
    sh
    git clone [https://github.com/ayubaamir/Smart-Finance-bot](https://github.com/ayubaamir/Smart-Finance-bot)
    

2.  *Install Dependencies:*
    sh
    pip install -r requirements.txt
    

3.  *Set Up API Keys:*
    You will need a Telegram Bot Token from *@BotFather. You will also need a Google AI API Key from **Google AI Studio*. Save these keys as environment variables named BOT_TOKEN and GOOGLE_API_KEY.

4.  *Run the Bot:*
    sh
    python main.py
    

## How to Use 'Fin'

Interact with the bot on Telegram:

- *To make a payment:*
  "Send 2.5 TON to [wallet_address] for coffee"
- *To ask a question:*
  "What is STON.fi?" or "Give me some crypto safety tips."
- *To get started:*
  "/start"

## Technology Used

- *Backend:* Python
- *Telegram API Wrapper:* pyTelegramBotAPI
- *AI Engine:* Google Gemini
- *Blockchain:* The Open Network (TON)
-
