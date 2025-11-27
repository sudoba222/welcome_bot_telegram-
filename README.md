# 🤖 Welcome Bot (Telegram)

A simple and friendly Telegram bot built with **PyTelegramBotAPI (telebot)**.  
When a user starts the bot using `/start`, it sends a personalized welcome message using their first name.

---

## 🚀 Features

- Responds to `/start` command  
- Greets the user by their **first name**  
- Beginner-friendly and clean structure  
- Uses **infinite polling** to stay online  

---

## 📦 Project Structure
project/
│── bot.py
│── README.md
---

## 🛠️ Installation & Setup

### 1️⃣ Create a virtual environment

<pre>
python3 -m venv venv
source venv/bin/activate     # macOS & Linux
venv\Scripts\activate        # Windows
</pre>
### 2️⃣ Install dependencies
<pre>pip install pytelegrambotapi</pre>

### 3 Add Your Bot Token: 
 create env file and insert your bot token there like 
 'TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"'

## ▶️ Running the Bot

Start the bot with:

<pre>python bot.py</pre>
