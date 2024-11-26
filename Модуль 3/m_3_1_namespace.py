def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    ln = len(string)
    hi = string.upper()
    lo = string.lower()
    result = (ln, hi, lo)
    return result


def is_contains(sample, sourse):
    count_calls()
    flag = False
    for string in sourse:
        if sample.lower() == string.lower():
            flag = True
            break
    return flag


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
