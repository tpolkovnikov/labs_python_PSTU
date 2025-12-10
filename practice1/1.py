from random import randint

number = 0
difficulty = 4 # по умолчанию длинна числа - 4
game = {}
count_game = 0
choice = ''

# выбор сложности
def choice_difficult() -> None:
    global difficulty
    print("Выберите сложность - длинну числа: \n q - Отмена \n 1 - длинна - 3 \n 2 - длинна - 4 \n 3 - длинна - 5 \n")
    while True:
        temp = str(input())
        match (temp):
            case 'q':
                # просто уход в меню 
                break
            case '1': 
                difficulty = 3
                break
            case '2':
                difficulty = 4
                break
            case '3':
                difficulty = 5
                break
            case _:
                print("Некорректный выбор! Нужно ввести 0, 1, 2 или 3.")
    
# печатает промежуточный результат - коровы, быки
def print_result(count_cow: int, count_bull: int) -> None:
    print("Найдено " + str(count_cow) + " коров и " + str(count_bull) + " быков")

# генерация числа
def generate_number(n: int) -> int:
    start = 10**(n - 1)
    end = 10**n - 1
    return randint(start, end)


# главное меню 
def main_menu() -> None:
    global choice
    if choice == 'нет':
        return 0
    print("Коровы и быки:\n")
    while True:
        if choice == 'нет':
            return 0
        print("Меню: \n 0 - Выбрать сложность. \n 1 - Играть. \n q - Выход. ")
        choice = str(input())
        if choice.lower() == 'q':
            print("Выход.")
            break
        match (choice):
            case '0':
                choice_difficult()
            case '1': 
                start_game()
            case _:
                print("Некорректный выбор! Нужно ввести 0, 1 или q.\n")
        

# проверка числа
def count_answer(answer: str, right_answer: str) -> tuple[int, int]:
    cow = 0
    bull = 0
    for i in range (difficulty):
        if (answer[i] == right_answer[i]):
            cow += 1
        elif (answer[i] in right_answer):
            bull += 1
    return cow, bull

# вывод результата игр
def game_result() -> None:
    global game
    best = game[0]
    worst = game[0]
    average = 0
    for i in range(len(game)):
        if (game [i] > worst):
            worst = game[i]
        if (game[i] < best):
            best = game[i]
        average += game[i]

    average = average / len(game)
    print("Всего игр сыграно: " + str(len(game)) )
    print("Лучший результат: " + str(best))
    print("Худший результат: " + str(worst))
    print("Средний результат: " + str(average) + '\n\n')

# проверка число ли это
def is_bad(answer: str) -> bool:
    try:
        return str(int(answer)) != answer
    except ValueError:
        return True

# обработка корректного варианта: 
# Проверка для 00000 - не правильно проходит - говорит что нет, так как число 0 
def check_answer(answer: str) -> str:
    temp = answer
    if int(temp) == 0 and temp == "".join(str(0) for _ in range(difficulty)):
        return temp
    # проверка на размер + на что это только число
    while (len(temp) != difficulty) or is_bad(temp):
        print("Вы ввели некорректный вариант (короче/длиннее или буквы/спец символы)")
        print("Ваш вариант: ", end = '')
        temp = str(input())

    return temp

# игра
def start_game() -> None:
    global choice
    if choice == 'нет':
        return
    global game
    global count_game
    count_attempt = 0
    right_answer = generate_number(difficulty)
    #right_answer = "12345" # для теста 
    print("Загадано число из " + str(difficulty) + " цифр.")
    print("Ваш вариант: ", end = '')
    answer = str(input())
    answer = check_answer(answer) # проверка ответа
    current = count_answer(answer, right_answer)
    
    # пока не отгадает
    while (current[0] != difficulty):
        print_result(current[0], current[1])
        print("Ваш вариант: ", end = '')
        answer = str(input())
        answer = check_answer(answer) # проверка ответа
        count_attempt += 1
        current = count_answer(answer, right_answer)
    
    # отгадал
    count_attempt += 1
    print("Вы угалади число " + str(right_answer) + " за " + str(count_attempt) + " попыток.")
    game[count_game] = count_attempt
    count_game += 1
    while choice != 'нет':
        print("Хотите сыграть ещё? (да/нет): ", end = "")
        choice = str(input())
        match (choice):
            case 'да':
                start_game()
            case 'нет':
                game_result()
            case _:
                print("Некорректный выбор! Нужно ввести да или нет.\n")

if __name__ == '__main__':
    main_menu()

