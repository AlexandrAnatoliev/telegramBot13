# telegramBot12

#### Бот на aiogram. Использование функции on_startup, параметра parse_mode="HTML", отправка emoji и stickers

* При включении бота выполняется функция on_startup
* По команде /start бот пишет сообщение жирным курсивом
* По команде /give бот посылает сообщение и стикер в чат, удаляет сообщение пользователя.
* Бот отвечает на сообщение пользователя его же сообщением, добавляя к нему emoji 🤪. На '❤️' отвечает '🖤'
* Бот подсчитывает количество ✅ в сообщении пользователя и отправляет их количество
* Бот отправляет ID стикера в ответ пользователю

Взят https://www.youtube.com/watch?v=lbLzGfshtaY&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=6

## Замечания:

* Параметр parse_mode="HTML" определяет метод чтения сообщения, в данном случае - как HTML-сообщение

```python
# <em> курсив </em> <b> жирный шрифт </b>
```

* В executor.start_polling(dp, on_startup=on_startup), прописываем аргумент on_startup=on_startup, чтобы функция
  on_startup(_) выполнялась при включении бота

```python
# Функция on_startup(_) принимает '_' аргумент!
```

* sticker_id берем у бота "get sticker id" (@idstickerbot). Emoji 🤪 просто копируем из телеграмм
* @dp.message_handler(content_types=['sticker']) тип входящего контента в хендлер - стикер
* await message.answer(message.sticker.file_id)  посылаем id стикера

## Требования:

* $ pip install -r requirements.txt
* создать файл config.py, в котором будут храниться токен для доступа к боту в виде

```python 
TOKEN_API = "1234567890:ASDFGHH..."
```

## Где взять token?

* https://xakep.ru/2021/11/28/python-telegram-bots/

## Примеры использования

#### ПРАКТИКА:

* Реализуйте бота, который будет отправлять стикер с котиком в ответ на команду /give. Но перед отправкой стикера
  отправьте сообщение "Смотри какой смешной кот ❤️"
* Модифицируйте бота, добавив возможность отправлять обычное сердечко, а в ответ получать черное.
* Реализуйте бота, который будет подсчитывать количество ✅ в сообщении пользователя и отправлять их количество.
* Напишите функцию /help, которая будет возвращать список существующих команд, отформатируйте текст т.о, чтобы имена
  команд были жирным шрифтом, а описание - курсивом.
* Напишите функцию on_startup(), которая будет выводить в терминал "Я запустился!"
* Напишите бота, который будет отправлять ID стикера в ответ пользователю

#### Добавляем библиотеки

```python
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
```

#### Создаем экземпляр класса Bot

```python
bot = Bot(TOKEN_API)
```

#### Создаем экземпляр класса Dispatcher

```python
dp = Dispatcher(bot)
```

#### Запуск бота

```python
if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
    # прописываем аргумент on_startup=on_startup, чтобы функция on_startup(_) выполнялась при включении бота
```

#### Функция on_startup(_) выполняется при включении бота

```python
async def on_startup(_):  # функция принимает (_) аргумент!
    print("Я запустился!")
```

#### Обрабатываем входящие сообщения, срабатывает на команды /start, /help. Использует HTML-разметку

```python
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("<em>Добро <b>пожаловать</b> в наш бот</em>", parse_mode="HTML")
    # параметр parse_mode="HTML" определяет метод чтения сообщения, в данном случае - как HTML-сообщение
    # <em> курсив </em>
    # <b> жирный шрифт </b>


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/give</b> - <em>посылает сообщение и стикер в чат, удаляет сообщение пользователя</em>
"""
```

#### Бот отправляет ID стикера в ответ пользователю

```python
@dp.message_handler(content_types=['sticker'])  # тип контента - стикер
async def get_sticker_id(message: types.Message):
    await message.answer(f"ID этого стикера: {message.sticker.file_id}")  # посылаем id стикера
```

#### По команде /give посылает сообщение и стикер в чат, удаляет сообщение пользователя

```python
@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Смотри какой смешной кот ❤️")
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEH305j97F6tGFBLsiXYpArYZ88f6d8wAACUwADrWW8FKPXOfaLMFQULgQ")
    # sticker_id берем у бота "get sticker id" (@idstickerbot)
    await message.delete()
```
