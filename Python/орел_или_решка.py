# ОРЕЛ ИЛИ РЕШКА

# написать циклическую программу подбрасывания монетки, где четные числа будут - орел, нечетные решка, а ноль - ребро

import random # импортируем модуль рандом

while True: # повторяющийся цикл монетки
    a = input("\nБросить монетку? (Да/Нет)") # выбор действия
    if a == "нет" or a == "Нет" or a == "НЕТ" or a == "ytn" or a == "YTN" or a == "Ytn":
        break # условия завершения программы
    
    b = random.randint (0,100) # диапазон рандомных чисел
    #print (b) # использовал для теста программы
    
    if b % 2 == 0 and not b == 0 and not b == 66: # условия вывода 1
        print ("\nОрел")
    elif b == 0: # условия вывода 2
        print ("\nМонетка упала на ребро")
    elif b % 2 == 1 and not b == 33 and not b == 11 and not b == 99: # условия вывода 3
        print ("\nРешка")
    elif b == 33 or b == 66 or b == 99 or b == 11: # условия вывода 4
        kor = ("\nМонетка упала в траву", "\nМонетка укатилась под машину", "\nМонетку подхватил бездомный и убежал", "\nМонетка попала в телевизор и разбила его")
        print (random.choice(kor)) # функция рандомного вывода индекса из списка
    
print ("\nКонец программы.")
