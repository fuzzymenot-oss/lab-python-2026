# Обмен значениями через третью переменную.
# Жуковский Иван Александрович, группа УБ-64

first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print()
print("До обмена")
print("first_room =", first_room)
print("second_room =", second_room)

temporary_room = first_room
first_room = second_room
second_room = temporary_room

print()
print("После обмена")
print("first_room =", first_room)
print("second_room =", second_room)
