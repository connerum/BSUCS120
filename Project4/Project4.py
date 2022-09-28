#Conner Um
#Project 4


class GradeBook:
  def __init__(self, studentName, studentId):
    self._name = studentName
    self._id = studentId
    self.testScores = 0
    self.countTest = 0
    self.projectScores = 0
    self.countProject = 0
    self.labScores = 0
    self.countLab = 0
    self.assignmentScores = 0
    self.countAssignment = 0
  
  def getName(self):
    return self._name
    
  def getId(self):
    return self._id
  
  def addTest(self, score):
    if (score < 0):
      showInformation("You need to enter a positive value")
    elif (score >= 0):
      self.testScores = self.testScores + score
      self.countTest = self.countTest + 1
    else:
      showInformation("You entered wrong input!!")
      
  def addProject(self, score):
    if (score < 0):
      showInformation("You need to enter a positive value")
    elif (score >= 0):
      self.projectScores = self.projectScores + score
      self.countProject = self.countProject + 1
    else:
      showInformation("You entered wrong input!!")
      
  def addLab(self, score):
    if (score < 0):
      showInformation("You need to enter a positive value")
    elif (score >= 0):
      self.labScores = self.labScores + score
      self.countLab = self.countLab + 1
    else:
      showInformation("You entered wrong input!!")  
  
  def addAssignment(self, score):
    if (score < 0):
      showInformation("You need to enter a positive value")
    elif (score >= 0):
      self.assignmentScores = self.assignmentScores + score
      self.countAssignment = self.countAssignment + 1
    else:
      showInformation("You entered wrong input!!")  
  
  
  def getAverageTest(self):
    return self.testScores / self.countTest
    
  def getAverageProject(self):
    return self.projectScores / self.countProject
    
  def getAverageLab(self):
    return self.labScores / self.countLab
    
  def getAverageAssignment(self):
    return self.assignmentScores / self.countAssignment
  
  def getFinalNumericScore(self):
    finalGrade1 = self.getAverageTest() * 0.3 + self.getAverageProject() * 0.3
    finalGrade2 = self.getAverageLab() * 0.25 + self.getAverageAssignment() * 0.15
    finalGrade = finalGrade1 + finalGrade2
    return finalGrade
    
  def getLetterGrade(self):
    grade = self.getFinalNumericScore()
    if (grade >= 93 and grade <= 100):
      return "A"
    elif (grade >= 90 and grade <= 92):
      return "A-"
    elif (grade >= 88 and grade <= 89):
      return "B+"
    elif (grade >= 83 and grade <= 87):
      return "B"
    elif (grade >= 80 and grade <= 82):
      return "B-"
    elif (grade >= 77 and grade <= 79):
      return "C+"
    elif (grade >= 73 and grade <= 76):
      return "C"
    elif (grade >= 70 and grade <= 72):
      return "C-"
    elif (grade >= 67 and grade <= 69):
      return "D+"
    elif (grade >= 63 and grade <= 66):
      return "D"
    elif (grade >= 60 and grade <= 62):
      return "D-"
    else:
      return "F"
  
  
def main():
  s1 = GradeBook("Bob", "800-86-1900")
  
  for i in range(0, 3):
    grade = requestInteger("Enter 3 test scores (70, 90, 85) for Bob:")
    s1.addTest(grade)
  for i in range(0, 4):
    grade = requestInteger("Enter 4 project scores (70, 90, 85, 80) for Bob:")
    s1.addProject(grade)
  for i in range(0, 6):
    grade = requestInteger("Enter 6 Lab scores (90, 90, 85, 80, 90, 100) for Bob:")
    s1.addLab(grade)
  for i in range(0, 5):
    grade = requestInteger("Enter 5 assignment scores (90, 90, 85, 80, 95) for Bob:")
    s1.addAssignment(grade)
    
  print s1.getId(),", ", s1.getName(),", Final Numeric score:",s1.getFinalNumericScore(), " and letter grade:",s1.getLetterGrade()
  
  s2 = GradeBook("Nancy", "800-14-1523")
  for i in range(0,3):
    grade = requestInteger("Enter 3 test scores (80,90,95) for Nancy:")
    s2.addTest(grade)
  for i in range(0,4):
    grade = requestInteger("Enter 4 project scores (90,90,85,100) for Nancy:")
    s2.addProject(grade)
  for i in range(0,6):
    grade = requestInteger("Enter 6 lab scores (90,90,95,90,90,100) for Nancy:")
    s2.addLab(grade)
  for i in range(0,5):
    grade = requestInteger("Enter 5 assignment scores (90,90,85,90,95) for Nancy:")
    s2.addAssignment(grade)
    
  print s2.getId(), ", ", s2.getName(),", Final Numeric score:",s2.getFinalNumericScore(), " and letter grade:",s2.getLetterGrade()
   