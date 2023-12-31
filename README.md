# Test_trainee_avito

## Задание 1
Открыть папку task2_test_plan и скачать файл Test_plan_QA_Svetlova.xlsx

## Задание 2

### Требования к ПО:
- Python 3.11+ - [www.python.org/getit/](https://www.python.org/getit/)
- Виртуальное окружение (будет в инструкции ниже)
- Selenium (будет в инструкции ниже)
- Google Chrome (тест для одного браузера) [скачать](https://www.google.com/intl/ru_ru/chrome/) можно тут
- ChromeDriver [скачать](https://sites.google.com/chromium.org/driver/) можно тут

#### Как запустить тест (командная строка Windows): 
- Cкопировать репозиторий
```
git clone https://github.com/NataSvet/Test_trainee_avito.git
```
- Создать папку, в которой будет храниться виртуальное окружение и перейти в неё
```
mkdir environment
cd environment
```
- Создать вируальное окружение:
```
python -m venv selenium_env
```
- Активировать виртуальное окружение
```
selenium_env\Scripts\activate.bat
```
- Установить зависимости
```
cd task1_add_favorites
pip install -r requirements.txt
```
- Перейти в папку с тестом task1_add_favorites и запустить его
```
pytest test_add_to_favorites.py
```

### Описание работы теста
После запуска теста, откроется браузер в режиме инкогнито (чтобы провести тест для неавторизованного пользователя). 
Объявление добавится в избранное, будет осуществлена проверка что текст кнопки поменялся и появилось уведомление что объявление добавлено в избранное. 
Далее будет выполнен переход в избранное и проведены проверки что объявление добавлено с правильным названием, адресом, ценой.. 
Если тест пройден он будет обозначен passed.
