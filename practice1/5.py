TEXT1 = "В Python есть несколько структур данных для хранения коллекций. \
Список — это изменяемая последовательность элементов. \
Кортеж — это неизменяемая последовательность. \
Словарь — это коллекция пар ключ-значение."

TEXT2 = "Отец мой Андрей Петрович Гринев в молодости своей служил при графе Минихе и вышел в отставку премьер-майором в 17.. году. \
С тех пор жил он в своей Симбирской деревне, где и женился на девице Авдотье Васильевне Ю., дочери бедного тамошнего дворянина. \
Нас было девять человек детей. Все мои братья и сестры умерли во младенчестве.\
Матушка была еще мною брюхата, как уже я был записан в Семеновский полк сержантом, по милости майора гвардии князя В., близкого нашего родственника. \
Если бы паче всякого чаяния матушка родила дочь, то батюшка объявил бы куда следовало о смерти неявившегося сержанта, и дело тем бы и кончилось. \
Я считался в отпуску до окончания наук. В то время воспитывались мы не по-нонешнему. \
С пятилетнего возраста отдан я был на руки стремянному Савельичу, за трезвое поведение пожалованному мне в дядьки. \
Под его надзором на двенадцатом году выучился я русской грамоте и мог очень здраво судить о свойствах борзого кобеля. \
В это время батюшка нанял для меня француза, мосье Бопре, которого выписали из Москвы вместе с годовым запасом вина и прованского масла. \
Приезд его сильно не понравился Савельичу. «Слава богу, — ворчал он про себя, — кажется, дитя умыт, причесан, накормлен. \
Куда как нужно тратить лишние деньги и нанимать мусье, как будто и своих людей не стало!»"

exclude = ".,!?;:""()[]«»—"
def amount_symbol(text: str) -> tuple[int, int]:
    amount_space = 0
    for ch in text:
        if ch == ' ':
            amount_space += 1
    return len(text), len(text) - amount_space


# подсчет слов и запись в массив
def amount_word_form(text: str) -> tuple[list[str], int]:
    delims = " .,;:!?()[]{}\"'«»-—\n\t"
    amount_word = 0
    current_word = ''
    words = []
    for ch in text:
        if ch in delims:
            if current_word != "": 
                words.append(current_word)
                amount_word += 1
            current_word = ""
        else:
            current_word += ch

    # если текст заканчивается словом без знакак препинания
    if current_word != "":
        words.append(current_word)
        amount_word += 1

    return words, amount_word

# Поиск 5 самых частых словоформ и их частоту
def most_frequent_words(words: list[str]) -> dict[str, int]:
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    items = list(frequencies.items())
    # сортировка
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    top5_items = items[:5]
    top5 = {k: v for k, v in top5_items}
    return top5



# вставка элемента на i-ое место и смещение остатка дальше
def rename(words: list[str], word: str, index: int):
    # если вставить на последнее слово
    if index == len(words) - 1:
        words[index] = word
        return words
    
    moved_word = ""
    for i in range(len(words)):
        if i == index:
            moved_word = words[i]
            words[i] = word
        elif i > index:
            moved_word, words[i] = words[i], moved_word
    return words

# Поиск 5 самых длинных словоформ
def longest_words(words: list[str]) -> list[str]:
    longest = ["", "", "", "", ""]
    for word in words:
        for w in longest:
            if word == w:
                break
            if len(word) > len(w):
                longest = rename(longest, word, longest.index(w))
                break
    return longest

# Подсчет средней длины словоформы
def average_length(words: list[str]) -> float:
    sum_len = sum(len(word) for word in words)
    average_len = round(sum_len / len(words), 1)
    return average_len

def start() -> None:
    text = ""
    while amount_symbol(text)[0] < 100:
        text = input("Введите текст для анализа (не менее 100 символов):\n")
        text = text.replace(" — ", " ")
        text = ''.join(ch for ch in text if ch not in exclude).lower()
        if amount_symbol(text)[0] < 100:
            print(f"Ошибка! Текст меньше 100 символов \n")

    # тест
    # text = TEXT1
    # text = TEXT1
    # text = text.replace(" — ", " ")
    # text = ''.join(ch for ch in text if ch not in exclude).lower()

    symbols = amount_symbol(text)

    print("Результаты анализа:")
    print(f"Общее количество символов: {symbols[0]} (без пробелов: {symbols[1]})")

    words = amount_word_form(text)
    print(f"Количество словоформ: {words[1]}")

    print("\nСамые частые словоформы:")
    for word, freq in most_frequent_words(words[0]).items():
        print(f"- '{word}': {freq} раза")

    print("\nСамые длинные словоформы:")
    for word in longest_words(words[0]):
        print(f"- '{word}' ({len(word)} букв)")

    print(f"Средняя длина словоформы: {average_length(words[0])} символа")
    

# 24 слова в TEXT1
if __name__ == '__main__':
    start()