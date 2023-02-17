"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {}

def ask_user(answers_dict):  #answers_dict
    """
    Замените pass на ваш код
    """
    word = input('Введи вопрос: ')
    while word != 'выход':
      if word in answers_dict:
        print(questions_and_answers[word]) #questions_and_answers[word]
      else:
        answer = input('Научи меня отвечать на этот вопрос: ')
        answers_dict[word] = answer

      word = input('Введи вопрос: ')  
      
if __name__ == "__main__":
    ask_user(questions_and_answers)  #questions_and_answers
