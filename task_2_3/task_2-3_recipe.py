medium_name = input("Введите название питательной среды: ")
agar_concentration = float(input("Введите концентрацию агара (%): "))
sterilization_temp = float(input("Введите температуру стерилизации (°C): "))

content = (
    f"{medium_name}\n"
    f"- Концентрация агара: {agar_concentration}%\n"
    f"- Температура стерилизации: {sterilization_temp} °C\n"
)

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Файл 'recipe.txt' успешно сформирован!")