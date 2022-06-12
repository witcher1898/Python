import random

# функция генерации почты
FIO = (input("Введите ФИО: ")).split()
mail = FIO[1][:2] + FIO[2][:2] + FIO[0] + "@sberbank.ru"
print("Ваша почта:", mail)


# функция генерации пароля
def password():
    newPassword = []
    lowwerChar = 'abcdefghijklmnopqrstuvwxyz'
    upperChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    specChar = '!@#$%^&*()-+'

    while len(newPassword) < 12:
        a = random.randint(0, 100)
        b = random.choice(lowwerChar)
        c = random.choice(upperChar)
        d = random.choice(specChar)

        newPassword.append(a)
        newPassword.append(b)
        newPassword.append(c)
        newPassword.append(d)
    string = [str(i) for i in newPassword]
    print("Ваш пароль:", ''.join(string))

print ("gitChecking")
password()
