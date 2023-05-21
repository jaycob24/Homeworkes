from abc import ABC, abstractmethod

class FigureExceptions(Exception):
  pass

class TriangleExceptions(Exception):
  pass

class QuadrilateralExceptions(Exception):
  pass

class Figure(ABC):
  def area(self, h, w):
    return h * w
    
  def perimeter(self, *sides):
    s = 0
    for n in sides:
      s += n
    return s

class Triangle(Figure):
  def __init__(self, points):
    if not len(points) == 3:
      raise FigureExceptions("Количество точек не равно 3!")
    for point in points:
      if point[0] < 0 or point[1] < 0:
        raise FigureExceptions("Координаты не положительные!")
    self.points = points
    self.x1 = self.points[0][0]
    self.x2 = self.points[1][0]
    self.x3 = self.points[2][0]
    self.y1 = self.points[0][1]
    self.y2 = self.points[1][1]
    self.y3 = self.points[2][1]
    if self.area() == 0.0:
      raise TriangleExceptions("Неправильный треугольник!")

  def area(self):
    return abs(self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2)) / 2

  def isRavn(self):
    import math
    a = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
    b = math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
    c = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
    if a == b == c or a == b or b == c or c == a:
      return True
    return False

  def computeDirection(commonPoint, firstEndpoint, secondEndpoint):
    import operator
    firstVector = tuple(map(operator.sub, firstEndpoint, commonPoint))
    secondVector = tuple(map(operator.sub, secondEndpoint, commonPoint))
    return firstVector[0] * secondVector[1] - firstVector[1] * secondVector[0]

  def doLineSegmentsIntersect(firstSegment, secondSegment):
    d1 = Triangle.computeDirection(firstSegment[0], firstSegment[1], secondSegment[0])
    d2 = Triangle.computeDirection(firstSegment[0], firstSegment[1], secondSegment[1])
    d3 = Triangle.computeDirection(secondSegment[0], secondSegment[1], firstSegment[0])
    d4 = Triangle.computeDirection(secondSegment[0], secondSegment[1], firstSegment[1])
    if d1 * d2 < 0 and d3 * d4 < 0:
      return True
    return False
    
  def intersect(firstTriangle, secondTriangle):    
    for firstTriangleSide in range(3):
      firstSide = [firstTriangle.points[firstTriangleSide], firstTriangle.points[(firstTriangleSide + 1) % 3]]
      for secondTriangleSide in range(3):
        secondSide = [secondTriangle.points[secondTriangleSide], secondTriangle.points[(secondTriangleSide + 1) % 3]]
        if Triangle.doLineSegmentsIntersect(firstSide, secondSide):
          return True
        return False

#class Quadrilateral(Figure):
#  def __init__(self, points):
#    if not len(points) == 4:
#      raise FigureExceptions("Количество точек не равно 4!")
#    for point in points:
#      if point[0] < 0 or point[1] < 0:
#        raise FigureExceptions("Координаты не положительные!")
#    if self.area()