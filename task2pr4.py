def task_2():
    products = [
        ("Яйця", 32.5, 2),
        ("Молоко", 28.75, 1),
        ("Шоколад", 45.99, 5)
    ]

    header = "{:<20} {:>10} {:^8}".format("Назва товару", "Ціна", "Кількість")
    print(header)
    print("-" * 40)

    for name, price, quantity in products:
        print("{:<20} {:>10.2f} {:^8}".format(name, price, quantity))

task_2()
