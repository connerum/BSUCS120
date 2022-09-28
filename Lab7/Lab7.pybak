def collage():
  butterfly=makePicture(pickAFile())
  explore(butterfly)
  edgePic=edge(butterfly)
  edgeColorPic=edgeColor(butterfly)
  blendPic=blend(butterfly,edgeColorPic)
  cropPic=crop(butterfly)
  negCrop=negative(cropPic)
  linePic=drawLines(butterfly)
  mirrorPic=mirror(butterfly)
  width=3*getWidth(butterfly)
  height=2*getHeight(butterfly)
  canvas=makeEmptyPicture(width, height, white)
  copyInto(butterfly, canvas, 0, 0)
  startX=getWidth(butterfly);startY=0
  copyInto(edgePic, canvas, startX, startY)
  startX=2*getWidth(butterfly);startY=0
  copyInto(mirrorPic, canvas, startX, startY)
  startX=0;startY=getHeight(butterfly)
  copyInto(blendPic, canvas, startX, startY)
  startX=getWidth(blendPic);startY=getHeight(butterfly)
  copyInto(cropPic, canvas, startX, startY)
  startX=getWidth(blendPic)
  startY=getHeight(butterfly)+getHeight(cropPic)
  copyInto(negCrop, canvas, startX, startY)
  startX=getWidth(blendPic)+getWidth(butterfly)
  startY=getHeight(butterfly)
  changeColor(canvas, startX,startY)
  signature=makePicture(pickAFile())
  signatureRight=rotateRight(signature)
  startX=getWidth(blendPic)+getWidth(butterfly)
  startY=getHeight(butterfly)
  chromakeySig(signatureRight, canvas, startX, startY)
  show(canvas)
  
def edgeColor(pic):
  newPic=duplicatePicture(pic)
  for px in getPixels(newPic):
    x = getX(px)
    y = getY(px)
    if y < getHeight(newPic) - 1 and x < getWidth(newPic) - 1:
      colorSum = getRed(px)+getGreen(px)+getBlue(px)
      pixelOverOne = getPixel(newPic, x+1, y+1)
      colorSumOverOne= getRed(pixelOverOne)+getGreen(pixelOverOne)+getBlue(pixelOverOne)
      colorDifference = abs(colorSum-colorSumOverOne)
      if colorDifference < 10:
        setColor(px, white)
      elif colorDifference > 10 and colorDifference <40:
        setColor(px, yellow)
      else:
        setColor(px,gray)
  return(newPic)
  
def edge(pic):  #Line drawing or edge detection  
  newPic=duplicatePicture(pic)
  for px in getAllPixels(newPic):
    x = getX(px)
    y = getY(px)
    if y < getHeight(newPic) - 1 and x < getWidth(newPic) - 1:
      colorSum = getRed(px)+getGreen(px)+getBlue(px)
      pixelOverOne = getPixelAt(newPic, x+1, y+1)
      colorSumOverOne= getRed(pixelOverOne)+getGreen(pixelOverOne)+getBlue(pixelOverOne)
      colorDifference = abs(colorSum-colorSumOverOne)
      #newcolor = makeColor(colorDifference, colorDifference, colorDifference)
    if colorDifference > 10:
      setColor(px, black)
    if colorDifference <= 10:
      setColor(px,white)
  return newPic
  
def blend(butterflyPic,lineDrawingPic):
  width=getWidth(butterflyPic) + int(getWidth(lineDrawingPic)*0.6)
  height=getHeight(lineDrawingPic)
  targetPic=makeEmptyPicture(width, height, white)
  butterflyEnding=int(getWidth(butterflyPic)*0.6)
  sourceX=0
  for targetX in range (0, butterflyEnding):
    sourceY=0
    for targetY in range (0, getHeight(butterflyPic)):
      butterflyColor=getColor(getPixelAt(butterflyPic, sourceX, sourceY))
      setColor(getPixel(targetPic, targetX, targetY), butterflyColor)
      sourceY+=1
    sourceX+=1
  overLap=getWidth(butterflyPic)-butterflyEnding
  sourceX=0
  for targetX in range (butterflyEnding, getWidth(butterflyPic)):
    sourceY=0
    for targetY in range (0, getHeight(lineDrawingPic)):
      butterflyPx=getPixel(butterflyPic, sourceX+butterflyEnding, sourceY)
      lineDrawingPx=getPixel(lineDrawingPic, sourceX, sourceY)
      mixedRed=0.5 * getRed(butterflyPx)+0.5*getRed(lineDrawingPx)
      mixedGreen=0.5*getGreen(butterflyPx)+0.5*getGreen(lineDrawingPx)
      mixedBlue=0.5*getBlue(butterflyPx)+0.5*getBlue(lineDrawingPx)
      mixedColor=makeColor(mixedRed,mixedGreen,mixedBlue)
      setColor(getPixelAt(targetPic, targetX, targetY),mixedColor)
      sourceY+=1
    sourceX+=1
    
  sourceX=overLap
  for targetX in range (butterflyEnding+overLap, butterflyEnding+getWidth(lineDrawingPic)):
    sourceY=0
    for targetY in range (0, getHeight(lineDrawingPic)):
      color=getColor(getPixelAt(lineDrawingPic, sourceX, sourceY))
      setColor(getPixelAt(targetPic, targetX, targetY), color)
      sourceY+=1
    sourceX+=1
  return(targetPic)
  
def crop(srcPic):
  width=getWidth(srcPic);height=getHeight(srcPic)/2
  targetPic=makeEmptyPicture(width, height)
  targetX=0
  for sourceX in range (0, width):
    targetY=0
    for sourceY in range (0, height):
      srcPx=getPixelAt(srcPic, sourceX, sourceY)
      srcColor=getColor(srcPx)
      targetPx=getPixelAt(targetPic, targetX, targetY)
      setColor(targetPx, srcColor)
      targetY=targetY+1
    targetX=targetX+1
  return targetPic

def negative(pic):
  newPic=duplicatePicture(pic)
  for px in getPixels(newPic):
    r=getRed(px)
    b=getBlue(px)
    g=getGreen(px)
    neg=makeColor(255-r, 255-g, 255-b)
    setColor(px, neg)
  return newPic
  
def drawLines(pic):
  newPic=duplicatePicture(pic)
  verticalLines(newPic)
  horizontalLines(newPic)
  return newPic
  
def horizontalLines(src):
  for x in range(0, getHeight(src), 5):
    for y in range(0, getWidth(src)):
      setColor(getPixel(src, y, x), red)
      
def verticalLines(src):
  for x in range(0, getWidth(src), 5):
    for y in range(0, getHeight(src)):
      setColor(getPixel(src, x, y), red)
      
def mirror(source):
  newPic=duplicatePicture(source)
  mirrorPoint=getHeight(newPic)/2
  height=getHeight(newPic)
  for x in range (0, getWidth(newPic)):
    for y in range (0, mirrorPoint):
      topPixel=getPixelAt(newPic, x, y)
      bottomPixel=getPixelAt(newPic, x, height-y-1)
      color=getColor(topPixel)
      setColor(bottomPixel, color)
  return newPic
  
def changeColor(canvas, startX, startY):
  replacedColor=makeColor(200, 198, 199)
  for x in range (startX, getWidth(canvas)):
    for y in range (startY, getHeight(canvas)):
      currentPx=getPixelAt(canvas, x, y)
      currentColor=getColor(currentPx)
      if (distance(currentColor, white)<200):
        setColor(currentPx, replacedColor)
        
def rotateRight(picture):
  newPict=makeEmptyPicture(getHeight(picture), getWidth(picture))
  newX=getWidth(newPict)-1
  for y in range(getHeight(picture)):
    newY=0
    for x in range (getWidth(picture)):
      px=getPixel(picture, x, y)
      newPx=getPixel(newPict, newX, newY)
      setColor(newPx, getColor(px))
      newY=newY+1
    newX=newX-1
  return newPict
  
def chromakeySig(sourcePic, canvas, targetX, targetY):
  for sX in range (0, getWidth(sourcePic)):
    for sY in range (0, getHeight(sourcePic)):
      sPx=getPixelAt(sourcePic, sX, sY)
      sColor=getColor(sPx)
      targetPx=getPixelAt(canvas, sX+targetX, sY+targetY)
      if distance(black, sColor)<180:
        setColor(targetPx, red)