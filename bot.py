import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен вашего бота
TOKEN = '7442663671:AAHCxt8booz0VRszB1Y1AAUlJt0Mm0HgHcs'

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    # Текст сообщения
    message_text = """\
ПРИВЕТСТВУЕМ

Добро пожаловать в наш онлайн-магазин одежды в Telegram! 🛍️

Вы попали в самое уютное и стильное место, где вас ждут эксклюзивные коллекции одежды по самым выгодным ценам. Мы тщательно отбираем каждую вещь, чтобы вы могли выглядеть и чувствовать себя безупречно.

Наши преимущества:

💎 Новинки недели - будьте первыми, кто оценит свежие модели!
🔥 Горячие скидки и распродажи круглый год - экономьте до 50%!
🌟 Редкая одежда и аксессуары, эксклюзивно в нашем магазине
✨ Быстрая бесплатная доставка по всей России - получите свой заказ в кратчайшие сроки!
🎁 Подарки и бонусы для постоянных покупателей - приятные сюрпризы гарантированы!

Заходите к нам почаще, ведь у нас всегда найдется что-то особенное для вашего гардероба. Добро пожаловать в мир стиля и комфорта вместе с нами! 🤗

Цены для подписчиков ниже от -10% чем на маркетплейсах 
При полной предоплате заказа ☝️

🎁 ГАРАНТИРОВАННЫЙ ПОДАРОК К ПЕРВОМУ ЗАКАЗУ"""

    # Кнопка с ссылкой
    keyboard = [
        [InlineKeyboardButton("Перейти", url="https://t.me/locstore")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Прямая ссылка на изображение
    photo_url = 'https://i.ibb.co/p1YMNzH/9399c0df-d61e-459a-8334-d4523d933144.jpg'

    try:
        # Отправка сообщения с фотографией и кнопкой
        context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=message_text, reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error sending photo: {e}")

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    try:
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.error(f"Error starting the bot: {e}")

if __name__ == '__main__':
    main()
