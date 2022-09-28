#Lab 13
#Name: Conner Um

def main():
  splitJoin()
  phoneList = readPhoneFile()
  print phoneList
  name = requestString("Enter a name:")
  findPosition(phoneList, name)
  genderReport(phoneList)
  weeklyPay(phoneList)
  

def splitJoin():
  string = "Mary 7658930234 Realtor F 25"
  list_string = string.split(' ')
  print (list_string)
  joinString = '-'.join(list_string)
  print (joinString)

def readPhoneFile():
  inFilePath = pickAFile()
  inFile = open(inFilePath, "r")
  content = inFile.read()
  inFile.close()
  phoneContent = content.split('\n')
  subPhoneList = []
  for list in phoneContent:
    subPhoneList += [list.split(":")]
  return subPhoneList
  
def findPosition(phoneList, name):
  count = 0
  for list in phoneList:
    if list[0] == name:
      count += 1
      showInformation("Position for " + name + " is " + list[2])
  if count == 0:
    showInformation("The person, " + name + ", is not in the phone book.")
  
def genderReport(phoneList):
  outFilePath = pickAFile()
  outFile = open(outFilePath, "w")
  outFile.write("The employee gender's information report " + "\n" + "\n")
  males = 0; females = 0;
  for list in phoneList:
    if list [3] == "M":
      males += 1
    if list[3] == "F":
        females += 1
  total = males + females
  fPercentage = str(100 * females / total) + '%'
  mPercentage = str(100 * males / total) + '%'
  outFile.write("\nThere are total of " + str(females) + " females' employees. " + "\n")
  outFile.write("\nThere are total of " + str(males) + " males' employees. " + "\n")
  outFile.write("\nThere are " + mPercentage + " males and " + fPercentage + " females.")
  outFile.close()
  
def weeklyPay(phoneList):
  outFilePath = pickAFile()
  outFile = open(outFilePath, "w")
  outFile.write("\tThe Weekly Payroll Report" + "\n" + "\n")
  outFile.write("Name" + "\tWeekly Pay" + "\tJob Title" + "\n")
  outFile.write("____________________________________________" + "\n")
  for list in phoneList:
    hourPay = int(list[4])
    hours = int(list[5])
    if hours > 40:
      pay = 40 * hourPay + (hours - 40)* hourPay * 1.5
    else:
      pay = hours * hourPay
    outFile.write(list[0] + "\t$" + str(pay) + "\t\t" + list[2] + "\n")
  outFile.close()