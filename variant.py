# Вариант 2. Книжный магазин: учебники и сборники задач.
# Жуковский Иван Александрович, группа УБ-64

order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

item_one_name = input("Название учебников: ")
item_one_quantity = int(input("Количество учебников: "))
item_one_price = float(input("Цена одного учебника (руб.): "))

item_two_name = input("Название сборников задач: ")
item_two_quantity = int(input("Количество сборников задач: "))
item_two_price = float(input("Цена одного сборника задач (руб.): "))

delivery_cost = float(input("Стоимость доставки (руб.): "))
paid_amount = float(input("Внесённая сумма (руб.): "))

item_one_cost = item_one_quantity * item_one_price
item_two_cost = item_two_quantity * item_two_price
goods_total = item_one_cost + item_two_cost
order_total = goods_total + delivery_cost
total_quantity = item_one_quantity + item_two_quantity
change = paid_amount - order_total

print()
print("Заказ:", order_name)
print("Заказчик:", customer_name)
print(f"{item_one_name} | {item_one_quantity} | {item_one_price:.2f} | {item_one_cost:.2f}")
print(f"{item_two_name} | {item_two_quantity} | {item_two_price:.2f} | {item_two_cost:.2f}")
print(f"Стоимость товаров: {goods_total:.2f} руб.")
print(f"Доставка: {delivery_cost:.2f} руб.")
print(f"Итого с доставкой: {order_total:.2f} руб.")
print("Общее количество единиц:", total_quantity)
print(f"Внесено: {paid_amount:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
