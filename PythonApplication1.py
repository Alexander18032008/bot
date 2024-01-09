# Создаем экземпляр класса TeleBot с токеном нашего бота
import telebot
from telebot import types
bot = telebot.TeleBot('6871519347:AAEFD4UttDaUoy1ujm74uVPqSLnG7pC5ahE')
# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(messege):

    # Создаем и настраиваем кнопки
   # keyboard = types.InlineKeyboardMarkup(row_width=2)  # указываем, что кнопки будут выводиться по 2 в ряд
   # button2 = types.InlineKeyboardButton(text="Ла лига", callback_data='button2')
   # button3 = types.InlineKeyboardButton(text="АПЛ", callback_data='button3')
  #  button4 = types.InlineKeyboardButton(text="Бундеслига", callback_data='button4')
  #  keyboard.add(button1, button2, button3, button4)  # добавляем кнопки на клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет')


    # Отправляем сообщение с клавиатурой
    bot.send_message(chat_id=message.chat.id, text="Добро пожаловать! Выберите одну из лиг ниже:",
                     reply_markup=keyboard)


# Обработчик нажатия на кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    # Обрабатываем выбор пользователя в зависимости от кнопки
    if call.data == 'button1':
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали Серию А")
    elif call.data == 'button2':
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали Ла лигу")
    elif call.data == 'button3':
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали АПЛ")
    elif call.data == 'button4':
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали Бундеслигу")




def show_buttons():
    # Функция, которая вызывается при нажатии на кнопку "Серия А"
    print("Турнирная таблица")
    print("Результаты матчей")

button_apl = input("Введите 'Серия А' чтобы показать кнопки: ")
if button_apl == "Серия А":
    show_buttons()


    def show_buttons():
        # Функция, которая вызывается при нажатии на кнопку "ЛА лига"
        print("Турнирная таблица")
        print("Результаты матчей")


    button_apl = input("Введите 'ЛА лига' чтобы показать кнопки: ")
    if button_apl == "ЛА лига":
        show_buttons()


        def show_buttons():
            # Функция, которая вызывается при нажатии на кнопку "АПЛ"
            print("Турнирная таблица")
            print("Результаты матчей")


        button_apl = input("Введите 'АПЛ' чтобы показать кнопки: ")
        if button_apl == "АПЛ":
            show_buttons()


            def show_buttons():
                # Функция, которая вызывается при нажатии на кнопку "Бундеслига"
                print("Турнирная таблица")
                print("Результаты матчей")


            button_apl = input("Введите 'Бундеслига' чтобы показать кнопки: ")
            if button_apl == "Бундеслига":
                show_buttons()
