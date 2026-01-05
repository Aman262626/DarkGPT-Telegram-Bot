# 🌑 DarkGPT - Telegram Bot

A powerful Telegram bot powered by Claude Opus 4 AI with advanced conversation memory and multi-language support.

## ✨ Features

- 🤖 **Claude Opus 4 AI** - Latest and most advanced AI model
- 💾 **Conversation Memory** - Remembers previous messages in chat
- 🌍 **Multi-Language** - Supports Hindi, English, Hinglish
- ⚡ **Real-time Responses** - Fast and intelligent replies
- 🎯 **Context-Aware** - Understands conversation flow

## 📋 Requirements

- Python 3.8+
- Telegram Bot Token
- Anthropic API Key

## 🚀 Quick Setup

### 1. Clone Repository
```bash
git clone https://github.com/Aman262626/DarkGPT-Telegram-Bot.git
cd DarkGPT-Telegram-Bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create `.env` file:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
ANTHROPIC_API_KEY=your_anthropic_api_key
```

**Get Your Keys:**
- **Telegram Token**: Message [@BotFather](https://t.me/BotFather) → `/newbot`
- **Anthropic Key**: [console.anthropic.com](https://console.anthropic.com)

### 4. Run Bot
```bash
python bot.py
```

## 📦 Deploy on Render.com

1. Fork this repository
2. Go to [Render.com](https://render.com)
3. Create New → Web Service
4. Connect your GitHub repository
5. Add Environment Variables:
   - `TELEGRAM_BOT_TOKEN`
   - `ANTHROPIC_API_KEY`
6. Deploy!

## 🎮 Bot Commands

- `/start` - Start the bot
- `/clear` - Clear conversation history
- `/help` - Show help menu

## 💡 Usage

Simply send any message to the bot and it will respond intelligently using Claude Opus 4 AI. The bot maintains conversation context across messages.

**Example:**
```
You: Hello! Tum kaun ho?
Bot: Main DarkGPT hoon, Claude Opus AI se powered ek intelligent bot...
```

## 🛠️ Tech Stack

- **Python 3.8+**
- **python-telegram-bot** - Telegram Bot API wrapper
- **Anthropic API** - Claude Opus 4 AI
- **python-dotenv** - Environment management

## 📝 License

MIT License - Free to use and modify

## 👨‍💻 Developer

Created by [@Aman262626](https://github.com/Aman262626)

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

⭐ Star this repo if you find it helpful!
