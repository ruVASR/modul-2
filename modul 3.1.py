# Создание глобальной переменной calls
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    global calls
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    global calls
    count_calls()
    for item in list_to_search:
        if item.lower() == string.lower():
            return True
    return False

# Вызов функций string_info и is_contains произвольное количество раз
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

# Вывод значения переменной calls на экран
print(calls)