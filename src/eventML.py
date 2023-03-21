
import math
import re 

EventDictionary = {}
NotEventDictionary = {}
sizeDict = 0 #Number of words in EventDictionary
sizeNDict = 0 #Number of words in NotEventDictionary
regex = re.compile('[,\/\.!?]');

"""
Creates two Dictionaries from training files 
"""
def makeDict():
    createEventDicitonary('/Users/luisgallegos/Desktop/Programming-Projects/SeniorProject/trainingfiles/eventtrainingset.csv')
    createNotDicitonary('/Users/luisgallegos/Desktop/Programming-Projects/SeniorProject/trainingfiles/noteventtraining.csv')

"""
Adds words to EventDictionary
Word are read form training file
Parameter: String (name of file)
Key = String Value=Integer (# of times word read) 
"""
def createEventDicitonary(filename):
    global sizeDict
    file = open(filename)
    for line in file:
        line = regex.sub('',line)
        line = line.rstrip()
        line = line.lower()
        wordarr = line.split(" ")
        for word in wordarr:
            if (EventDictionary.get(word,0) == 0):
                EventDictionary[word] = 1
                sizeDict += 1;
            else:
                val = EventDictionary.get(word)
                val += 1
                EventDictionary[word] = val

    file.close()    

"""
Adds words to NotEventDictionary
Words are read form training file
Parameter: String (name of file)
Key = String Value=Integer (# of times word used) 
"""
def createNotDicitonary(filename):
    global sizeNDict
    file = open(filename)
    for line in file:
        line = regex.sub('',line)
        line = line.rstrip()
        line = line.lower()
        wordarr = line.split(" ")
        for word in wordarr:
            if(NotEventDictionary.get(word,0) == 0):
                NotEventDictionary[word] = 1
                sizeNDict += 1;
            else:
                val = NotEventDictionary.get(word)
                val+=1
                NotEventDictionary[word] = val

    file.close() 


"""
Calculates the probability of string being an Event
Parameter: String

"""
def calcEventProb(line):
    x = sizeDict / (sizeDict + sizeNDict)
    eventprob = math.log(x)
    line = line.lower()
    line =  line.rstrip()
    wordarr = line.split(" ")
    for word in wordarr:
        #print("Word: %s Prob: %d " % (word, EventDictionary.get(word,0)))
        if(EventDictionary.get(word,0) != 0):
            value = EventDictionary.get(word) + 1 #smooths prob
            den = sizeDict + 2 #smooths
            eventprob += math.log(value/den)
        else:
            value = EventDictionary.get(word,0) + 1
            den = sizeDict + 2
            eventprob += math.log(1-(value/den))

    return eventprob

"""
Calculates the probability of string NOT being an Event
Parameter: String
"""
def notEventProb(line):
    x = sizeNDict / (sizeDict + sizeNDict)
    eventprob = math.log(x)
    line = line.lower()
    line =  line.rstrip()
    wordarr = line.split(" ")
    for word in wordarr:
        #print("Word: %s Prob: %d " % (word, NotEventDictionary.get(word,0)))
        if(NotEventDictionary.get(word,0) != 0):
            value = NotEventDictionary.get(word) + 1 #smooths prob
            den = sizeNDict + 2 #smooths
            eventprob += math.log(value/den)
        else:
            value = NotEventDictionary.get(word,0) + 1
            den = sizeNDict + 2
            eventprob += math.log(1-(value/den))
            
    return eventprob


"""
Returns TRUE or FALSE boolean
TRUE - String probability is an event
FALSE - String probability is not an event
Parameter: String
"""
def getEventBoolean(line):
    line = regex.sub('',line)
    print("Line: %s True: %.2f False: %.2f " % (line, calcEventProb(line), notEventProb(line)))
    if(calcEventProb(line) < notEventProb(line)):
        return True
    
    return False