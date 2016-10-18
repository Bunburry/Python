import random
with open("stopwords.txt") as myfile:
	list = myfile.split()
hello = ["Hi there","Welcome","Hey","Hello there","Hello"]
print(random.choice(hello))
response = raw_input()
greeting = ["How are you doing?","How is life?","What's going on?","How's your day going?"]
name = raw_input("What is your name? ")
print("Nice to meet you " + name + "\n" + random.choice(greeting))
#print("Hello " + response + "\nHow are you feeling today?")

answer = raw_input()
if answer in ["good","Good","Great","great","not bad","Not bad","very well","Very well"]:
	print("I'm pleased to hear that!")
elif answer in ["bad","Bad","not well","Not well"]:
	print("Hang in there, " + name + ". Things will work out.")
	
print("Do you want to hear a joke?")
joke = raw_input()
if joke in ["Yes","yes","Sure","sure","Of course","of course","yeah","Yeah"]:
	print("How many programmers does it take to change a light bulb? \nNone. It's a hardware problem.")
elif joke in ["No","no","Not really","not really","Nope","nope"]



