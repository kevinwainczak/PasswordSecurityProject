# Kevin Wainczak
# kwaincza + section J
# Term Project: Data Analysis

#Data Collection Counts
# Kevin Wainczak: 150
# Anmol Bajaj:	  100
# Chris Lewis:	  100
# Micah Fenner:	  100
# Bryant Backus:  100
# Tyler Wellener: 50
# Mya Snyder:	  100

#Observation from the developer:
# When I have un-even amounts of data, more heavily represented people get falsely selected more often.

import eventBasedAnimation
from Tkinter import *
import csv
import time
import random

# Text Size function taken from HW 4 write up for 15-112
def textSize(canvas, text, font):
	temp = canvas.create_text(0, 0, text=text, anchor=NW, font=font)
	(x0, y0, x1, y1) = canvas.bbox(temp)
	canvas.delete(temp)
	return (x1-x0, y1-y0)

#------------------------------------------------------------------------------
# Initialization Functions
#------------------------------------------------------------------------------

def dataAnalysisInit(data):
	# setting password, defaults, and how to know what screen to show
	data.password = ".tie5roanl"
	data.notTyped = data.password
	data.pressedLetters = ""
	data.typedLetters = ""
	data.backgroundColor = "papaya whip"
	data.aboutText = data.windowTitle = "User Verifier"
	data.startScreen = False
	data.typeScreen = False
	data.entryMode = False
	data.analyzeScreen = False
	data.incorrectUser = False
	data.resultScreen = False
	data.startImage = PhotoImage(file = 'vault.gif')
	startScreenInit(data)

def startScreenInit(data):
	data.startScreen = not(data.startScreen)
	data.startScreenText = "Please Enter Your Password\n\t'.tie5roanl'"
	data.timeList = []

def analyzeScreenInit(data):
	data.entryMode = False
	data.typeScreen = False
	data.analyzeScreen = True
	
def imageInit(data):
	data.photoList = [ ]
	for person in data.profiledUsers:
		filename = "%s.gif" % person
		data.photoList.append(PhotoImage(file=filename))
	data.photoList.append(PhotoImage(file = 'missing.gif'))

def resultScreenInit(data):
	data.analyzeScreen = False
	data.resultScreen = True
	if data.user == None:
		data.userImage = data.photoList[-1]
		data.resultText = "No User Found\nClick to Continue"
	else:
		index = data.profiledUsers.index(data.user)
		data.userImage = data.photoList[index]
		data.resultText = "%s\nIs This Correct?" % data.user
	data.yesBoxText = "YES"
	data.noBoxText = "NO"
	data.yesBoxColor = "green"
	data.noBoxColor = "red"
	data.yesBoxTextColor, data.noBoxTextColor = "white", "white"
	data.endImage = PhotoImage(file = 'security.gif')

def incorrectUserInit(data):
	data.resultScreen = False
	data.incorrectUser = True
	data.inputUser = ""
	data.existingUserText = """\
	Please type your first name using no capital letters, then press "Enter".\n\tMake sure you have saved a .gif file under your name as a profile picture.
	"""


#------------------------------------------------------------------------------
# Draw Functions
#------------------------------------------------------------------------------

def interfaceDraw(canvas, data):
	# create background
	canvas.create_image(0,0, image = data.startImage, anchor = NW)
	if data.startScreen:
		drawStart(canvas, data)
	if data.typeScreen:
		drawTypeScreen(canvas, data)
	if data.resultScreen:
		canvas.create_image(0,0, image = data.endImage, anchor = NW)
		drawResultScreen(canvas, data)
	if data.incorrectUser:
		canvas.create_image(0,0, image = data.endImage, anchor = NW)
		drawIncorrectUserScreen(canvas, data)


def drawStart(canvas, data):
	text = data.startScreenText
	font = "Arial " + str(data.width/20) + " bold"
	textWidth, textHeight = textSize(canvas, text, font)
	canvas.create_rectangle(data.width/4, data.height/4, 										data.width/4 + textWidth, 											data.height/4 + textHeight, fill = "black" )
	canvas.create_text(data.width/4, data.height/4, text = text,						   anchor = NW, fill = "white", font = font)

def drawTypeScreen(canvas, data):
	canvas.create_rectangle(274, 341, 855, 450, fill = "black", width = 3, 					    outline = "gray")
	left = data.width/4
	top = data.height/2
	font = "Arial " + str(data.width/10) + " bold"
	text = data.typedLetters
	textWidth, textHeight = textSize(canvas, text, font)
	canvas.create_text(left, top, text = text, anchor = NW,								   fill = "green", font = font)
	text = data.pressedLetters
	left += textWidth
	textWidth, textHeight = textSize(canvas, text, font)
	canvas.create_text(left, top, text = text, anchor = NW,								   fill = "gold2", font = font)
	text = data.notTyped
	left += textWidth
	canvas.create_text(left, top, text = text, anchor = NW,								   fill = "white", font = font)

def drawResultScreen(canvas, data):
	image = data.userImage
	canvas.create_image(data.width/2, data.height/2,										image = image)
	
	fill = "green2"
	font = "Arial " + str(data.width/10) + " bold"
	canvas.create_text(data.width/2, data.height/2, text = data.resultText, 			   fill = fill, font = font)
	if data.user != None:
		text = data.yesBoxText
		textWidth, textHeight = textSize(canvas, text, font)
		# textWidth, textHeight = 242, 138
		left = data.width/8
		top =  3*data.height/4
		canvas.create_rectangle(left, top, left+textWidth, top+textHeight, 				     		fill = data.yesBoxColor)
		canvas.create_text(left, top, text = text, fill = data.yesBoxTextColor, 			   anchor = NW, font = font)
		left = 6*data.width/8
		text = data.noBoxText
		textWidth, textHeight = textSize(canvas, text, font)
		#textWidth, textHeight = 182, 138
		canvas.create_rectangle(left, top, left+textWidth, top+textHeight,							fill = data.noBoxColor)
		canvas.create_text(left, top, text = text, fill = data.noBoxTextColor,				   anchor = NW, font = font)

def drawIncorrectUserScreen(canvas, data):
	canvas.create_rectangle(100, 50, 1190, 175, fill = "black")
	canvas.create_rectangle(data.width/2-100, data.height/2-30, 								data.width/2 + 100, data.height/2+30, 								fill = "black")
	font = "Arial " + str(data.width/40) + " bold"
	canvas.create_text(data.width/2, data.height/5, 									   text = data.existingUserText, fill = "white", 					   font = font)
	canvas.create_text(data.width/2, data.height/2, text = data.inputUser, 				   fill = "white", font = font)

#------------------------------------------------------------------------------
# Key Functions
#------------------------------------------------------------------------------

def keyDown(event, data):
	if data.incorrectUser:
		if event.keysym == "BackSpace":
			data.inputUser = data.inputUser[0:-1]
		elif event.keysym == "Return":
			data.user = data.inputUser
			machineLearningPart(data)
			dataAnalysisInit(data)
		else:
			data.inputUser += event.keysym
	else:
		data.startScreen = False
		data.typeScreen = True
		data.entryMode = True
		if event.keysym == "period":
			event.keysym = "."
			data.initTime = time.time()
			data.pressedLetters = ""
			data.typedLetters = ""
			data.tempTimingList = [ ]
		data.time = (event.keysym, 0, time.time() - data.initTime)
		if data.entryMode:
			data.pressedLetters += event.keysym
			data.notTyped = data.notTyped.replace(event.keysym, "")
			checkLegality(event, data)

def keyUp(event, data):
	if event.keysym == "period":
		event.keysym = "."
	data.time = (event.keysym, 1, time.time() - data.initTime)
	if data.entryMode:
		data.pressedLetters = data.pressedLetters.replace(event.keysym, "")
		data.typedLetters += event.keysym
		checkLegality(event, data) 

def checkLegality(event, data):
	data.tempTimingList.append(data.time)
	if event.keysym not in data.password:
		data.tempTimingList = [ ]
		data.typedLetters = ""
		data.notTyped = data.password
	if data.typedLetters == data.password:
		data.timeList.append(data.tempTimingList)
		data.typedLetters = ""
		data.notTyped = data.password
		analyzeScreenInit(data)
		analyzeData(data.tempTimingList, data)
	if not(data.password.startswith(data.typedLetters)):
		data.tempTimingList = [ ]
		data.typedLetters = ""
		data.notTyped = data.password

def clicked(event, data):
	if data.resultScreen and data.user != None:
		left = data.width/8
		top = 3*data.height/4
		right = left + 242
		bottom = top + 138
		if left <= event.x <= right and top <= event.y <= bottom:
			machineLearningPart(data)
			dataAnalysisInit(data)
		left = 6*data.width/8
		right = left + 182
		if left <= event.x <= right and top <= event.y <= bottom:
			incorrectUserInit(data)
	if data.resultScreen and data.user == None:
		dataAnalysisInit(data)
#------------------------------------------------------------------------------
# Data Initialization
#------------------------------------------------------------------------------

def machineLearningPart(data):
	user = data.user
	if user in data.profiledUsers:
		fieldnames = [". - Down", ". - Up", "5 - Down", "5 - Up", "a - Down", 			"a - Up", "e - Down", "e - Up", "i - Down", "i - Up", 			  "l - Down", "n - Down", "n - Up", "o - Down", "o - Up", 			"r - Down", "r - Up", "t - Down", "t - Up", "t - i Down",		   "i - e Down", "e - 5 Down", "5 - r Down", "r - o Down", 			  "o - a Down", "a - n Down", "n - l Down", ". - t Up", 		  "t - i Up", "i - e Up", "e - 5 Up", "5 - r Up", 			  	  "r - o Up", "o - a Up", "a - n Up"]
		filename = "%sTimes.csv" % user
		storedTimes = formatTimes(user)
		storedTimes.append(data.inputTimeList)
		with open(filename, 'w') as csvFile:
			write = csv.writer(csvFile)
			write.writerow(fieldnames)
			write.writerows(storedTimes)

def analyzeData(inputTimeList, data):
	collectedTimes = [ ]
	profiledUsersList = open('profiledUsers.csv', 'rU')
	for row in profiledUsersList:
		data.profiledUsers = row.split(",")
	imageInit(data)
	data.inputTimeList = formatTimeList(inputTimeList)
	for person in data.profiledUsers:
		collectedTimes.append((formatTimes(person), person))
	chiSquaredAnalysis(data.inputTimeList, collectedTimes, data)
	kNNAnalysis(data.inputTimeList, collectedTimes, data)

def formatTimes(person):
	newTimeList = []
	filename = '%sTimes.csv' % person 
	with open(filename, 'rU') as csvfile:
		timeList = csv.reader(csvfile, delimiter=' ', quotechar = '|')
		for row in timeList:
			if row[0] == '.': continue
			for char in row:
				tempList = char.split(',')
				holdList = [ ]
				for val in tempList:
					val = float(val)
					holdList.append(val)
				newTimeList.append(holdList)
	return newTimeList

def formatTimeList(timingList):
	tempList = []
	timingList = timingList[:len(timingList)-1]
	timingList = sorted(timingList)
	for i in xrange(len(timingList)):
		tempList.append(timingList[i][2])
	tempList = addDiagraphs(tempList)
	return tempList

def reorganizeTimes(inputTimeList, collectedTimes, data):
	tempList = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 		  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 			 [], [], [], [] ]
	organizedTimes = []
	for timeListTuple in collectedTimes:
		# timeListTuple[0] is the collected time list
		# timeListTuple[1] is the person
		for col in xrange(len(timeListTuple[0][0])-1):
			for row in xrange(len(timeListTuple[0])):
				tempList[col].append((timeListTuple[0][row][col],							  timeListTuple[1]))
	for i in xrange(len(inputTimeList)-1):
		tempList[i].append((inputTimeList[i], "X"))
	for times in tempList:
		times = sorted(times)
		organizedTimes.append(times)
	return organizedTimes

def addDiagraphs(tempList):
	times = tempList
	times.append(times[8]-times[17])
	times.append(times[6]-times[8])
	times.append(times[2]-times[6])
	times.append(times[15]-times[2])
	times.append(times[13]-times[15])
	times.append(times[4]-times[13])
	times.append(times[11]-times[4])
	times.append(times[10]-times[11])
	times.append(times[18]-times[1])
	times.append(times[9]-times[18])
	times.append(times[7]-times[9])
	times.append(times[3]-times[7])
	times.append(times[16]-times[3])
	times.append(times[14]-times[16])
	times.append(times[5]-times[14])
	times.append(times[12]-times[5])
	return tempList

#------------------------------------------------------------------------------
# Data Analysis
#------------------------------------------------------------------------------
# Chi-Squared
#------------------------------------------------------------------------------

def chiSquaredAnalysis(inputTimeList, collectedTimes, data):
	person = None
	# using some ridiculous value as a base
	bestChiSquared = 10**5
	for people in collectedTimes:
		chiSquared = chiSquaredCalculation(inputTimeList, people[0])
		if chiSquared < bestChiSquared:
			bestChiSquared = chiSquared
			person = people[1]
	print person
	return person

def chiSquaredCalculation(inputList, otherTimingList):
	# using some ridiculous value for our base case
	bestChiSquared = 10**5
	for timeList in otherTimingList:
		chiSquared = 0
		for i in xrange(len(inputList)):
			chiSquared += ((timeList[i] - inputList[i])**2)/timeList[i]
		if chiSquared < bestChiSquared:
			bestChiSquared = chiSquared
	return bestChiSquared

#------------------------------------------------------------------------------
# k-Nearest Neighbors
#------------------------------------------------------------------------------

def kNNAnalysis(inputTimeList, collectedTimes, data):
	k = 13
	organizedTimes = []
	collectedTimes = reorganizeTimes(inputTimeList, collectedTimes, data)
	for i in xrange(len(collectedTimes)):
		index = collectedTimes[i].index((inputTimeList[i], 'X'))
		organizedTimes.append(collectedTimes[i][index-k-1:index+k+1])
	organizedTimes = organizedTimes[1:]
	classes = dict()
	for values in organizedTimes:
		person, kValue = mostFrequentClass(values, k)
		if person in classes:
			classes[person] += kValue
		else:
			classes[person] = kValue
	count = 0
	print classes
	closestPerson = None
	for person in classes:
		if classes[person] > count and classes[person] >= 60:
			count = classes[person]
			closestPerson = person
		if classes[person] == count:
			closestPerson = random.choice([person,closestPerson])
	data.user = closestPerson
	resultScreenInit(data)
	print closestPerson
	return closestPerson

def mostFrequentClass(values,k):
	classes = dict()
	for dataPoint in values:
		dataPoint = (abs(dataPoint[0] - values[k][0]), dataPoint[1])
	values = sorted(values)
	values = values[1:k+1]
	try:
		kValue = abs(1.0/values[0][0])
	except:
		kValue = 0
	count = 0
	closestPerson = None
	for dataPoint in values:
		if dataPoint[1] in classes:
			classes[dataPoint[1]] += 1
		else:
			classes[dataPoint[1]] = 1
	for person in classes:
		if classes[person] > count:
			count = classes[person]
			closestPerson = person
		if classes[person] == count:
			person = random.choice([person, closestPerson])
	return closestPerson, kValue
	
#------------------------------------------------------------------------------
# Run Function
#------------------------------------------------------------------------------

eventBasedAnimation.run(
	width = 1200,
	height = 650,
	initFn = dataAnalysisInit,
	drawFn = interfaceDraw,
	keyFn = keyDown,
	mouseFn = clicked,
	keyReleaseFn = keyUp,
	timerDelay = 100)




