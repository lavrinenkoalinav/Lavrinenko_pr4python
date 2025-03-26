def task_1():
    name = input("Введіть ім'я: ")
    surname = input("Введіть прізвище: ")
    age = float(input("Введіть вік: "))
    city = input("Введіть місто: ")

    result = f"{name} {surname:<15} | {age:.2f} | {city:>15}"
    print(result)

task_1()
