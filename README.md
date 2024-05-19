# Взламываем электронный дневник
При помощи этого скрипта можно исправить плохие оценки в электронном дневнике.<br>
А также удалить замечания и добавить похвалу.

## Сайт электронного дневника
Сайт с электронным дневником можно найти по [ссылке](https://github.com/devmanorg/e-diary/tree/master)

## Скачайте скрипт

Скачайте скрипт из [репозитория](https://github.com/OlgaZhivaeva/hacking_electronic_diary)
И разместите его на сервере в папке `e-diary` рядом с файлом `manage.py`

## Подключитесь к базе данных 

Подключитесь к базе данных через интерактивную оболочку `shell`. Для этого в командной строке наберите
```commandline
python manage.py shell
```
В открывшейся интерактивной оболочке `shell` сделайте необходимые импорты

```commandline
import random
from datacenter.models import Schoolkid, Subject, Lesson, Mark, Chastisement, Commendation
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from hacking_electronic_diary import get_child, fix_marks, del_note, create_commendation, get_subject, hacking
```

## Приступайте к исправлениям

Для исправления оценок запустите в `shell` функцию `hacking()`
```commandline
hacking()
```
Скрипт предложит ввести фамилию и имя ученика, а затем исправит у него в базе данных все плохие оцeнки на пятёрки.<br>
Удалит все замечания и добавит похвалу от учителя. Перед тем как добавить похвалу, скрипт предложит ввести название предмета.<br>
Можно не вводить название предмета, а нажать клавишу`Enter`, тогда предмет для похвалы будет выбран случайным образом.<br>

