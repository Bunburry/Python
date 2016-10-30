import twitter
import sqlite3
import urllib2
import shutil

file = open("secret_keys.txt")
keys = file.read().split('\n')

api = twitter.Api(keys[0],keys[1],keys[2],keys[3])
#\\ ant windowsu

shutil.copyfile('/Users/ggruzinskaite/Library/Application Support/Google/Chrome/Default/History','History')

History = ('History')

console = sqlite3.connect('History')
cursor = console.cursor()
cursor.execute("SELECT * FROM urls")
rows = cursor.fetchall()
for row in rows: 
    urls = row[2] #patalpina i masyva
new = urls.split('\n') #perskaito kiekviena eilute
print new[-1] #paima paskutini

message = ["I like ","I mostly view ","Today I read "]
response = api.PostUpdate(random.choice(message) + new[-1])
print(response.text)
