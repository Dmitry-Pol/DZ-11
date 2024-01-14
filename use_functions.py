"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import json
import os

schet = 0
dic = {}
dic_new = {}
def fun_increase(schet):
    in_cash = float(input('введите сумму'))
    print(schet)
    schet += in_cash
    print(schet)
    return schet

def fun_buy(schet, dic):
    in_cash = float(input('введите сумму покупки'))
    try:
        os.path.isfile('text.data')
        with open('text.data', 'r') as f:
            schet = json.load(f)
    except:
        print('Файла для  загрузки счета нет')

    # if os.path.isfile('text.data'):
    #     with open('text.data', 'r') as f:
    #         schet = json.load(f)
    if schet < in_cash:
        print('денег не хватает')
    else:
        schet = schet - in_cash
        name = input('введите наименование покупки')
        dic[name] = in_cash
    return schet, dic

def fun_history(dic):
    for i in dic.items():
        print(f'{i[0]}-->{i[1]}')

def bank():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        global schet
        global dic
        print(schet, os.path.isfile('text.data'))
        if choice == '1':
            if os.path.isfile('text.data'):
                with open('text.data', 'r') as f:
                    schet = json.load(f)
                    print('file', schet)
            schet = fun_increase(schet)
            with open('text.data', 'w') as f:
                print('2', schet)
                json.dump(schet, f)
        elif choice == '2':
            if os.path.isfile('text_hist.data'):
                with open('text_hist.data', 'r') as f:
                    dic = json.load(f)
            schet, dic_new = fun_buy(schet, dic)
            with open('text_hist.data', 'w') as f:
                print('2', dic)
                json.dump(dic, f)

        elif choice == '3':
            fun_history(dic)
        elif choice == '4':

            break
        else:
            print('Неверный пункт меню')