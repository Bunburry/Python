import random
stopwordsfile = open("stopwords.txt", "r")
stopwords = stopwordsfile.read().split('\n')
#for eachWord in stopwords:
	#print(eachWord)
	
hello = ["Hi there","Hola","Hey","Hello there","Hello"]
print(random.choice(hello))
response = raw_input()
greeting = ["How are you doing?","How is life?","How are you?","How's your day going?"]
name = raw_input("What is your name? ")
newname = name.split()
for elem in newname:
	if elem in stopwords:
		pass
	else:
		print ("Nice to meet you " + elem + "\n" + random.choice(greeting))


answer = raw_input()
answer2 = answer.split()
for i in answer2:
	if answer2 not in stopwords or answer2 in ["good","great","not bad","very well"]:
		print("I'm pleased to hear that!")
	elif answer2 in ["bad","not well"]:
		print("Hang in there, " + elem + ". Things will work out.")
#if answer.lower() in ["good","great","not bad","very well"]:
#	print("I'm pleased to hear that!")
#elif answer.lower() in ["bad","not well"]:
#	print("Hang in there, " + elem + ". Things will work out.")
	
print("Do you want to hear a joke?")
joke = raw_input()
if joke.lower() in ["yes","sure","of course","yeah"]:
	print("How many programmers does it take to change a light bulb? \nNone. It's a hardware problem.")
elif joke.lower() in ["no","not really","nope"]:
	print("Why so serious?")



