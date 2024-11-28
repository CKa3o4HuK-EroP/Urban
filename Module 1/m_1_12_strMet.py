my_string = input()
print(f'String: {my_string}\n'
      f'Length: {len(my_string)}\n'
      f'Upper: {my_string.upper()}\n'
      f'Lower: {my_string.lower()}\n'
      f'No spaces: {my_string.replace(" ", "")}\n'
      f'First symbol: {my_string[0]}\n'
      f'Last symbol: {my_string[-1]}')
