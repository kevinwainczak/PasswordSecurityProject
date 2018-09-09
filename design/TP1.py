import eventBasedAnimation
from Tkinter import *
import tkMessageBox
import tkSimpleDialog

class Struct(object): pass

# Text Size function taken from HW 4 write up for 15-112
def textSize(canvas, text, font):
	temp = canvas.create_text(0, 0, text=text, anchor=NW, font=font)
	(x0, y0, x1, y1) = canvas.bbox(temp)
	canvas.delete(temp)
	return (x1-x0, y1-y0)
#------------------------------------------------------------------------------
# Initialization Functions
#------------------------------------------------------------------------------

def passwordInit(data):
	data.aboutText = data.windowTitle = "Kevin Wainczak's Password Collector"
	data.password = ".tie5roanl"
	#password used by professor maxion in his research
	data.startScreen = False
	data.prepScreen = False
	data.startTrials = False
	data.practice = False
	data.selectedKeyboard = None
	data.incorrect = False
	startScreenInit(data)

def startScreenInit(data):
	data.startScreen = not(data.startScreen)
	data.startScreenText = "Password Collector\nSelect Your Keyboard"
	data.kBOneColor = "firebrick"
	data.kBTwoColor = "midnight blue"
	data.kBTextColor = "white"
	data.kBOneText = "Keyboard One"
	data.kBTwoText = "Keyboard Two"

def prepScreenInit(data):
	data.startScreen,data.prepScreen = not(data.startScreen),not(data.practice)
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
	data.prepScreen, data.practice = not(data.prepScreen), not(data.practice)
	data.typedLetters = ""
	data.pressedLetters = ""
	data.notTyped = data.password
	data.typedColor = "green"
	data.pressedColor = "gold2"
	data.notTypedColor = "black"

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
	if data.prepScreen:
		drawPrep(canvas, data)
	if data.practice:
		drawPractice(canvas, data)

def drawStart(canvas, data):
	margin = 5
	#text for start screen
	canvas.create_text(data.width/2, data.height/4, text =data.startScreenText,
					   fill = "black", 										font = "Arial " + str(data.width/25) +" bold")
	font = "Arial " +str(data.width/35) + " bold"
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

def drawPrep(canvas, data):
	margin = 5
	canvas.create_text(data.width/4, data.height/2, text = data.prepScreenText,
					  fill = "black",										font = "Arial " + str(data.width/35) +" bold")
	text = "START"
	font = "Arial " + str(data.width/35) + " bold"
	textWidth, textHeight = textSize(canvas, text, font)
	print textWidth, textHeight
	left = data.width/2
	top = data.height/10
	canvas.create_rectangle(left - margin, top - margin, 										left + textWidth + margin, 											top + textHeight + margin, fill = "lime green", 					outline = "green", width = 3)
	canvas.create_text(left, top, text = text, anchor = NW, fill = "white",				   font = font)

def drawPractice(canvas, data):
	if data.typedLetters == "": text = "Begin Typing"
	else: text = ""
	canvas.create_text(data.width/2, data.height/5, text = text, 						   fill = "black", 													   font = "Arial " + str(data.width/35) + " bold")
	left = data.width/4
	top = data.height/2
	font = "Arial " + str(data.width/10) + " bold"
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


#------------------------------------------------------------------------------
# Mouse Related Functions
#------------------------------------------------------------------------------

def clicked(event, data):
	if data.startScreen:
		checkStartClick(event, data)
	if data.prepScreen:
		checkPrepClick(event, data)

def checkStartClick(event, data):
	margin = 5
	left = data.width/5 - margin 
	top = 3*data.height/5 - margin 
	right = left + 234 + margin
	bottom = top + 39 + margin 
	if left <= event.x <= right and top <= event.y <= bottom:
		data.selectedKeyboard = "Keyboard One"
		prepScreenInit(data)
	left = 3*left - margin 
	right = left + 234 + margin 
	if left <= event.x <= right and top <= event.y <= bottom:
		data.selectedKeyboard = "Keyboard Two"
		prepScreenInit(data)

def checkPrepClick(event, data):
	margin = 5
	left = data.width/2 - margin
	top = data.height/10 - margin
	right = left + 115 + margin
	bottom = top + 39 + margin
	if left <= event.x <= right and top <= event.y <= bottom:
		practiceInit(data)

#------------------------------------------------------------------------------
# "Button" Functions
#------------------------------------------------------------------------------

def keyboardOneSelected(data):
	data.selectedKeyboard = "Keyboard One"
	prepScreenInit(data)

def keyboardTwoSelected(data):
	data.selectedKeyboard = "Keyboard Two"
	prepScreenInit(data)

#------------------------------------------------------------------------------
# Keyboard Related Functions
#------------------------------------------------------------------------------

def keyDown(event, data):
	if data.practice:
		if event.keysym == "period":
			event.keysym = "."
		data.pressedLetters += event.keysym
		data.notTyped = data.notTyped[1:]
		checkLegality(event, data)

def keyUp(event, data):
	if data.practice:
		if event.keysym == "period":
			event.keysym = "."
		data.pressedLetters = data.pressedLetters[1:]
		data.typedLetters += event.keysym
		checkLegality(event,data)

#------------------------------------------------------------------------------
# Legality Functions
#------------------------------------------------------------------------------

def checkLegality(event, data):
	if event.keysym not in data.password:
		data.typedLetters = ""
		data.notTyped = data.password
	if data.typedLetters == data.password:
		data.typedLetters = ""
		data.notTyped = data.password
	if not(data.password.startswith(data.pressedLetters)):
		data.typedLetters = ""
		data.notTyped = data.password

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







