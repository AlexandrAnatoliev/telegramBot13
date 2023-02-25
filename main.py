# telegramBot13

# Бот на aiogram для администрирования группы
# Бот умеет отслеживать анализировать обновления и сообщения, как в личных сообщениях, так и в групповом чате.
# Такой функционал представляет нам возможность использовать бота в качестве администратора группы.
# Бот отправляет местоположение (в виде картинки - точки на карте) и фотографии
# https://www.youtube.com/watch?v=-ifqYvyjoDo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=8

# ЗАМЕЧАНИЯ:
# Для отправки контента пользователю используется функция send_something, в аргумент chat_id которой указывают ID чата,
# куда боту необходимо отправлять сообщение:
# message.from_user.id - если мы хотим отправить сообщение в личку
# message.chat.id - если мы хотим отправить в группу
# message.answer() - всегда отправляет сообщение в то место, где пользователь оставил сообщение
# т.е написал в группе - бот ответил в группе, написал боту в личку - бот ответил тебе в личку
# аргументы message.answer(): text=сообщение, parse_mode=тип разметки (часто используют HTML)
# bot.send_photo() - данный метод позволяет отправлять фотографии
# его аргументы: chat_id=ID чата, photo=ссылка на фотографию
# bot.send_location() - данный метод позволяет отправлять местоположение (в виде картинки - точки на карте)
# его аргументы: chat_id=ID чата, latitude, longitude = широта, долгота
# Важно! Не нужно где-либо использовать токен чата, достаточно токена бота и добавление бота администратором!
# Важно! Бот должен иметь доступ к сообщениям!
# Для этого:
# Перейдите в BotFather,
# напишите команду /mybots,
# выберите нужного бота,
# перейдите в Bot Settings → Group Privacy
# Выберите Turn off
# Должна появиться фраза Privacy mode is disabled for Bot
# chat_id=message.chat.id       "=id чата, куда пришло сообщение"
# chat_id=message.from_user.id  "=id чата пользователя, приславшего сообщение"
# (commands=['картинка'])- команды могут быть написаны и на кириллице

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

HELP_COMMAND = """
<b>/help</b> - <em>основные команды</em>
<b>/картинка</b> - <em>прислать картинку</em>
"""
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    """
    По команде посылает в личку пользователю список основных команд и удаляет сообщение пользователя
    :param message: /help
    :return:
    """
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler()
async def send_hello(message: types.Message):
    """
    Бот на bot.send_message() - отправляет пользователю HELLO:
    если chat_id=message.chat.id:
        в чат - если пользователь написал в чат
        в личку - если пользователь написал боту
    если chat_id=message.from_user.id:
        в личку пользователю - в любом случае
    """
    # await bot.send_message(chat_id=message.chat.id, text='HELLO')  # =id чата, куда пришло сообщение
    await bot.send_message(chat_id=message.from_user.id,
                           text='HELLO')  # =id чата пользователя, приславшего сообщение


@dp.message_handler()
async def echo(message: types.Message):
    """
    Эхо бот на message.answer() - отправляет пользователю его же текст:
    в чат - если пользователь написал в чат
    в личку - если пользователь написал боту
    """
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp)
