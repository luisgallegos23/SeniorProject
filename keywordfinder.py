from pypdf import PdfReader 
import re 
from datetime import datetime


date_pattern = "[0-9]{1,2}\\S[0-9]{1,2}\\S[0-9]{2,4}"
date_pattern2 = "[0-9]{1,2}\\/[0-9]{1,2}"
date_pattern3 = "(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\\s*[0-9]{1,2}(?:th|st|nd|rd)?\\s*,\s*[0-9]{2,4}"
myset = {date_pattern, date_pattern2, date_pattern3}
days = "Monday|Mon|Tuesday|Tue|Tues|Wednesday|Wed|Thursday|Thur|Thurs|Friday|Fri|Saturday|Sat|Sunday|Sun"
simpledays = "MWF|TR|TTh|TT|MW|WF"




def findclasstimes(line):
    timepattern = "((1[0-2]|0?[1-9]):([0-5][0-9])\s*?([AaPp][Mm])?)"
    match1 = re.search(r"[Oo]ffice\s[Hh]ours", line)
    match = re.search(timepattern, line)
    if match:
        print(re.findall(timepattern, line))
        print("Match found!") 
        print(line)
    
def extract_office_hours(text):
    office_hours_regex = re.compile(f"({days})[.]*[\s-]*(and|to)?[\s-]*({days})?")
    match = office_hours_regex.search(text)
    if match:
        return match.group()    

  
def testre():

    re.match(date_pattern, '12/12/2022') # Returns Match object
    print(re.findall(date_pattern, 'I\'m on vacation from 1/18/2021 till 1/29/2021'))
    print(re.findall(date_pattern3, ' * February 16, 2023  – First Essay Due  '))
    print(re.findall(date_pattern, 'youre 10-12-2012 and 1/20/2012 and 2.19.2022'))
    
def createEvent(date,currevent):
    
    date_array = date.replace(",", " ").split(" ")
    while "" in date_array:
        date_array.remove("")
    for i in range(3):
        currevent[i] = date_array[i]
    print(currevent)

def main():
    alldates = []
    dandEvents = []
    reader = PdfReader("music.pdf")
    number_of_pages = len(reader.pages)
    
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        text_split = text.splitlines()
        
        for x in text_split:
            #findclasstimes(x)
            for y in myset:
                match = re.search(y, x)
                #if match:
                currevent = ["", "", "", ""]
                if len(re.findall(y,x)) != 0:
                    alldates.append(re.findall(y,x)[0])
                    onlyevent = x
                    onlyevent = onlyevent.replace(re.findall(y,x)[0], "")
                    currevent[3] = onlyevent
                    #print(currevent)
                    #print(onlyevent)
                    createEvent(re.findall(y,x)[0],currevent)
    
        
    

main()
