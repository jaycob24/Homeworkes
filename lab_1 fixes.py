def CountZeroes(n):
  zs  = 0
  for i in reversed(n):
    if (i == "0"):
      zs += 1
    else:
      break
  print("Количество нулей в конце строки:", zs)

def IsSame(m):
  b = True
  for i in m:
    if not i == m[0]:
      b = False
      break
  if b: print("Массив состоит из одинаковых значений")
  else: print("Массив не состоит из одинаковых значений")

def ReturnValues(matrix):
  for value in matrix:
    if type(value) is list:
      ReturnValues(value)
    else:
      print(value, end =' ')

# 4 задача
number = str(input("Введите строку для подсчета количества нулей в конце: "))
CountZeroes(number)

# 6 задача
a = input("\nВведите массив через пробелы: ")
if a == "":
  print("Массив пустой")
else:
  a = a.split()
  IsSame(a)

# 8 задача
a = [[1, 2], [[3, [1, [2]]], 5], 6]
print()
ReturnValues(a)