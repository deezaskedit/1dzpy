# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.


try:
    def dayoff():
        number = int(input("Введите день недели:3 :"))
        if number == 6 or number == 7:
            print("Да")
        else: 
            print("Нет")
except ValueError:
    print("Это число не входит в дни недели")

dayoff()
