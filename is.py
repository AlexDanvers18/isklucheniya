a = input('Ввведите операцию, используя метод "Польской нотации" ')
b = a.split(' ')

#AssertionError
b[0] == '+'
assert b[0] in ['+', '-', '*', '/'], 'Внимание! Неверный знак операции.'
print(b)

try:
  if b[0] == '+':
    result = int(b[1]) + int(b[2])
  elif b[0] == '-':
    result = int(b[1]) - int(b[2])
  elif b[0] == '*':
    result = int(b[1]) * int(b[2])
  elif b[0] == '/':
    result = int(b[1]) / int(b[2])
  print(result)
except ZeroDivisionError:
    print('Внимание! Делить на ноль нельзя.')
except ValueError:
    print('Внимание! Ошибка в типе значения.')
except IndexError:
    print('Внимание! Неправильное количество аргументов.')

