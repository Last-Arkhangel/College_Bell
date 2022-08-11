# Дзвінки пар (SchoolBell)
Дзвінки пар в коледжі (SchoolBell)

## Встановлення
1. Завантажити python останньої версії з сайту [https://www.python.org/](https://www.python.org/) і встановити
2. Встановіть модулі, використовуючи команду:
```
pip install -r requirements.txt
```

## Особливості

Що може програма:
1. Показати поточний час;
2. Показати час найближчого дзвінка;
3. Відтворювати дзвінок у вибраний час (можна змінити час лише у файлі .py, а не у виконуваному файлі);
4. Увімкніть дзвінок, коли вам потрібно;
5. Ви можете вибрати музику для відтворення (за замовчуванням: sound3.mp3).

![Image alt](https://github.com/Last-Arkhangel/College_Bell/blob/main/program.JPG)


## Щоб створити файл exe, використовуйте:
```
pip install pyinstaller
```
з командою:
```
pyinstaller -F -w --icon=bell.ico --add-data="bell.ico;." Begin.py
```

Оригінальний репозиторій:
[Посилання](https://github.com/CyberHusky/School-Bell-Ubuntu-Raspberry)
