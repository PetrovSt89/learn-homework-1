"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def strings(string1,string2):
      if type(string1) != str or type(string2) != str:
        return "0"
      else:
        if string1 == string2:
          return "1"
        elif len(string1) > len(string2):
          return "2"
        elif string2 == "learn":
          return "3"     
    print(strings("Стас",1))
    print(strings(1,"Стас"))
    print(strings(1,1)) 
    print(strings("Стас","Стас"))
    print(strings("Став1","Стас")) 
    print(strings("Стас","learn"))       
    
if __name__ == "__main__":
    main()
