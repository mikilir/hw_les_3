# Задание-2:
'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания,
email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def my_func(name, surname, byear, city, email, phone):
    print(name, surname, byear, city, email, phone)

my_func(name= 'Anna', surname='Ivanova', byear = 1992 , city='Saint-Petersburg', email='kobra@inbox.ru', phone='911')