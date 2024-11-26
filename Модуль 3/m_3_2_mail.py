def send_email(msg, recepient, *, sender='university.help@gmail.com'):
    if recepient == sender:
        print('Нельзя отправить письмо самому себе!')
    else:
        if check_mail(recepient) and check_mail(sender):
            if sender != 'university.help@gmail.com':
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recepient}')
            else:
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recepient}')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recepient}')


def check_mail(email):
    global domains
    flag = True
    if email.count('@') != 1:
        flag = False
    else:
        user, host = email.split('@')
        if host.count('.') != 1:
            flag = False
        else:   # стоит доработать для доменов третьего уровня с двумя точками
            hostname, domain = host.split('.')
            if domain not in domains:
                flag = False
        pass
    return flag


domains = ['net', 'com', 'ru']  # дополнительные существующие домены: 'uk', 'su', 'org', 'info'
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
