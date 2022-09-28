#Lab 12
#Name: Conner Um

class Media:
  def __init__(self, pictureFile, soundFile):
    self.picture = makePicture(pictureFile)
    self.sound = makeSound(soundFile)
    
  def getPicture(self):
    return self.picture
    
  def getSound(self):
    return self.sound
    
  def show(self):
    explore(self.picture)
    blockingPlay(self.sound)
    
  def grayScale(self):
    newPic = duplicatePicture(self.picture)
    for px in getAllPixels(newPic):
      redValue = getRed(px)
      greenValue = getGreen(px)
      blueValue = getBlue(px)
      AvgValue = (redValue + greenValue + blueValue)/3
      newColor = makeColor(AvgValue, AvgValue, AvgValue)
      setColor(px, newColor)
    addText(newPic, 10, 40, "Gray", red)
    show(newPic)
    
  def negative(self):
    newPic = duplicatePicture(self.picture)
    for px in getAllPixels(newPic):
      redValue = getRed(px)
      greenValue = getGreen(px)
      blueValue = getBlue(px)
      negativeColor = makeColor(255 - redValue, 255 - greenValue, 255 - blueValue)
      setColor(px, negativeColor)
    addText(newPic, 10, 40, "Negative", white)
    show(newPic)
    
  def echo(self):
    delay = 10000
    s1 = self.getSound()
    s2 = self.getSound()
    for index in range(delay, getLength(s1)):
      echo = 0.6 * getSampleValueAt(s2, index - delay)
      combo = getSampleValueAt(s1, index) + echo
      setSampleValueAt(s1, index, combo)
    blockingPlay(s1)
    
  def removeNegativeValues(self):
    newSound = duplicateSound(self.sound)
    for samples in range(0, getLength(newSound)):
      value = getSampleValueAt(newSound, samples)
      if value < 0:
        setSampleValueAt(newSound, samples, 0)
      else:
        pass
    explore(newSound)
    
def main():
  media1 = Media(pickAFile(), pickAFile())
  print media1.getPicture()
  print media1.getSound()
  media1.show()
  media1.grayScale()
  media1.negative()
  media1.echo()
  media1.removeNegativeValues()
  media2 = Media(pickAFile(), pickAFile())
  print media2.getPicture()
  print media2.getSound()
  media2.show()
  media2.grayScale()
  media2.negative()
  media2.echo()
  media2.removeNegativeValues()