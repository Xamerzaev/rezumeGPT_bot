# RezumeGPT_bot

![RezumeGPT_bot](https://i.imgur.com/3JcB7fT.png)

## Описание проекта

RezumeGPT_bot - это Telegram-бот, который использует модель GPT-3 от OpenAI для генерации резюме на основе введенных пользователем данных. Бот предлагает пользователю ответить на несколько вопросов, связанных с опытом работы и образованием, а затем генерирует резюме на основе этих ответов.

## Требования к установке

Для запуска проекта необходимо установить следующие зависимости:

- Python 3.6+
- Flask
- python-dotenv
- requests
- python-telegram-bot
- openai

## Установка и запуск

1. Склонируйте репозиторий:

```
git clone https://github.com/mahamerz/RezumeGPT_bot.git
```

2. Создайте файл `.env` на основе `.env.example` и заполните его своими данными для OpenAI API и Telegram API.

3. Установите зависимости:

```
pip install -r requirements.txt
```

4. Запустите приложение:

```
python app.py
```

5. Откройте бота в Telegram и начните использование.

## Пример использования

1. Найдите бота в Telegram по имени @RezumeGPT_bot.

2. Нажмите кнопку "Start" или отправьте команду /start.

![Start](https://i.imgur.com/0KwW8Pz.png)

3. Ответьте на несколько вопросов, связанных с опытом работы и образованием.

![Questions](https://i.imgur.com/5Z5j2QJ.png)

4. Получите сгенерированное резюме на основе введенных данных.

![Resume](https://i.imgur.com/r7vHb3e.png)

## Автор

Mahamerz - Мансур Хамерзаев. Запрещается использование кода в коммерческих условиях.

## Лицензия

Этот проект находится под лицензией [MIT](https://opensource.org/licenses/MIT).