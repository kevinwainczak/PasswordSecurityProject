# Kevin Wainczak
# kwaincza + section J
#Term Project: Data Collection

import eventBasedAnimation
# event based animation taken from 15-112 course
from Tkinter import *
from ttk import *
import time
import csv

# Text Size function taken from HW 4 write up for 15-112
def textSize(canvas, text, font):
	temp = canvas.create_text(0, 0, text=text, anchor=NW, font=font)
	(x0, y0, x1, y1) = canvas.bbox(temp)
	canvas.delete(temp)
	return (x1-x0, y1-y0)
#------------------------------------------------------------------------------
# Initialization Functions
#------------------------------------------------------------------------------

def sortTimingList(timingList):
	tempList = [ ]
	for times in timingList:
		tempList.append(sorted(times))
	return tempList

def addDiagraphs(data):
	for times in data.timingList:
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

def passwordInit(data):
	data.initTime = time.time()
	data.aboutText = data.windowTitle = "Kevin Wainczak's Password Collector"
	data.profile = None
	# Selected the Profile. If "Kevin Wainczak", then we will compare for analysis, otherwise, just performing data collection
	data.password = ".tie5roanl"
	# Password used by professor maxion in his research
	# Following Falses are for displaying the correct screen
	data.startScreen = False
	data.prepScreen = False
	data.startTrials = False
	data.practice = False
	data.interim = False
	data.trials = False
	data.endScreen = False
	data.inputUser = ""
	data.existingUserScreen, data.newUserScreen = False, False
	data.existingUser, data.newUser = False, False
	data.tempTimingList = [ ]
	data.timeList = [ ]	
	startScreenInit(data)

def startScreenInit(data):
	# Starts displaying the Start Screen
	data.startScreen = not(data.startScreen)
	data.startScreenText = "Password Collector\nSelect Your Keyboard"
	data.kBOneColor = "firebrick"
	data.kBTwoColor = "midnight blue"
	data.kBTextColor = "white"
	data.kBOneText = "Existing User"
	data.kBTwoText = "New User"

def selectUserInit(data):
	data.existingUserText = """\
	Please type your first name using no capital letters, then press "Enter".\n\tMake sure you have saved a .gif file under your name as a profile picture.
	"""
	
def prepScreenInit(data):
	if data.existingUser:
		existingTimeList = []
		filename = "%sTimes.csv" % data.inputUser
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
					existingTimeList.append(holdList)
		data.existingTimeList = existingTimeList
	# Tells the program to display the prep Screen
	data.newUserScreen, data.existingUserScreen = False, False
	data.prepScreen = not(data.prepScreen)
	data.prepScreenText = """
			You will be asked to type a password given to you 50 times.
			It will consist of only lowercase characters and 
			symbols (i.e. ?!*%$@ etc.)
			On the next screen, you will have a chance to practice 
			inputting the password 5 times.
			An attempt to input the password is only valid if the entire
			password is entered correctly.
			There is no rush, please take your time!
			Press 'Start' to begin!"""

def practiceInit(data):
	# Counts how many times the password has been inputted
	data.practiceCounter = 0
	# Tells the program to display the practice screen
	data.prepScreen, data.practice = not(data.prepScreen), not(data.practice)
	data.typedLetters = ""
	data.pressedLetters = ""
	data.notTyped = data.password
	data.typedColor = "green"
	data.pressedColor = "gold2"
	data.notTypedColor = "black"

def interimScreenInit(data):
	# Tells the program to display the interim screen
	data.practice, data.interim = not(data.practice), not(data.interim)
	data.interimButtonColor = "lime green"
	data.interimButtonOutline = "green"
	data.interimButtonText = "START"
	data.interimScreenText = "Press 'Start' to begin the 50 trials"
	
def trialsInit(data):
	data.tempTimingList = [ ]
	data.timeList = [ ]
	data.progressBar = Progressbar(length = data.width, maximum = 50)
	# Tells the program to display the trials screen
	data.interim, data.trials = not(data.interim), not(data.trials)
	# Creates a progress bar for our 50 trials
	data.drawProgressBar = True
	data.typedLetters = ""
	data.pressedLetters = ""
	data.notTyped = data.password
	data.typedColor = "green"
	data.pressedColor = "gold2"
	data.notTypedColor = "black"
	data.counter = 0

def formatTimingList(timingList):
	newTimingList = [ ]
	for trial in timingList:
		tempList = [ ]
		for dataPoint in trial:
			tempList.append(dataPoint[2])
		newTimingList.append(tempList)
	return newTimingList

def endScreenInit(data):
	if data.newUser:
		profiledUsers = open('profiledUsers.csv', 'rU')
		for row in profiledUsers:
			newProfiledUsers = row.split(",")
		newProfiledUsers.append(data.inputUser)
		with open('profiledUsers.csv', 'w') as csvFile:
			write = csv.writer(csvFile)
			write.writerow(newProfiledUsers)
	data.trials, data.endScreen = not(data.trials), not(data.endScreen)
	data.timingList = sortTimingList(data.timeList)
	data.timingList = formatTimingList(data.timingList)
	addDiagraphs(data)
	if data.existingUser:
		for trial in data.timingList:
			data.existingTimeList.append(trial)
	else:
		data.existingTimeList = data.timingList
	filename = "%sTimes.csv" % data.inputUser
	with open(filename, 'w') as csvFile:
		fieldnames = [". - Down", ". - Up", "5 - Down", "5 - Up", "a - Down", 			"a - Up", "e - Down", "e - Up", "i - Down", "i - Up", 			  "l - Down", "n - Down", "n - Up", "o - Down", "o - Up", 			"r - Down", "r - Up", "t - Down", "t - Up", "t - i Down",		   "i - e Down", "e - 5 Down", "5 - r Down", "r - o Down", 			  "o - a Down", "a - n Down", "n - l Down", ". - t Up", 		  "t - i Up", "i - e Up", "e - 5 Up", "5 - r Up", 			  	  "r - o Up", "o - a Up", "a - n Up"]
		write = csv.writer(csvFile)
		write.writerow(fieldnames)
		write.writerows(data.existingTimeList)
	data.endButtonText = "END"
	data.endButtonColor = "firebrick"
	data.endButtonOutline = "red"
	data.endText = " Thank you for participating!"

#------------------------------------------------------------------------------
# Drawing Functions
#------------------------------------------------------------------------------

def interfaceDraw(canvas, data):
	backgroundColor = "papaya whip"
	#background created
	canvas.create_rectangle(0,0,data.width, data.height,
							fill = backgroundColor)
	if data.startScreen:
		drawStart(canvas, data)
	if data.existingUserScreen or data.newUserScreen:
		drawUserScreen(canvas, data)
	if data.prepScreen:
		drawPrep(canvas, data)
	if data.practice:
		drawPractice(canvas, data)
	if data.interim:
		drawInterimScreen(canvas,data)
	if data.trials:
		drawTrials(canvas, data)
	if data.endScreen:
		drawEndScreen(canvas, data)

def drawStart(canvas, data):
	margin = 5
	#text for start screen
	canvas.create_text(data.width/2, data.height/4, text =data.startScreenText,
					   fill = "black", 										font = "krungthep " + str(data.width/25) +" bold")
	font = "krungthep " +str(data.width/35) + " bold"
	left = data.width/5
	top = 3*data.height/5
	textWidth, textHeight = textSize(canvas, data.kBOneText, font)
	#print textWidth, textHeight # needs to be hardcoded. returns 234 and 39
	#keyboard one "button"
	canvas.create_rectangle(left-margin, top-margin, left + textWidth+margin, 					  top+textHeight+margin, fill = data.kBOneColor, 						outline = "red", width = 3)
	canvas.create_text(left, top, text = data.kBOneText, anchor = NW,					   fill = data.kBTextColor, font = font)
	#keyboard two "button"
	textWidth, textHeight = textSize(canvas, data.kBTwoText, font)
	left *= 3
	canvas.create_rectangle(left-margin, top-margin, left + textWidth+margin, 					  top+textHeight + margin, fill = data.kBTwoColor,						outline = "dodger blue", width = 3)
	canvas.create_text(left, top, text = data.kBTwoText, anchor = NW,					   fill = data.kBTextColor, font = font)

def drawUserScreen(canvas, data):
	font = "krungthep " + str(data.width/40) + " bold"
	canvas.create_text(data.width/2-82, data.height/5, 									   text = data.existingUserText, fill = "black", 					   font = font)
	canvas.create_text(data.width/2, data.height/2, text = data.inputUser, 				   fill = "black", font = font)

def drawPrep(canvas, data):
	margin = 5
	canvas.create_text(data.width/4, data.height/2, text = data.prepScreenText,
					  fill = "black",										font = "krungthep " + str(data.width/35) +" bold")
	text = "START"
	font = "krungthep " + str(data.width/35) + " bold"
	textWidth, textHeight = textSize(canvas, text, font)
	top = data.height/10
	left = data.width/2
	canvas.create_rectangle(left - margin, top - margin, 										left + textWidth + margin, 											top + textHeight + margin, fill = "lime green", 					outline = "green", width = 3)
	canvas.create_text(left, top, text = text, anchor = NW, fill = "white",				   font = font)

def drawPractice(canvas, data):
	if data.typedLetters == "": text = "Begin Typing"
	else: text = ""
	canvas.create_text(data.width/2, data.height/5, text = text, 						   fill = "black", 													   font = "krungthep " + str(data.width/35) + " bold")
	left = data.width/4
	top = data.height/2
	font = "krungthep " + str(data.width/10) + " bold"
	text = data.typedLetters
	textWidth, textHeight = textSize(canvas, text, font)
	# TYPED LETTERS --------------------------------------
	canvas.create_text(left, top, text = text, anchor = NW, 							   fill = data.typedColor, font = font)
	text = data.pressedLetters
	left += textWidth
	textWidth, textHeight = textSize(canvas, text, font)
	# PRESSED LETTERS -------------------------------------
	canvas.create_text(left, top, text = text, anchor = NW, 							   fill = data.pressedColor, font = font)
	text = data.notTyped
	left += textWidth
	# NOT TYPED LETTERS ------------------------------------
	canvas.create_text(left, top, text = text, anchor = NW, 							   fill = data.notTypedColor, font = font)

def drawInterimScreen(canvas, data):
	margin = 5
	font = "krungthep " + str(data.width/25) + " bold"
	top = data.height/10
	left = data.width/2
	textWidth, textHeight = textSize(canvas, data.interimButtonText, font)
	# print textWidth, textHeight # returns 162, 55, need to hardcode this
	# create button text
	canvas.create_rectangle(left-margin, top-margin, left+textWidth+margin, 					top+textHeight+margin, 												fill = data.interimButtonColor, 									outline = data.interimButtonOutline, width = 3)
	canvas.create_text(left, top, text = data.interimButtonText, anchor = NW, 				 fill = "white", font = font)
	font = "krungthep " + str(data.width/20) + " bold"
	canvas.create_text(data.width/2, data.height/2, 									   text = data.interimScreenText, fill = "black", 					   font = font)

def drawTrials(canvas, data):
	if data.drawProgressBar:
		data.progressBar.pack()
	if data.typedLetters == "": text = "Begin Typing"
	else: text = ""
	canvas.create_text(data.width/2, data.height/5, text = text, 						   fill = "black", 													   font = "krungthep " + str(data.width/35) + " bold")
	left = data.width/4
	top = data.height/2
	font = "krungthep " + str(data.width/10) + " bold"
	text = data.typedLetters
	textWidth, textHeight = textSize(canvas, text, font)
	# TYPED LETTERS --------------------------------------
	canvas.create_text(left, top, text = text, anchor = NW, 							   fill = data.typedColor, font = font)
	text = data.pressedLetters
	left += textWidth
	textWidth, textHeight = textSize(canvas, text, font)
	# PRESSED LETTERS -------------------------------------
	canvas.create_text(left, top, text = text, anchor = NW, 							   fill = data.pressedColor, font = font)
	text = data.notTyped
	left += textWidth
	# NOT TYPED LETTERS ------------------------------------
	canvas.create_text(left, top, text = text, anchor = NW, 							   fill = data.notTypedColor, font = font)

def drawEndScreen(canvas, data):
	font = "krungthep " + str(data.width/20) + " bold"
	margin = 5 
	left = data.width/2
	top = data.height/10
	textWidth, textHeight = textSize(canvas, data.endButtonText, font)
	#print textWidth, textHeight # returns 129, 69
	canvas.create_rectangle(left-margin, top-margin, left+textWidth+margin,						top+textHeight+margin, fill = data.endButtonColor,					  outline = data.endButtonOutline, width = 3)
	canvas.create_text(left, top, text = data.endButtonText, anchor = NW,				   fill = "white", font = font)
	font = "krungthep " + str(data.width/20) + " bold"
	canvas.create_text(data.width/2, data.height/2, text = data.endText,				   fill = "black", font = font)

#------------------------------------------------------------------------------
# Mouse Related Functions
#------------------------------------------------------------------------------

def clicked(event, data):
	if data.startScreen:
		checkStartClick(event, data)
	if data.prepScreen:
		checkPrepClick(event, data)
	if data.interim:
		checkInterimClick(event, data)
	if data.endScreen:
		checkEndClick(event, data)

def checkStartClick(event, data):
	margin = 5
	left = data.width/5 - margin 
	top = 3*data.height/5 - margin 
	right = left + 234 + margin
	bottom = top + 39 + margin 
	if left <= event.x <= right and top <= event.y <= bottom:
		existingUserSelected(data)
	left = 3*left - margin 
	right = left + 234 + margin 
	if left <= event.x <= right and top <= event.y <= bottom:
		newUserSelected(data)

def checkPrepClick(event, data):
	margin = 5
	left = data.width/2 - margin
	top = data.height/10 - margin
	right = left + 115 + margin
	bottom = top + 39 + margin
	if left <= event.x <= right and top <= event.y <= bottom:
		practiceInit(data)

def checkInterimClick(event, data):
	margin = 5
	left = data.width/2 - margin
	top = data.height/10 - margin
	right = left + 162 + margin
	bottom = top + 55 + margin
	if left <= event.x <= right and top <= event.y <= bottom:
		trialsInit(data)

def checkEndClick(event, data):
	margin = 5
	left = data.width/2 - margin
	top = data.height/10 - margin
	right = left + margin + 129
	bottom = top + margin + 69
	if left <= event.x <= right and top <= event.y <= bottom:
		data.drawProgressBar = False
		passwordInit(data)

#------------------------------------------------------------------------------
# "Button" Functions
#------------------------------------------------------------------------------

def existingUserSelected(data):
	data.existingUser = True
	data.startScreen, data.existingUserScreen = not(data.startScreen), 												not(data.existingUserScreen)
	selectUserInit(data)

def newUserSelected(data):
	data.newUser = True
	data.startScreen, data.newUserScreen = not(data.startScreen), 											   not(data.newUserScreen)
	selectUserInit(data)

#------------------------------------------------------------------------------
# Keyboard Related Functions
#------------------------------------------------------------------------------

def keyDown(event, data):
	if data.existingUserScreen or data.newUserScreen:
		if event.keysym == "BackSpace":
			data.inputUser = data.inputUser[0:-1]
		elif event.keysym == "Return":
			prepScreenInit(data)
			data.existingUserScreen, data.newUserScreen = False, False
		else:
			data.inputUser += event.keysym
	else:
		# we want '.' to appear, not 'period', so we switch it.
		if event.keysym == "period":
				event.keysym = "."
				data.initTime = time.time()
				data.pressedLetters = ""
				data.typedLetters = ""
				data.tempTimingList = [ ]
				# set our initial 'zero' time
		# create a tuple of time, key, and up or down
		# down is represented by a 0
		data.time = (event.keysym, 0, time.time() - data.initTime)
		if data.practice or data.trials:
			data.pressedLetters += event.keysym
			data.notTyped = data.notTyped.replace(event.keysym, "")
			checkLegality(event, data)

def keyUp(event, data):
	if not(data.existingUserScreen) and not(data.newUserScreen):
		if event.keysym == "period":
				event.keysym = "."
		# the up is represented by a 1
		data.time = (event.keysym, 1, time.time() - data.initTime)
		if data.practice or data.trials:
			data.pressedLetters = data.pressedLetters.replace(event.keysym, "")
			data.typedLetters += event.keysym
			checkLegality(event,data)

#------------------------------------------------------------------------------
# Legality Functions
#------------------------------------------------------------------------------

def checkLegality(event, data):
	if event.keysym not in data.password:
		data.tempTimingList = [ ]
		data.typedLetters = ""
		data.notTyped = data.password
	if data.typedLetters == data.password:
		data.timeList.append(data.tempTimingList)
		data.tempTimingList = [ ]
		data.typedLetters = ""
		data.notTyped = data.password
		data.practiceCounter += 1
		if data.practice:
			if data.practiceCounter == 5:
				interimScreenInit(data)
		if data.trials:
			data.progressBar.step()
			data.counter += 1
			if data.counter == 50:
				endScreenInit(data)
	if not(data.password.startswith(data.typedLetters)):
		data.tempTimingList = [ ]
		data.typedLetters = ""
		data.notTyped = data.password
	data.tempTimingList.append(data.time)

#------------------------------------------------------------------------------
# Run Function
#------------------------------------------------------------------------------

eventBasedAnimation.run(
	width = 1200,
	height = 650,
	initFn = passwordInit,
	drawFn = interfaceDraw,
	mouseFn = clicked,
	keyFn = keyDown,
	keyReleaseFn = keyUp)

