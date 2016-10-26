from graphics import *

#numbersfile = open("marks.txt", "r")
#numbers = numbersfile.read().split('\n')
numbers = []

#opening file as numbers

with open("marks.txt") as f:
	for line in f:
		data = line.split()
		numbers.append(int(data[0]))
		
window = GraphWin("Visualisation", 300, 300)

list = []
#x = float()
for i in numbers:
	
	if (i >= 40 and i <= 50):
		list.append(int(i))
		x = len(list)
		print x
		y = 0
		counter = 0
		while(y < x):
			counter = counter + 1
			rec = Rectangle(Point(20*counter,10*counter),Point(10*counter,20*counter))
			rec.setOutline(color_rgb(255, 124, 135))
			rec.setFill(color_rgb(255, 124, 135))
			rec.draw(window)
			y = y + 1
		
	elif (i>50 and i<=60):
		x = len(list)
		y = 0
		while(y < x):
			y = y + 1
		#tria = Polygon(Point(40,40,40),Point(40,40,40),Point(40,40,40))
		#tria.draw(window)
        

window.getMouse()


