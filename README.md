# Телеграм-бот

## Описание

Бот для принятия решений.

Принцип работы бота:
- Бот получает вопрос, выбирает из списка ANSWER ответ случайным образом и возвращает его пользователю.
- Список ANSWER можно пополнить любыми фразами.

#### Технологии

- Python 3.9
- aiogram
- asynco

#### Запуск проекта

- Склонируйте репозиторий:  
``` git clone <название репозитория> ``` 
- Заполнить переменную main.py   
``` BOT_TOKEN = токен_Вашего_Telegtam_бота ```  
- Установите и активируйте виртуальное окружение:  
``` python -m venv venv ```  
``` source venv/Scripts/activate ``` 
- Установите зависимости из файла requirements.txt:   
``` pip install -r requirements.txt ```

![pic](https://github.com/egorzhmaev/bot_decision_making/blob/main/photo_2024-03-03_15-20-04.jpg)
