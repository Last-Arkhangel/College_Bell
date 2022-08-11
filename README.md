# Дзвінки пар (SchoolBell)
Дзвінки пар в коледжі (SchoolBell)

## Особливості

Що може програма (Schoolbell):
Показати поточний час;
Показати час найближчого дзвінка;
Відтворювати музику у вибраний час (можна змінити час лише у файлі .py, а не у виконуваному файлі);
Увімкніть музику, коли вам потрібно;
Ви можете вибрати музику для відтворення (за замовчуванням: sound3.mp3).

![Image alt](https://github.com/Last-Arkhangel/College_Bell/blob/main/program.JPG)


Щоб створити файл exe, використовуйте:
```
pip install pyinstaller
```
з командою:
```
pyinstaller -F -w --icon=bell.ico --add-data="bell.ico;." Begin.py
```

Оригінальний репозиторій:
[Посилання](https://github.com/CyberHusky/School-Bell-Ubuntu-Raspberry)
