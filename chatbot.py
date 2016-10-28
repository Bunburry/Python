import random
import urllib2, urllib


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
	if i in stopwords or i in ["good","great","not bad","very well"]:
		print("I'm pleased to hear that!")
	elif i in stopwords or i in ["bad","not well","terribly","terrible"]:
		print("Hang in there, " + elem + ". Things will work out.")
	else:
		print("Do you want to hear a joke?")
		joke = raw_input()
		if joke.lower() in ["yes","sure","of course","yeah"]:
			print("How many programmers does it take to change a light bulb? \nNone. It's a hardware problem.")
		elif joke.lower() in ["no","not really","nope"]:
			print("Why so serious?")

while True:
	phrase = raw_input()
	
	phrase = urllib.quote(phrase)
	blah = urllib2.urlopen("http://en.wikipedia.org/wiki/" + "".join(phrase))
	html = blah.read()
	start = html.find("<p>")
	end = html.find("</p>")
	for j in phrase:
		if j in stopwords:
			pass
		else:
			print("Are you talking about " + html[start:end])

while True:
	phrase = raw_input()
	phrase = phrase.lower()
	if "" in phrase:
		if "what" in phrase and "name" in phrase:
			print ("I haven't got a name. Give me one.")
			bot = raw_input()
			bot2 = bot.split()
			for x in bot2:
				if x in stopwords:
					pass
				else:
					print ("My name is " + x)
		elif "old" in phrase:
			print ("I'm two weeks old")
		elif "how" in phrase and "you" in phrase:
			print ("I'm very well, thank you")
		elif "lol" in phrase:
			print ("*laughs in robot*")
		elif "nice" in phrase and "you" in phrase:
			print ("The pleasure is mine")
		elif "bye" in phrase:
			goodbye = ["Adios","See you soon","Goodbye","Hasta la vista"]
			print (random.choice(goodbye))
		elif "dunno" in phrase or "ok" in phrase:
			print ("k k k")
		else:
			something = ["Code harder","I can't understand you","*sobs*"]
			print (random.choice(something))
			



