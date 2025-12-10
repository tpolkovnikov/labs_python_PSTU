# найти делители числа
def find_divisors(number: int) -> list[int]:
    divisors = []
    divisors.append(1)
    temp_number = int(number)
    for i in range(2, temp_number // 2 + 1):
        if temp_number % i == 0:
            divisors.append(int(i))
    divisors.append(int(temp_number))
    return divisors

# проверка на простоту
def check_simple(divisors: list[int]) -> bool:
    if len(divisors) == 2:
        return True
    return False

# проверка на совершенность
def check_perfect(number: int, divisors: list[int]) -> bool:
    if number == int(sum((divisors))) - number:
        return True
    return False


# функция main
if __name__ == '__main__':
    number = None

    while number is None:
        print('Введите целое число больше 0: ', end='')
        try:
            n = int(input())
            if n > 0:
                number = n
            else:
                print('Число должно быть > 0\n')
        except (ValueError, TypeError):
            print('Введите корректное целое число!\n')

    # Если валидация прошла - дальше
    divisors = find_divisors(number)
    print ("Делители числа:", divisors)
    
    # проверка на простое
    if check_simple(divisors):
        print('Число ' + str(number) + ' является простым')
    else:
        print('Число ' + str(number) + ' не является простым')

    amount = '(' + str(divisors[0])
    # проверка на совершенное
    if check_perfect(number, divisors):
        print('Число ' + str(number) + ' является совершенным ', end = '')
        for i in range (1, len(divisors) - 1):
            amount += '+' + str(divisors[i])
        amount += '=' + str(number) + ')'
        print (amount)
    else:
        print('Число ' + str(number) + ' не является совершенным')
