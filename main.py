from turtle import *
from math   import sqrt

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


# The list of colors. I left you a longer list, but I'll let you implement it
possible_colors = ["RED", "BLUE", "YELLOW", "GREEN", "PURPLE", "ORANGE", "WHITE", "BLACK", "GREY", "GRAY", "INDIGO"]
colors = []

with open(raw_input("Drop File Here\n> "), 'r') as book:
	data = book.read().replace('\n', ' ')

	finder = data.split()
 
	
	# For every word in the finder...
	for word in finder:
		
		# If the word is in our list of colors...	
		if word.upper() in possible_colors:
			# Add it to the list
			colors.append(word)

# counts to squareCount. When it reaches that threshhold the graph skips to a new line
switch = 0

# How many squares in a row
squareCount = int(sqrt(len(colors)))

#length of side
side = 20

# Turtle gotta go FAST
speed("fastest")
color("white")

# Center the square on screen
goto(-(squareCount/2)*side, (squareCount/2)*side)

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

# Keep alive
mainloop()