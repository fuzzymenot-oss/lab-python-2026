# Учебная нагрузка.
# Жуковский Иван Александрович, группа УБ-64

subject_one = input("Название первого предмета: ")
lessons_one = int(input("Количество занятий по первому предмету за неделю: "))
duration_one = int(input("Продолжительность одного занятия по первому предмету (мин): "))

subject_two = input("Название второго предмета: ")
lessons_two = int(input("Количество занятий по второму предмету за неделю: "))
duration_two = int(input("Продолжительность одного занятия по второму предмету (мин): "))

available_hours = float(input("Доступное время на неделю (ч): "))

minutes_one = lessons_one * duration_one
minutes_two = lessons_two * duration_two
total_minutes = minutes_one + minutes_two
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
hours_four_weeks = total_hours * 4

print()
print("Учебная нагрузка")
print("----------------")
print(f"{subject_one}: {minutes_one} мин")
print(f"{subject_two}: {minutes_two} мин")
print(f"Общая нагрузка: {total_minutes} мин или {total_hours:.2f} ч")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за четыре недели: {hours_four_weeks:.2f} ч")
