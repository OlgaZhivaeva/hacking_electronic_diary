import random
from datacenter.models import Schoolkid,  Subject, Lesson, Mark, Chastisement, Commendation
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

commendation_list = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]


def get_child(schoolkid):
    """Функция возвращает учетную запись ученика"""
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid)
    except ObjectDoesNotExist:
        print("Такого ученика не существует")
        print('Запусти скрипт заново и введи фамилию и имя правильно')
    except MultipleObjectsReturned:
        print("Найдено более одного ученика")
        print('Запусти скрипт заново и введи фамилию и имя ученика')
    else:
        return child


def fix_marks(schoolkid):
    """Функция исправляет все плохие оценки на пятёрки"""
    Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)
    print('Все плохие оценки исправлены')


def del_note(schoolkid):
    """Функция удаляет все замечания"""
    note = Chastisement.objects.filter(schoolkid=schoolkid)
    note.delete()
    print('Замечания удалены')


def get_subject(schoolkid):
    """Функция запрашивает предмет для похвалы или выдает случайный предмет"""
    subject_list = []
    queryset_subject = Subject.objects.filter(year_of_study=schoolkid.year_of_study)
    for subject in queryset_subject:
        subject_list.append(subject.title)
    while True:
        subject = input('Предмет для похвалы: ')
        if subject in subject_list:
            return subject
        if subject:
            print('Нет такого предмета или предмет введен с ошибкой')
            continue
        else:
            return random.choice(subject_list)


def create_commendation(schoolkid):
    """Функция записывает похвалу от учителя"""
    commendation = random.choice(commendation_list)
    subject = get_subject(schoolkid)
    lesson = Lesson.objects.filter(subject__title=subject,
                                   year_of_study=schoolkid.year_of_study,
                                   group_letter=schoolkid.group_letter).latest('date')
    Commendation.objects.create(text=commendation, schoolkid=schoolkid, created=lesson.date,
                                subject=lesson.subject, teacher=lesson.teacher)
    print(f'Добавлена похвала: {commendation}, предмет {subject}')


def hacking():
    name = input('Фамилия и Имя ученика: ')
    child = get_child(name)
    if child:
        fix_marks(child)
        del_note(child)
        create_commendation(child)
