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

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp)