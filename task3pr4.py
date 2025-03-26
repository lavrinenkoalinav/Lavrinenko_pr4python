def task_3():
    students = [
        ("Поліна Бойко", 85.5, 90),
        ("Юлія Фещук", 92.0, 95),
        ("Оксана Зубко", 78.25, 85)
    ]

    avg_score = sum(student[1] for student in students) / len(students)

    print("ЗВІТ ПРО УСПІШНІСТЬ СТУДЕНТІВ")
    print("-" * 50)
    print("{:<20} {:>15} {:>15}".format("Ім'я", "Середній бал", "Відвідуваність"))
    print("-" * 50)

    for name, score, attendance in students:
        print("{:<20} {:>15.2f} {:>15}%".format(name, score, attendance))

    print("-" * 50)
    print(f"{'Середній бал групи':<20} {avg_score:>15.2f}")

task_3()
