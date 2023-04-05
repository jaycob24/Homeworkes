import numpy as np

# Задача 1
def CalcFib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return CalcFib(n - 1) + CalcFib(n - 2)

print("#1:", CalcFib(6))

# Задача 2
def RemoveSameInArrays(a, b):
  comNs = []
  for x in a:
    for y in b:
      if x == y:
        comNs.append(x)
  newA, newB = [], []
  for n in a:
    if not n in comNs:
      newA.append(n)
  for n in b:
    if not n in comNs:
      newB.append(n)
  return newA, newB

fArray = [1, 2, 3, 4, 5, 6]
sArray = [4, 5, 6, 7, 8, 9]
fArray, sArray = RemoveSameInArrays(fArray, sArray)
print("") #это просто для красивого разделения вывода ответов
print("#2:", fArray, sArray)

#Задача 3
def RemoveSameNumbers(a, n):
  d = {}
  res = []
  for i in a:
    if not i in d:
      d[i] = 1
    else:
      d[i] += 1
  for i in a:
    if d[i] >= n and not i in res:
      res.append(i)
  return res

tArray = [1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 2, 2]
print("")
print("#3:", RemoveSameNumbers(tArray, 3))

#Задача 4
def SumInterValues(mat, lvl):
  sum = 0
  res = []
  for value in mat:
    if type(value) is list:
      value = SumInterValues(value, lvl + 1)
    if lvl == 1:
      res.append(value)
    else:
      sum += value
  if lvl == 1:
    return res
  else:
    return sum

print("")
print("#4:", SumInterValues([1, [2, [3, 4]]], 1))

#Задача 5
def FindMaxOrder(m):
  oldMinIndex = 0
  oldMaxIndex = 0
  minIndex = 0
  maxIndex = 0
  for i in range(1, len(m)):
    orderLen = maxIndex - minIndex + 1
    oldOrderLen = oldMaxIndex - oldMinIndex + 1
    if m[i] > m[i-1]:
      maxIndex = i
      if orderLen > oldOrderLen:
        oldMinIndex = minIndex
        oldMaxIndex = maxIndex
    else:
      minIndex = i
      maxIndex = i
  orderLen = maxIndex - minIndex + 1
  oldOrderLen = oldMaxIndex - oldMinIndex + 1
  if orderLen >= oldOrderLen:
    return m[minIndex:(maxIndex+1)]
  else:
    return m[oldMinIndex:(oldMaxIndex+1)]

print("")
print("#5:", FindMaxOrder([1, 2, 3, 2, 4, 5, 6, 7, 1]))

#Задача 6
def MakeFence(text):
  doUpper = True
  res = ""
  for c in text:
    if c.isalpha():
      res += c.upper() if doUpper else c.lower()
      doUpper = not doUpper
    else:
      res += c
  return res

print("")
print("#6:", MakeFence("ехехе пРифКИ!!"))

#Задача 7
#Я не придумал как сделать ромб не квадратным, слишком сложновое
def DrawRhombus(w, h):
  center = w // 2
  gap = 0
  for y in range (h):
    for x in range (w):
      if x == center + gap or x == center - gap:
        print("*", end = '')
      else:
        print(" ", end = '')
    if y < h // 2:
      gap += 1
    else:
      gap -= 1
    print("")

print("")
print("#7:")
DrawRhombus(7, 7)

#Задача 8
def DrawMatrix(n):
  mat = [[1] * n for i in range(n)]
  for y in range (1, n):
    for x in range(1, n):
      mat[y][x] = mat[y - 1][x] + mat[y][x - 1]
  return mat

print("")
print("#8:")
print(np.matrix(DrawMatrix(4)))

#Задача 9
def SumStrNumbers(s):
  res = 0
  words = s.split()
  for word in words:
    if word.isdigit():
      res += int(word)
  return res

print("")
print("#9: ", end = '')
print(SumStrNumbers("В этой 1 строке 10 всего 5 четыре числа 9"))

#Задача 10
def SumStrNumbersNotInt(s):
  res = 0
  words = s.split()
  for word in words:
    if word.isdigit():
      n = 0
      i = 1
      for c in reversed(word):
        n += (ord(c) - 48) * i
        i *= 10
      res += n
  return res

print("")
print("#10: ", end = '')
print(SumStrNumbersNotInt("В этой 1 строке 10 всего 5 четыре числа 9"))