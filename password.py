import string
import secrets
import pyperclip
print(f"Password generator from elliotjustatech\n")
try:
    while True:
        try:
            a = int(input("Какая нужна длина пароля?(От 1 до 20):"))
            if 0 < a < 21:
                break
            else:
                print(f"\nВведи число от 1 до 20.\n")
        except ValueError:
            print(f"\nОшибка. Введи число\n")
    sys = string.ascii_lowercase
    while True:
        u = input("Нужны заглавные буквы?(y/n):")
        if u == "y" or u == "n":
            break
        else:
            print(f"\nВведи либо 'y' либо 'n'.\n")
    if u == "y":
        sys += string.ascii_uppercase
    while True:
        f = input("Нужны ли цифры?(y/n):")
        if f == "y" or f == "n":
            break
        else:
            print(f"\nВведи либо 'y' либо 'n'.\n")
    if f == "y":
        sys += string.digits
    while True:
        h = input("Нужны ли символы?(y/n):")
        if h == "y" or h == "n":
            break
        else:
            print(f"\nВведи либо 'y' либо 'n'.\n")
    if h == "y":
        sys += string.punctuation
    pas = ""
    for _ in range(a):
        s = secrets.choice(sys)
        pas += s
    print(f"\nПароль: {pas}")
    pyperclip.copy(pas)
    print("Ваш пароль скопирован в буфер обмена.")
except KeyboardInterrupt:
    print(f"\n\nСкрипт прерван. До встречи")