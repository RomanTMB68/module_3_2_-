p = 0
s = 0
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    z = "@"
    q = "university.help@gmail.com"
    a = sender[-4:]
    b = recipient[-4:]
    c = sender[-3:]
    d = recipient[-3:]
    e = ([".com"], [".net"], [".ru"])
    t = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient
    global p
    for i in recipient:
        if i == z:
            p += 1
        else:
            continue
            if p < 1:
                continue
            elif p >= 1:
                global s
                s = 1
                p = 0
                break
        if s < 1:
            for j in sender:
                 if j == z:
                     p += 1
                 if p < 1:
                     continue
                 elif p >= 1:
                    print(t)
                    break
        elif a or b != e[0] or e[1] and c or d != e[2]:
           print(t)
        else:
            break
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")

    elif sender is "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса "+sender+" на адрес "+recipient)

    elif sender != q:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "+sender+" на адрес "+recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
