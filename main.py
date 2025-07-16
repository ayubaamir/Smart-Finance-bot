# --- Importing Necessary Libraries ---
import telebot
from telebot import types
import os
import json
import google.generativeai as genai

# --- Setting up the API Keys from Replit Secrets ---
BOT_TOKEN = os.environ['BOT_TOKEN']
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

# --- Initializing the Telegram Bot ---
bot = telebot.TeleBot(BOT_TOKEN)

# --- Configuring and Initializing the Google AI (Gemini) ---
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Defining the '/start' and '/donate' Command Handlers ---
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
  bot.reply_to(message, "Hello! I am Fin, the Smart Finance Bot. How can I assist you today? You can ask me to make a payment, for example: 'Send 2 TON to [address] for dinner'.")

@bot.message_handler(commands=['donate'])
def send_donate_link(message):
  wallet_address = "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N"
  amount_in_nanotons = 1000000000
  payment_link = f"ton://transfer/{wallet_address}?amount={amount_in_nanotons}&text=Donation for Smart Bot"
  keyboard = types.InlineKeyboardMarkup()
  donation_button = types.InlineKeyboardButton(text="Donate 1 TON", url=payment_link)
  keyboard.add(donation_button)
  bot.send_message(message.chat.id, "You can support the project by donating. Click the button below:", reply_markup=keyboard)

# --- Defining the Main AI Message Handler ---
@bot.message_handler(func=lambda message: True)
def handle_message(message):
  try:
    bot.reply_to(message, "🧠...") # Shorter thinking message

    # New, powerful, all-in-one prompt for the AI
    prompt = f"""
    You are 'Fin', a helpful and professional Smart Finance Assistant inside a Telegram bot.
    Your primary task is to parse payment requests on the TON blockchain.
    Your secondary task is to answer general questions in a friendly manner, in character as 'Fin'.

    Analyze the user's message: '{message.text}'

    First, determine the user's intent. The intent can be 'send_payment' or 'chat'.

    - If the intent is 'send_payment', extract the recipient's wallet address (a long string), the amount, and the reason.
    - If the intent is 'chat', formulate a helpful and friendly response to the user's question.

    You MUST respond ONLY with a single JSON object.

    Example 1 (Payment):
    User message: "send 5.5 ton to EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N for coffee"
    Your JSON response: {{"intent": "send_payment", "address": "EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N", "amount": 5.5, "reason": "for coffee"}}

    Example 2 (Chat):
    User message: "what is your name?"
    Your JSON response: {{"intent": "chat", "response": "My name is Fin. I'm your Smart Finance assistant, ready to help you with TON payments!"}}
    
    Now, analyze the user's message and provide the JSON response.
    """
    
    response = model.generate_content(prompt)
    json_response_text = response.text.replace('```json', '').replace('```', '').strip()
    ai_data = json.loads(json_response_text)

    # Check the intent provided by the AI in a single step
    if ai_data.get("intent") == "send_payment":
      address = ai_data.get("address")
      amount = float(ai_data.get("amount"))
      reason = ai_data.get("reason", "Payment")
      amount_in_nanotons = int(amount * 1_000_000_000)

      payment_link = f"ton://transfer/{address}?amount={amount_in_nanotons}&text={reason}"
      keyboard = types.InlineKeyboardMarkup()
      payment_button = types.InlineKeyboardButton(text=f"Click to Pay {amount} TON", url=payment_link)
      keyboard.add(payment_button)
      bot.send_message(message.chat.id, "I've prepared the transaction link for you. Please confirm the details in your wallet:", reply_markup=keyboard)
    
    elif ai_data.get("intent") == "chat":
      # If the intent is chat, simply send the response from the AI.
      bot.reply_to(message, ai_data.get("response"))

    else:
      # Fallback for safety
      bot.reply_to(message, "I'm not sure how to handle that. Please try rephrasing.")

  except Exception as e:
    print(f"An error occurred: {e}")
    bot.reply_to(message, "Sorry, an error occurred. Please try again in a moment.")

# --- Keeping the Bot Running ---
print("Smart Finance Bot Running ...")
bot.infinity_polling()

