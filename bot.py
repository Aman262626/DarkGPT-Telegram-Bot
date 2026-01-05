import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from anthropic import Anthropic
from collections import defaultdict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Anthropic client
anthropic_client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

# Conversation memory storage
user_conversations = defaultdict(list)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    welcome_message = (
        "🌑 *DarkGPT - Powered by Claude Opus*\n\n"
        "Features:\n"
        "✅ Advanced AI Conversations\n"
        "✅ Memory-Based Chat\n"
        "✅ Multi-Language Support\n"
        "✅ Real-time Intelligence\n\n"
        "Commands:\n"
        "/start - Bot shuru karo\n"
        "/clear - Chat history clear karo\n"
        "/help - Help menu\n\n"
        "💬 Kuch bhi pucho, DarkGPT ready hai!"
    )
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clear conversation history"""
    user_id = update.effective_user.id
    user_conversations[user_id] = []
    await update.message.reply_text("🌑 Chat history successfully cleared!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = (
        "*DarkGPT Help Menu* 🌑\n\n"
        "📌 *Kaise use kare:*\n"
        "• Seedhe apna question type karo\n"
        "• Bot previous messages yaad rakhega\n"
        "• Hindi, English, Hinglish - sabhi supported\n"
        "• Long conversations ke liye optimized\n\n"
        "📌 *Commands:*\n"
        "/start - Welcome message\n"
        "/clear - Conversation reset\n"
        "/help - Ye menu\n\n"
        "⚡ *Powered by Claude Opus 4* - Latest AI Model"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user messages"""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    # Typing indicator
    await update.message.chat.send_action("typing")
    
    try:
        # Add user message to conversation history
        user_conversations[user_id].append({
            "role": "user",
            "content": user_message
        })
        
        # Keep only last 20 messages for context (10 back-and-forth)
        if len(user_conversations[user_id]) > 20:
            user_conversations[user_id] = user_conversations[user_id][-20:]
        
        # Call Claude Opus API
        response = anthropic_client.messages.create(
            model="claude-opus-4-20250514",  # Latest Opus model
            max_tokens=2048,
            temperature=1,
            messages=user_conversations[user_id]
        )
        
        # Extract response
        bot_response = response.content[0].text
        
        # Add bot response to history
        user_conversations[user_id].append({
            "role": "assistant",
            "content": bot_response
        })
        
        # Send response
        await update.message.reply_text(bot_response)
        
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text(
            "❌ Error occurred! Kripya phir se try karo.\n"
            "Agar problem continue ho to /clear karke naye conversation start karo."
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot"""
    # Get token from environment
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        raise ValueError("❌ TELEGRAM_BOT_TOKEN environment variable not set!")
    
    # Create application
    app = Application.builder().token(token).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)
    
    # Start bot
    logger.info("🌑 DarkGPT Bot starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()