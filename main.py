from turtle import *
from math   import sqrt

side = 20

def square(fillColor):
	color(fillColor)
	begin_fill();
	
	# Square
	forward(side)
	left(90)
	forward(side)
	left(90)
	forward(side)
	left(90)
	forward(side)
	left(90)
	
	# Fill square
	end_fill()
	forward(side)


colors = []

with open(raw_input("Drop File Here\n> "), 'r') as book:
	data = book.read().replace('\n', ' ')

	finder = data.split()
 
	counter = 0 
	
	for x in range(len(finder) - 1):
		# Listen for each color and if found add to an array	
		if finder[x] == "red" or finder[x] == "Red" or finder[x] == "red.":
			counter += 1
			colors.append("red")

		elif finder[x] == "blue" or finder[x] == "Blue" or finder[x] == "blue.":
			counter += 1
			colors.append("blue")

		elif finder[x] == "yellow" or finder[x] == "Yellow" or finder[x] == "yellow.":
			counter += 1
			colors.append("yellow")

		elif finder[x] == "green" or finder[x] == "Green" or finder[x] == "green.":
			counter += 1
			colors.append("green")

		elif finder[x] == "purple" or finder[x] == "Purple" or finder[x] == "purple.":
			counter += 1
			colors.append("purple")

		elif finder[x] == "orange" or finder[x] == "Orange" or finder[x] == "orange.":
			counter += 1
			colors.append("orange")

		elif finder[x] == "white" or finder[x] == "White" or finder[x] == "white.":
			counter += 1
			colors.append("white")

		elif finder[x] == "black" or finder[x] == "Black" or finder[x] == "black.":
			counter += 1
			colors.append("black")

		elif finder[x] == "grey" or finder[x] == "Grey" or finder[x] == "grey.":
			counter += 1
			colors.append("grey")

		elif finder[x] == "gray" or finder[x] == "Gray" or finder[x] == "gray.":
			counter += 1
			colors.append("gray")

		elif finder[x] == "indigo" or finder[x] == "Indigo" or finder[x] == "indigo":
			counter += 1
			colors.append("indigo")

# counts to squareCount. When it reaches that threshhold the graph skips to a new line
switch = 0
# How many squares in a row
squareCount = sqrt(len(colors))

speed("fastest")

for item in colors:
	# makes a square with the item in colors
	square(item)
	switch += 1
	
	# Code that skips to new line
	if switch == squareCount:
		switch = 0
		left(180)
		color("white")
		forward(side * squareCount)
		left(90)
		forward(side)
		left(90)

# Keeps the window open and "hides" the turtle
# Kinda sketchy but a wise man once said "sketchy is good"
# ctrl C is your best friend here
while True:
	color("white")
	forward(side * squareCount)