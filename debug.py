# Поиск и исправление ошибок.
# Жуковский Иван Александрович, группа УБ-64

print("Фрагмент А")
print("Ожидалось: сумма чисел 5.")
print("Причина ошибки: оператор + соединяет строки, поэтому получалось 23.")
first = "2"
second = "3"
print("Тип first до преобразования:", type(first))
print("Тип second до преобразования:", type(second))
first_number = int(first)
second_number = int(second)
print("Тип first после преобразования:", type(first_number))
print("Тип second после преобразования:", type(second_number))
print("Сумма:", first_number + second_number)

print()
print("Фрагмент Б")
print("Ожидалось: возраст через год при вводе 17 равен 18.")
print("Причина ошибки: input() возвращает строку, сложение строки и числа вызывает TypeError.")
age = input("Возраст: ")
print("Тип age до преобразования:", type(age))
age_number = int(age)
print("Тип age после преобразования:", type(age_number))
print("Возраст через год:", age_number + 1)

print()
print("Фрагмент В")
print("Ожидалось: среднее чисел 4, 7 и 10 равно 7.0.")
print("Причина ошибки: деление выполняется раньше сложения, поэтому считалось 4 + 7 + 3.333..., а не среднее.")
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Среднее:", average)
