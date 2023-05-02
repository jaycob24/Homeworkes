class Human:
  default_name = ""
  default_age = 0
  def __init__(self, name = default_name, age = default_age):
    self.name = name
    self.age = age
    self.__money = 0
    self.__house = []
  def info(self):
    print(self.name, self.age, self.__house, self.__money)
  @staticmethod
  def default_info(a = default_name, b = default_age):
    print(a, b)
  def __make_deal(self, house, price):
    self.__money = self.__money - price
    self.__house.append((house._price, house._area))
  def earn_money(self):
    self.__money += 100
  def buy_house(self, house, discount = 0):
    price = house.final_price(discount)
    if self.__money < price:
      print("Недостаточно средств!")
    else:
      self.__make_deal(house, price)
      print("Покупка успешно совершена!")

class House:
  def __init__(self, price, area):
    self._price = price
    self._area = area
  def final_price(self, discount = 0):
    return self._price * (1 - (discount/100))

class SmallHouse(House):
  def __init__(self, price, area = 40):
    self._price = price
    self._area = area

h = Human("Pupa", 30)
h.default_info()
h.info()

sh = SmallHouse(30)
h.buy_house(sh)

h.earn_money()
h.buy_house(sh)
h.info()