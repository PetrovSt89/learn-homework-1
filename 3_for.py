"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phones =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    def summa(items_sold):
      s=0
      for item in items_sold:
        s+=item
      return s

    def AM(items_sold):
      s=0
      for item in items_sold:
        s+=item
      AM = s/len(items_sold)  
      return AM 
    
    total_sum = 0

    for S_one_phone in phones:
      sum_item_sold = summa(S_one_phone['items_sold']) 
      print(f'суммарное количество продаж: {sum_item_sold}')
      total_sum += sum_item_sold

    #проверка print(sum([363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]))

    for AM_one_phone in phones:
      AM_item_sold = AM(AM_one_phone['items_sold']) 
      print(f'Среднее количество продаж продукта: {AM_item_sold}')  

    total_AM = total_sum / len(phones)
    #проверка print(sum(z:=[363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186])/len(z))     

    print(total_sum)
    print(total_AM)
   

if __name__ == "__main__":
    main()
