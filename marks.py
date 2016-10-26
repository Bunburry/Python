from graphics import *

#opening file as numbers

numbers = []

with open("marks.txt") as f:
	for line in f:
		data = line.split()
		numbers.append(int(data[0]))
		
window = GraphWin("Visualisation", 300, 300)

list = []
for i in numbers:
	
	if (i >= 40 and i <= 50):
		list.append(int(i))
		x = len(list)
		print x
		y = 0
		counter = 0
		while(y < x):
			counter = counter + 0.5	
			#rec = Rectangle(Point(20*counter,10*counter),Point(10*counter,20*counter))
			rec = Rectangle(Point(20,10),Point(10,20))
			rec.move(50*counter,0)
			rec.setOutline(color_rgb(255, 0, 0))
			rec.setFill(color_rgb(255, 0, 0))
			rec.draw(window)
			y = y + 1
		
	elif (i>50 and i<=60):
		x = len(list)
		y = 0
		counter = 0
		while(y < x):
			counter = counter + 0.5
			rec = Rectangle(Point(20,10),Point(10,20))
			rec.move(50*counter,20)
			rec.setOutline(color_rgb(255, 102, 0))
			rec.setFill(color_rgb(255, 102, 0))
			rec.draw(window)
			y = y + 1
			
	elif (i>60 and i<=70):
		x = len(list)
		y = 0
		counter = 0
		while(y < x):
			counter = counter + 0.5
			rec = Rectangle(Point(20,10),Point(10,20))
			rec.move(50*counter,40)
			rec.setOutline(color_rgb(255, 255, 77))
			rec.setFill(color_rgb(255, 255, 77))
			rec.draw(window)
			y = y + 1
			
	elif (i>70 and i<=80):
		x = len(list)
		y = 0
		counter = 0
		while(y < x):
			counter = counter + 0.5
			tria = Polygon(Point(10,20),Point(30,40),Point(10,60))
			tria.setOutline(color_rgb(77, 255, 77))
			tria.setFill(color_rgb(77, 255, 77))
			tria.move(50*counter,60)
			tria.draw(window)
			y = y + 1

window.getMouse()


