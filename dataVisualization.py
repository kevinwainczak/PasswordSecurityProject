# Kevin Wainczak
# kwaincza + Section J
# Term Project: Data Visualization

from Tkinter import *
import eventBasedAnimation
import csv

# Taken from 15-112 Homework # 1
def almostEqual(d1, d2, epsilon=10**-4):
    return abs(d1 - d2) < epsilon

# Taken from 15-112 Homework # 9
def flatten(a):
	flattenedList = [ ]
	#base case
	if type(a) != list: return a
	#if the type isn't a list, return it, need this for ints
	for item in a:
		#iteratively go through list
		#otherwise a is a list, go inside of it and 
		if type(item) != list:
			flattenedList += [item]
		else:
			flattenedList += flatten(item)
			#recursively go inside and flatten
	return flattenedList

class DataPoint(object):
	def __init__(self, count, color, upDown, time, margin, maxValue, 				 width, height, rows, char):
		self.color = color
		self.char = char
		self. r = 3
		self.upDown = upDown
		if upDown == 0:
			self.fill = color
		else:
			self.fill = None
		self.xValue = 1.0*((time / maxValue) * (width - 2 * margin)) + margin
		self.yValue = margin + ((height - (2* margin)) / rows) * count

	def draw(self, canvas):
		x = self.xValue
		y = self.yValue
		fill = self.fill
		r = self.r
		outline = self.color
		canvas.create_oval(x-r, y-r, x+r, y+r, fill = fill, outline = outline,				 width = 1)

	#Taken from OOP Smileys example in 15-112
	def contains(self, x, y):
		return ((self.xValue - x)**2 + (self.yValue - y)**2 <= self.r**2)

def visualizeInit(data):
	data.aboutText = data.windowTitle= "Data Visualizer - Press 'b' to go back"
	profiledUsersList = open('profiledUsers.csv', 'rU')
	for row in profiledUsersList:
		data.profiledUsers = row.split(",")
	data.chooseUserScreen = True

def dataGraphInit(data, rows = 100):
	data.chooseUserScreen = False
	data.margin = 15
	possibleFiles = ['kevinTimes.csv', 'anmolTimes.csv', 'bryantTimes.csv',			  'chrisTimes.csv', 'micahTimes.csv', 'myaTimes.csv', 					 'tylerTimes.csv']
	personFile = "%sTimes.csv" % data.person
	data.password = ".tie5roanl"
	data.colorList = ["navy", "red", "dark violet", "dark green", 				  		  "DeepPink2", "navy", "red", "dark violet", 					  	  "dark green", "black"]
	data.personTimeList = grabData(data, personFile)
	data.rowsDisplayed = rows
	data.displayGraph = True
	dataPointsInit(data)

def grabData(data, timingData):
	personTimeList = [ ]
	with open(timingData, 'rU') as csvfile:
		timeList = csv.reader(csvfile, delimiter=' ', quotechar = '|')
		for row in timeList:
			if row[0] == ".": continue
			for char in row:
				tempList = char.split(',')
				holdList = [ ]
				for val in tempList:
					holdList.append(float(val))
				personTimeList.append(holdList)
	personTimeList = manipulateData(data, personTimeList)
	return personTimeList

def manipulateData(data, personTimeList):
	reducedList = [ ]
	# This is the order the data is represented in from our .csv files we are pulling to get data from
	data.cats = "..55aaeeiilnnoorrtt"
	data.maxValue = max(flatten(personTimeList))
	for passwordInput in personTimeList:
		for i in xrange(len(passwordInput)):
			if i < 19:
				if (i <= 10 and i % 2 == 0) or (i > 10 and i % 2 == 1):
					y = 0
				else:
					y = 1
				passwordInput[i] = (data.cats[i],y,passwordInput[i])
			else:
				passwordInput.pop(19)
	return personTimeList 

def dataPointsInit(data):
	data.dataPoints = [ ]
	count = -1
	while count <= data.rowsDisplayed:
		for passwordInput in data.personTimeList:
			count += 1
			for dataPoint in passwordInput:
				char = dataPoint[0]
				colorIndex = data.password.index(dataPoint[0])
				color = data.colorList[colorIndex]
				upDown = dataPoint[1]
				time = dataPoint[2]
				if almostEqual(time, 0):
					time = 0
				dataPoint = DataPoint(count, color, upDown, time, data.margin, 					  data.maxValue, data.width, data.height, 					  data.rowsDisplayed, char)
				data.dataPoints.append(dataPoint)

def displayData(canvas, data):
	if data.chooseUserScreen:
		for user in xrange(len(data.profiledUsers)):
			if user % 2 == 0: color = "blue"
			else: color = "red"
			left = 5
			right = 500
			top = (data.height/len(data.profiledUsers))*user
			bottom = top + (data.height/len(data.profiledUsers))
			text = data.profiledUsers[user]
			font = "Arial " + str(data.height/(len(data.profiledUsers)+10)) 				+ " bold"
			canvas.create_rectangle(left, top, right, bottom, fill = color)
			canvas.create_text(left, top, text = text, anchor = NW, 					   fill = "white", font = font)
	else:	
		for line in xrange(data.rowsDisplayed):
			y0 = data.margin + ((data.height - 2 * data.margin) / data.rowsDisplayed) * line
			x0 = data.margin
			x1 = data.width - data.margin
			y1 = y0
			color = "black"
			canvas.create_line(x0,y0,x1,y1, fill = color, width = 1 )
		count = 0
		for dataPoint in data.dataPoints:
			if count <= (len(data.cats)*data.rowsDisplayed - 1):
				dataPoint.draw(canvas)
				count += 1

def clicked(event, data):
	if data.chooseUserScreen:
		left = 5
		right = 200
		if left <= event.x <= right:
			for user in xrange(len(data.profiledUsers)):
				top = (data.height/len(data.profiledUsers)) * user
				bottom = top + data.height/len(data.profiledUsers)
				if top <= event.y <= bottom:
					data.person = data.profiledUsers[user]
					dataGraphInit(data)	
	else:	
		for dataPoint in data.dataPoints:
			if dataPoint.contains(event.x, event.y):
				x = dataPoint.xValue
				char = dataPoint.char
				upDown = dataPoint.upDown
				for point in data.dataPoints:
					if point.char == char and point.upDown == upDown:
						dx = x - point.xValue
						point.xValue = x
						for dot in data.dataPoints:
							if dot != point and dot.yValue == point.yValue:
								dot.xValue += dx

def keyPressed(event, data):
	if event.keysym == "Up":
		if data.rowsDisplayed <= len(data.personTimeList):
			data.rowsDisplayed += 1
		dataGraphInit(data, data.rowsDisplayed)
	elif event.keysym == "Down":
		if data.rowsDisplayed >= 1:
			data.rowsDisplayed -= 1
		dataGraphInit(data, data.rowsDisplayed)
	elif event.keysym == 'b':
		visualizeInit(data)

eventBasedAnimation.run(
	width = 1200,
	height = 650,
	initFn = visualizeInit,
	drawFn = displayData,
	mouseFn = clicked,
	keyFn = keyPressed)


