# numbers = [1, 2, 3]
# point having methods like draw, etc

# pascal case, EmailConverter, PointRelation etc
class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point1 = Point()
# attributes of class
point1.x = 10
point1.y = 20
print(point1.x, point1.y)
point1.draw()
point1.move()

point2 = Point()
point2.x=1
print(point2.x)