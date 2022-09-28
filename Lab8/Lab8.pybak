#Lab8
#Name: Conner Um

def main():
  mySound = makeSound(pickAFile())
  explore (mySound)
  printSoundInformation(mySound)
  printSampleValues(mySound)
  max = maxSampleValue(mySound)
  print "Max sample value:", max
  min = minSampleValue(mySound)
  print "Minimum sample value:", min
  countPositiveNegativeValues(mySound)
  newSound = increaseAndDecrease(mySound)
  blockingPlay(newSound)
  printSampleValues(newSound)
  
def printSoundInformation(sound):
  totalSample = getNumSamples(sound)
  duration = getDuration(sound)
  rate = getSamplingRate(sound)
  print "The total of samples is:", totalSample
  print "It will take ", int(duration), " seconds to play this sound"
  print "The sample rate is ", rate, " per second"
  
def printSampleValues(sound):
  arraySample=[]
  for sampleIndex in range (0, 10):
    value = getSampleValueAt(sound, sampleIndex)
    arraySample.insert(sampleIndex, value)
  print arraySample
  
def maxSampleValue(sound):
  max = -32768
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > max:
      max = value
    else:
      pass
  return max
  
def minSampleValue(sound):
  min = 32767
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value < min:
      min = value
    else:
      pass
  return min
  
def countPositiveNegativeValues(sound):
  count1 = 0; count2 = 0
  for sample in getSamples(sound):
    sampleValue = getSampleValue(sample)
    if sampleValue > 0:
      count1+=1
    else:
      count2+=1
  print "Total positive sample value is: ", count1
  print "Total negative sample value is: ", count2
  
def increaseAndDecrease(sound):
  newSound = duplicateSound(sound)
  numSamples = getNumSamples(newSound)
  for index in range(numSamples/2):
    value = getSampleValueAt(newSound, index)
    setSampleValueAt(newSound, index, value * 2)
  for index in range(numSamples/2, numSamples):
    value = getSampleValueAt(newSound, index)
    setSampleValueAt(newSound, index, value * 0.60)
  return newSound