from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8908935616:AAGFX8oFTqeuADfB_7R0qSGWQgglZU5PQIk"
GAME_SHORT_NAME = "saladando"
GAME_URL = "https://mutanoandoficial-ship-it.github.io/meujogucho/" # URL onde o HTML está hospedado

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Envia o jogo para o chat quando o usuário digita /start
    await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name=GAME_SHORT_NAME)

async def game_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Quando o usuário clica no botão "Play", o bot abre o navegador interno com o link do jogo
    query = update.callback_query
    if query.game_short_name == GAME_SHORT_NAME:
        await query.answer(url=GAME_URL)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(game_callback))
    
    print("Bot rodando... Aperte /start no Telegram!")
    app.run_polling()

if __name__ == "__main__":
    main()
