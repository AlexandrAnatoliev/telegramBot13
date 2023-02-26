# telegramBot13

#### Бот на aiogram для администрирования группы

* Бот умеет отслеживать анализировать обновления и сообщения, как в личных сообщениях, так и в групповом чате. Такой
  функционал представляет нам возможность использовать бота в качестве администратора группы.
* Бот отправляет местоположение (в виде картинки - точки на карте) и фотографии

Взят: https://www.youtube.com/watch?v=-ifqYvyjoDo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=8

## Замечания:

* Для отправки контента пользователю используется функция send_something, в аргумент chat_id которой указывают ID чата,
  куда боту необходимо отправлять сообщение:
    * message.from_user.id - если мы хотим отправить сообщение в личку
    * message.chat.id - если мы хотим отправить в группу
* message.answer() - всегда отправляет сообщение в то место, где пользователь оставил сообщение, т.е написал в группе -
  бот ответил в группе, написал боту в личку - бот ответил тебе в личку
    * аргументы message.answer():
        * text=сообщение
        * parse_mode=тип разметки (часто используют HTML)
* bot.send_photo() - данный метод позволяет отправлять фотографии
    * его аргументы:
        * chat_id=ID чата
        * photo=ссылка на фотографию
* bot.send_location() - данный метод позволяет отправлять местоположение (в виде картинки - точки на карте)
    * его аргументы:
        * chat_id=ID чата
        * latitude, longitude = широта, долгота
* Важно! Не нужно где-либо использовать токен чата, достаточно токена бота и добавление бота администратором!
* Важно! Бот должен иметь доступ к сообщениям!
    * Для этого:
        * Перейдите в BotFather
        * напишите команду /mybots,
        * выберите нужного бота,
        * перейдите в Bot Settings → Group Privacy
        * Выберите Turn off
        * Должна появиться фраза "Privacy mode is disabled for Bot"
* chat_id=message.chat.id       "=id чата, куда пришло сообщение"
* chat_id=message.from_user.id  "=id чата пользователя, приславшего сообщение"
* (commands=['картинка'])- команды могут быть написаны и на кириллице
* import os - библиотека, которая позволяет загрузить картинку
* executor.start_polling(dp, skip_updates=False)
    * skip_updates=False - бот обработает сообщения, которые появились в чате за время его бездействия.
    * skip_updates=True - бот проигнорирует сообщения, которые появились в чате за время его бездействия

## Требования:

* $ pip install -r requirements.txt
* создать файл config.py, в котором будут храниться токен для доступа к боту в виде
* создать папку photos в которой разместить фото в .jpg формате

```python 
TOKEN_API = "1234567890:ASDFGHH..."
```

## Где взять token?

* https://xakep.ru/2021/11/28/python-telegram-bots/

## Примеры использования

#### Добавляем библиотеки

```python
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import os  # позволяет загрузить картинку
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
    executor.start_polling(dpif
    __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)  # skip_updates - проверка обновлений (когда бот был выключен)
```

#### По команде посылает в личку пользователю список основных команд и удаляет сообщение пользователя, срабатывает на команды /help. Использует HTML-разметку

```python
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


HELP_COMMAND = """
<b>/help</b> - <em>основные команды</em>
<b>/картинка</b> - <em>прислать картинку</em>
"""
```

#### По команде /картинка загружает картинку из файла и посылает ее в группу или личку, сообщение пользователя - удаляет

```python
@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    # загружаем картинку
    for files in os.listdir('photos/'):
        if files.split('.')[-1] == 'jpg':
            file = open('photos/' + files, 'rb')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=file)
    await message.delete()
```

#### По команде /location отправляет местоположение в иде картинки (google maps), удаляет сообщение пользователя

```python
@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=68.97,
                            longitude=33.09)
    await message.delete()
```

#### Бот на bot.send_message() - отправляет пользователю HELLO:

* если chat_id=message.chat.id:
    * в чат - если пользователь написал в чат
    * в личку - если пользователь написал боту
* если chat_id=message.from_user.id:
    * в личку пользователю - в любом случае

```python
@dp.message_handler()
async def send_hello(message: types.Message):
    # await bot.send_message(chat_id=message.chat.id, text='HELLO')  # =id чата, куда пришло сообщение
    await bot.send_message(chat_id=message.from_user.id,
                           text='HELLO')  # =id чата пользователя, приславшего сообщение
```

#### Эхо бот на message.answer() - отправляет пользователю его же текст:

* в чат - если пользователь написал в чат
* в личку - если пользователь написал боту

```python
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
```