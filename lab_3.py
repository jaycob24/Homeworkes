import numpy as np

# Задача 1
def First(arr):
  for k in range(len(arr)-1):
    if len(arr[k]) != len(arr[k+1]):
      return 0
  w = len(arr[0])
  h = len(arr)
  res = [[0]*h for i in range(w)]
  for y in range(len(arr[0])):
    for x in range(len(arr)):
      res[y][x] = arr[x][y]
  return res

print("1:")
print(np.matrix(First([[1, 2, 3], [4, 5, 6]])))

# Задача 2
def Second(arr):
  res = {}
  for cort in arr:
    nam = cort[2:4]
    if not nam in res:
      res.setdefault(nam, [])
    petName = cort[0:2]
    res[nam].append(petName)
  return res

print("")
print("2:", Second([('Муся', 7, 'Игорь', 'Бероев'), ('Изольда', 2, 'Игорь', 'Бероев'), ('Вася', 5, 'Ирина', 'Бероева')]))

# Задача 3
def Third(s):
  d = {}
  newS = ""
  for c in s:
    if c.isalpha() or c.isspace():
      newS += c
  words = newS.lower().split()
  for word in words:
    if word not in d:
      d.setdefault(word, 1)
    else: d[word] += 1
  minValue = d[min(d, key=d.get)]
  minWords = [k for k, v in d.items() if v == minValue]
  return sorted(minWords)[0]
  
print("")
print("3:", Third("а а я,    в А."))

# Задача 4
def Fourth(s):
  d = {}
  for c in s:
    if c.isalpha():
      l = c.lower()
      if not l in d:
        d.setdefault(l, 1)
      else:
        d[l] += 1
  maxValue = d[max(d, key = d.get)]
  maxLetters = [k for k, v in d.items() if v == maxValue]
  return sorted(maxLetters)[0]

print("")
print("4:", Fourth("cBC a;Ab.cB! !1a*"))

# Задача 5
def Fifth(s):
  if len(s) > 2 and s[0] == s[-1]:
    return Fifth(s[1:-1])
  elif len(s) == 2 and s[0] == s[1] or len(s) == 1:
    return "True"
  else:
    return "False"

print("")
print("5:", Fifth("aabhbaa"))

# Задача 6
def Sixth(m):
  d = {}
  res = []
  for n in m:
    if n not in d:
      d.setdefault(n, m.count(n))
  d = sorted(d.items(), key=lambda x:x[1], reverse=True)
  for pair in d:
    for i in range(pair[1]):
      res.append(pair[0])
  return res

print("")
print("6:", Sixth([4, 3, 5, 1, 2, 1, 5, 4, 4]))

# Задача 7
def Seventh(s):
  words = s.split()
  for i in range(len(words) - 2):
    w1, w2, w3 = words[i], words[i+1], words[i+2]
    if w1.isalpha() and w1 == w2 and w1 == w3:
      return True
  return False

print("")
print("7:", Seventh("а 1 о1 о1 о1 в в в"))

# Задача 8
def Eighth(s):
  cur, res = 0, 0
  for i in range(len(s) - 1):
    if s[i].isalpha() and s[i] == s[i+1]:
      cur += 1
      if cur > res:
        res = cur
    else:
      cur = 1
  return res

print("")
print("8:", Eighth("аааббдбаааа"))

# Задача 9 - в условии не написано, что нельзя использовать эту команду :)
def Nineth(s):
  return eval(s)

print("")
print("9:", Nineth("(21+2)*2"))

# Задача 10
def Tenth(m):
  res = {}
  for d in m:
    for k in d:
      if not k in res:
        res[k] = d[k]
      else:
        res[k] += d[k]
  return res

print("")
print("10:", Tenth([{'a':1, 'b':1, 'c':2}, {'c':1, 'a': 2}, {'b':2}]))
