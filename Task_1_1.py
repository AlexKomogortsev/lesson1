# Task 1

# a = 5
# print(a)
# b = "Hello"
# print(b)
# text = input("Введите фразу:")
# print(text, type(text))

age = int(input("Enter your age:"))
if type(age) == int:
    age = input("Напишите текстом:")
print("Вы уже взрослый! Вам", age, "лет.")

answer1 = input("Введите Ваше Имя:")
answer2 = int(input("Введите ответ выражения: 2 + 2 = "))
answer3 = float(input("Введите ответ выражения: 1 / 10 = "))
answer4 = int(input("Введите Ваш возраст:"))
result = f"{answer1}, первое выражение умноженное на второе выражение и умноженное на Ваш возраст имеет вид: {answer2} * {answer3} * {answer4}. Если вы правильно провели расчеты, то это меньше 25-ти!"
print(result)
input("Press Enter")
