from turtle import *

speed("fastest")
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

with open('Robin-Hood.txt', 'r') as book:
	data = book.read().replace('\n', ' ')

	finder = data.split()
 
	counter = 0 
	for x in range(len(finder) - 1):
		
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

switch = 0
squareCount = 12

for x in colors:
	square(x)
	switch += 1
	
	if switch == squareCount:
		switch = 0
		left(180)
		color("white")
		forward(side * squareCount)
		left(90)
		forward(side)
		left(90)

while True:
	color("white")
	forward(side * squareCount)