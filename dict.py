import json
import difflib

print("Type the word troubling you: ")

def translate(w):
	with open('/home/rajas.shah/Downloads/data.json') as info:
		d=json.load(info)
	words=d.keys()
	
	matches=difflib.get_close_matches(w, words, 5)#will show 5 close matches for w from words

	if w in words:
	    print(d[w])
	else:
	    if len(matches)==0:
	        print("No matches were found. Please check your input.")
	    else:
	        print(matches)	       
	        w2=input("Please enter a match: ")
	        translate(w2) #this continues, to ensure user satisfaction    	
     
word = input("Enter word: ")
translate(word)








































































































































