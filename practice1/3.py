from random import random
words = ['лотос', 'комод', 'столп', 'полка', 'дрова', 'дверь', 'трава', 'ручка' ,'палка']

#hidden_world = words[random.randint(0, len(words))]
hidden_word = words[0]

# проверка ввода
def is_valid_russian_word(word: str, length: int) -> bool:
    if len(word) != length:
        return False
    for ch in word:
        if not ('А' <= ch <= 'Я' or 'а' <= ch <= 'я'):
            return False
    return True


# Проверка введенного варианта
def check_word(word: str) -> str:
    global hidden_word
    if word == hidden_word:
        return True
    result = 'Результат: '
    
    for i in range (5):
        if word[i] == hidden_word[i]:
            result +=  ' [' + str(word[i]) + '] '
        elif word[i] in hidden_word:
            result +=  ' (' + str(word[i]) + ') '
        else:
            result += ' ' + str(word[i]) + ' '
    return result

# игра
def start_game():
    print('Загадано слово из 5 букв. У вас 6 попыток.')
    for i in range(6):
        print('Попытка ' + str(i + 1) + ': ', end = '')
        # проверка ввода
        word = ""
        length_required = 5
        while not is_valid_russian_word(word, length_required):
            word = input(f"Введите слово из {length_required} русских букв: ")
            if not is_valid_russian_word(word, length_required):
                print("Ошибка! Должно быть ровно", length_required, "русских букв.\n")

        result = check_word(word)
        if result:
            print('Вы угадали слово "' + str(hidden_word) + '" за ' + str(i + 1) + ' попытки!')
            return
        else:
            print(result)
    print('К сожалению вы не смогли отгадать слово "' + str(hidden_word) +'" за 6 попыток')
    return


if __name__ == '__main__':
    start_game()


    
    

