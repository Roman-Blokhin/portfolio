# Дневник для записей

# Создать дневник для записей, где каждая запись - это новая страница дневника
# с указание даты и времени

import datetime # импортируем модуль для определения даты и времени

a = 1 # переменная обозначающая кол-во записей
while True: # цикл повторения записей
    print ("\nЗапись " + str(a)) 
    
    t = datetime.datetime.today () # задействуем метод, самостоятельно определяющий дату и время
    print (t.strftime ("%d.%m.%Y. %H.%M")) # вывод даты и времени в нужном формате
    
    b = input("") # ввод заметки
    d = input ("\nДобавить еще заметку? (да/нет) ") # повторяем ли цикл?
    if d == "ytn" or d == "Ytn" or d == "YTN" or d == "НЕТ" or d == "Нет" or d == "" or d == "нет":
        break # условия выхода из программы
    else:
        a += 1 # изменяем номер заметки в большую сторону с каждой записью
        
    




