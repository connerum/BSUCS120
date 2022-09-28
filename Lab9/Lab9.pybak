#Lab9
#Conner Um

def main():
  mergeSound = merge()
  blockingPlay(mergeSound)
  slowerSound = halfFrequency(mergeSound)
  blockingPlay(slowerSound)
  quickSound = doubleFrequency(mergeSound)
  blockingPlay(quickSound)
  echoSound = echo(mergeSound, 10000)
  blockingPlay(echoSound)
  
def merge():
  I = makeSound(pickAFile())
  vote = makeSound(pickAFile())
  president = makeSound(pickAFile())
  length = getLength(I) + getLength(vote) + getLength(president)
  targetSound = makeEmptySound(length)
  copy(I, targetSound, 0)
  copy(vote, targetSound, getLength(I))
  copy(president, targetSound, getLength(I) + getLength(vote))
  return targetSound
  
def copy(source, target, targetStart):
  targetIndex = targetStart
  for sourceIndex in range(0, getLength(source)):
    value = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, value)
    targetIndex = targetIndex + 1
    
def halfFrequency(sourceSound):
  sourceIndex = 0
  length = getLength(sourceSound) * 2
  targetSound = makeEmptySound(length)
  for targetIndex in range(0, getLength(targetSound)):
    value = getSampleValueAt(sourceSound, int(sourceIndex))
    setSampleValueAt(targetSound, targetIndex, value)
    sourceIndex = sourceIndex + 0.5
  return targetSound
  
def doubleFrequency(source):
  len = getLength(source) / 2 + 1
  newSound = makeEmptySound(len)
  newIndex = 0
  for sourceIndex in range(0, getLength(source), 2):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(newSound, newIndex, sourceValue)
    newIndex = newIndex + 1
  return newSound
  
def echo(source, delay):
  sound1 = duplicateSound(source)
  sound2 = duplicateSound(sound1)
  for index in range(delay, getLength(sound1)):
    echoValue = 0.6 * getSampleValueAt(sound2, index-delay)
    comboValue = getSampleValueAt(sound1, index) + echoValue
    setSampleValueAt(sound1, index, comboValue)
  return sound1