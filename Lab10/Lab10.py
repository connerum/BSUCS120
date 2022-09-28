#Lab 10
#Name: Conner Um

import random

def main():
  whileLoopATM()
  searchName()
  listRandomNumber()
  listMethods()
  
def whileLoopATM():
  numberTry=0
  while (numberTry<3):
    pin = requestInteger("Please enter your PIN")
    if (pin==1994):
      showInformation("Please go to your checking account!")
      break
    else:
      showInformation("Please try again!")
    numberTry += 1
  
  if (pin!=1994):
    showInformation("You have tried more than 3 times!")
  else:
    showInformation("Cash amount: $20 or $100")
    
def searchName():
  name = ['Nancy', 'Tom', 'George', 'Emily', 'Paul']
  request = requestString("Enter a name:")
  index = 0
  found = 0
  while index < len(name):
    if name[index] == request:
      showInformation("Name was found in the list!")
      found = 1
      break
    index += 1
  if (found == 0):
    showInformation("Name was not found!")
    
def listRandomNumber():
  list=[]
  index = 0; sum = 0
  while (index < 20):
    number = random.randint(1, 50)
    list.append(number)
    sum += list[index]
    index += 1
  print list
  print "The maximum number is:", max(list)
  print "The minimum number is:", min(list)
  print "The Average is:", sum/len(list)
  
def listMethods():
  names = ['Bob', 'Nancy', 'Jeff', 'Paul']
  names.append('Emily')
  names.insert(0, 'Robert')
  names.insert(2, 'Emily')
  names.extend(['Jack', 'Eli'])
  print names
  print names[1:6:2]
  print "Jack's index =", names.index('Jack')
  names.append('Jeff')
  print "There are ", names.count('Jeff'), "Jeff"
  names.remove('Jeff')
  print names.pop(2)
  print names
  print names[2:7]
  names.sort()
  print names
  names.reverse()
  print names