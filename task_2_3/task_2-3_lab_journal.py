name = input("Введите ФИО: ")
date = input("Введите дату: ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

line = "+--------------------------------------------------+"

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(line + "\n")
    file.write("| Электронный лабораторный журнал                  |\n")
    file.write(line + "\n")
    file.write(f"| ФИО исследователя : {name:<30} |\n")
    file.write(f"| Дата              : {date:<30} |\n")
    file.write(f"| Эксперимент       : {experiment:<30} |\n")
    file.write(line + "\n")
    file.write("| Вывод:                                           |\n")
    file.write(f"| {conclusion:<48} |\n")
    file.write(line + "\n")

print("Готово! Данные записаны в journal.txt")