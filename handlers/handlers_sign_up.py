from keyboards.gender_keyboard import gender_keyboard, name_keyboard


def handlers_sign_up(bot):
    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(
            message.chat.id,
            "Привет! Я бот для регистрации пользователей. Пожалуйста, выберите ваш пол.",
            reply_markup=gender_keyboard(),
        )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("gender_"))
    def handle_gender_selection(call):
        gender = call.data.split("_")[1] # ПОТОМ БУДЕТ СОХРАНЕНИЕ В БАЗУ ДАННЫХ
        bot.edit_message_text(
            f"Введите Ваше имя: ",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )

    @bot.callback_query_handler(func=lambda call: call.data == "send_name")
    def handle_send_name(call):
        pass # Здесь можно добавить обработку имени пользователя, например, сохранить его в базу данных