from keyboards.sign_up_keyboards import gender_keyboard

def handlers_sign_up(bot):
    @bot.message_handler(commands=["start"])
    def start(message):
        msg = bot.send_message(
            message.chat.id,
            "Привет! Я бот vhfewukvjh ck,bgkycgfhskdbfewbfdjskfdj. Как вас зовут?."
        )
    # ДОБАВИТЬ СОХРАНЕНИЕ ИМЕНИ В БД
        
    @bot.message_handler(content_types=['text'])
    def handle_name(message):
        bot.send_message(
            message.chat.id,
            "Выберите Ваш пол",
            reply_markup=gender_keyboard()
        )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("gender_"))
    def handle_gender_selection(call):
        bot.send_message(
            call.message.chat.id,
            f"Теперь введите ваш возраст"
        )
    # ДОБАВИТЬ СОХРАНЕНИЕ ПОЛА В БД

    # @bot.message_handler(content_types=['text'])
    # def handle_age(message):
    #     bot.send_message(
    #         message.chat.id,
    #         ""
    #     )
