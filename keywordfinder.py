from pypdf import PdfReader
import re 
#from datetime import datetime


date_pattern = "\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?"
date_pattern3 = "(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s*[0-9]{1,2}(?:th|st|nd|rd)?\s*,?\s*(?:[0-9]{2,4})?"

myset = {date_pattern, date_pattern3}
days = "Monday|Mon|Tuesday|Tue|Tues|Wednesday|Wed|Thursday|Thur|Thurs|Friday|Fri|Saturday|Sat|Sunday|Sun"
simpledays = "MWF|TR|TTh|TT|MW|WF"
returningDates = []
month_dict = {'Jan': '01','January': '01','Feb': '02','February': '02','Mar': '03','March': '03','Apr': '04','April': '04','May': '05','Jun': '06','June': '06','Jul': '07','July': '07','Aug': '08','August': '08','Sep': '09','September': '09', 'Sept': '09', 'Oct': '10','October': '10','Nov': '11','November': '11','Dec': '12','December': '12'}




def findclasstimes(line):
    timepattern = "((1[0-2]|0?[1-9])\:([0-5][0-9])\s*?([AaPp][Mm])?)"
    match = re.search(timepattern, line)
    if match:
        print(re.findall(timepattern, line))
        print("Match found!") 
        print(line)
    
def extract_office_hours(text):
    match1 = re.search(r"[Oo]ffice\s[Hh]ours", text)
    if match1:
        print(text)
        office_hours_regex = re.compile(f"({days})[.]*[\s-]*(and|to)?[\s-]*({days})?")
        match = office_hours_regex.search(text)
        timepattern ="((1[0-2]|0?[1-9]):([0-5][0-9])\s*?([AaPp][Mm])?)"
        
        matchtime = re.search(timepattern, text)
        if match:
            print(match.group())
            #return match.group()
        if matchtime:
            print(re.findall(timepattern, text))

  
def testre():

    #re.match(date_pattern, '12/12/2022') # Returns Match object
    #print(re.findall(date_pattern, 'I\'m on vacation from 1/18/2021 till 1/29/2021'))
    #print(re.findall(date_pattern3, ' * February 16, 2023  – First Essay Due  '))
    print(re.findall(date_pattern, 'youre 10-12 and 1/20 and 2.19'))
    print(re.findall(date_pattern, 'youre 10-12-2012 and 1/20/2022 and 2.19.2022'))
    x = re.findall(date_pattern, 'youre 10-12-2012 and 1/20/2022 and 2.19.2022')[0]
    print(createEvent(x, ["",""], date_pattern))
    
def createEvent(date,currevent, currset):
    date_array = date.replace(",", " ").replace("/", " ").replace("-", " ").replace(".", " ").split(" ")
    #print(date_array)
    while "" in date_array:
        date_array.remove("")
    if currset == date_pattern3:
        date_array[0] = month_dict[date_array[0]] 
    event = "2023"
    if int(date_array[0]) > 12 or int(date_array[1]) > 32:
        return 
    for i in range(2):
        if len(date_array[i]) == 1:
            date_array[i] = "0"+date_array[i]
        event += "-"+date_array[i]
    currevent[0] = event
    return currevent

def test(alldates):
    return 0
            

def generateevents(pdf):
    alldates = []
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    Haveevent = False
    onlyevent = ""
    currevent = ["", ""]
    Newevent = ["", ""]
    events = []
    

    for i in range(number_of_pages):
        
        page = reader.pages[i]
        text = page.extract_text()

        pattern = r'\d+ \d+'
        text = re.sub(pattern, lambda match: match.group().replace(' ', ''), text)
        text_split = text.splitlines()
        #print(text)
        
        for x in text_split:
            #extract_office_hours(x)
            firstline = False
            for y in myset: 
                if len(re.findall(y,x)) != 0:
                    if Newevent != None and Newevent != ["", ""]:
                            events.append(Newevent)
                    currevent = ["", ""]              
                    alldates.append(re.findall(y,x)[0])
                    onlyevent = x
                    onlyevent = onlyevent.replace(re.findall(y,x)[0], "")
                    currevent[1] = onlyevent
                    #print(currevent)
                    #print(onlyevent)
                    firstline = True
                    Haveevent = True
                    Newevent = createEvent(re.findall(y,x)[0],currevent, y)
                    

            if firstline != True and Haveevent == True and Newevent != None:
                    Newevent[1] += x
                     

    events.append(Newevent)
    for i in events:
        print(i)
    return events
            

    #print(alldates)


#testre()

