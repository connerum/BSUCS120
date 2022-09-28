#Lab 11
#Name: Conner Um

def main():
  earth = World(650, 500)
  
  t1 = Turtle(earth)
  print t1.getXPos()
  print t1.getYPos()
  
  t2 = Turtle(earth)
  t3 = Turtle(earth)
  t4 = Turtle(earth)
  t1Position(t1)
  t2Position(t2)
  t3Position(t3)
  t4Position(t4)
  chase(t1, t2, t3, t4)
  turtleDuel()
  
def t1Position(t1):
  t1.color = red
  t1.penUp()
  t1.moveTo(10, 10)
  t1.penDown()
  t1.setPenWidth(3)
  
def t2Position(t2):
  t2.color = blue
  t2.penUp()
  t2.moveTo(10, 400)
  t2.penDown()
  t2.setPenWidth(3)
  
def t3Position(t3):
  t3.color = black
  t3.penUp()
  t3.moveTo(400, 10)
  t3.penDown()
  t3.setPenWidth(3)
  
def t4Position(t4):
  t4.color = green
  t4.penUp()
  t4.moveTo(400, 400)
  t4.penDown()
  t4.setPenWidth(3)
  
def chase(t1, t2, t3, t4):
  for i in range(0, 300):
    chaseTurtle(t1, t3)
    chaseTurtle(t3, t4)
    chaseTurtle(t4, t2)
    chaseTurtle(t2, t1)
    
def chaseTurtle(turtle1, turtle2):
  turtle1.turnToFace(turtle2)
  turtle1.forward(4)
  
def turtleDuel():
  earth = World(400, 400)
  t1 = makeTurtle(earth)
  t1.color = red
  t1.turn(90)
  t2 = makeTurtle(earth)
  t2.color = blue
  turn(t2, 180)
  for turtle in getTurtleList(earth):
    forward(turtle, 200)
  turnToFace(t1, t2)
  t1.forward(150)
  turnToFace(t2, t1)
  t2.forward(150)