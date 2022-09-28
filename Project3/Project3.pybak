#Project3
#Conner Um

def main():
  sound1 = makeSound(pickAFile())
  sound2 = makeSound(pickAFile())
  #explore(sound1)
  #explore(sound2)
  start = 46400
  end = 58600
  test = clip(sound1, start, end)
  #blockingPlay(test)
  start = 30794
  end = 54023
  aroundMe = clip(sound2, start, end)
  #blockingPlay(aroundMe)
  testAroundMe = merge(test, aroundMe)
  #blockingPlay(testAroundMe)
  slowerSound = halfFrequency(testAroundMe)
  #blockingPlay(slowerSound)
  normalizedSound = normalize(testAroundMe)
  #blockingPlay(normalizedSound)
  echoSound = echo(testAroundMe, 10000)
  #blockingPlay(echoSound)
  onlyPositive = removeNegativeValues(testAroundMe)
  explore(onlyPositive)
  
def clip(source, start, end):
  target = makeEmptySound(end - start)
  tIndex = 0
  for sIndex in range(start, end):
    value = getSampleValueAt(source, sIndex)
    setSampleValueAt(target, tIndex, value)
    tIndex = tIndex + 1
  return target
  
def merge(test, aroundMe):
  length = getLength(test) + getLength(aroundMe)
  mergedSong = makeEmptySound(length)
  copy(test, mergedSong, 0)
  copy(aroundMe, mergedSong, getLength(test))
  return mergedSong
  
def copy(source, target, targetStart):
  targetIndex = targetStart
  for sourceIndex in range(0, getLength(source)):
    value = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, value)
    targetIndex = targetIndex + 1
    
def normalize(sound):
  newSound = duplicateSound(sound)
  largest = 0
  for sample in getSamples(newSound):
    largest = max(largest, abs(getSampleValue(sample)))
  factor = 32767.0/largest
  for sample in getSamples(newSound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
  return newSound
    
def halfFrequency(sourceSound):
  sourceIndex = 0
  length = getLength(sourceSound) * 2
  targetSound = makeEmptySound(length)
  for targetIndex in range(0, getLength(targetSound)):
    value = getSampleValueAt(sourceSound, int(sourceIndex))
    setSampleValueAt(targetSound, targetIndex, value)
    sourceIndex = sourceIndex + 0.5
  return targetSound
  
def echo(source, delay):
  sound1 = duplicateSound(source)
  sound2 = duplicateSound(sound1)
  for index in range(delay, getLength(sound1)):
    echoValue = 0.6 * getSampleValueAt(sound2, index-delay)
    comboValue = getSampleValueAt(sound1, index) + echoValue
    setSampleValueAt(sound1, index, comboValue)
  return sound1
  
def removeNegativeValues(sound):
  noNegVal = duplicateSound(sound)
  for sample in getSamples(noNegVal):
    value = getSampleValue(sample)
    if value < 0:
      setSampleValue(sample, 0)
  return noNegVal