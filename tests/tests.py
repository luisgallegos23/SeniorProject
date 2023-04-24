import unittest
from src import DBhandle
from src import CalHandle

## Clear Database before testing
## Comment out line in DBhandle.py marked w/ "Mark for test"

email = "luisgallegos201@yahoo.com"
unittest.TestLoader.sortTestMethodsUsing = None

class TestWebFunctions(unittest.TestCase):

#Checks addUser() and checkUser()    
    def testAddUser(self):
        self.assertEqual(DBhandle.checkUser(email,"LuisGallegos"),False)
        DBhandle.addUser(email,"LuisGallegos", "Luis", "Gallegos")
        self.assertEqual(DBhandle.checkUser(email,"LuisGallegos"),True)

#Checks buildService(), existCreds(), and addCreds()   
    def addCreds(self):
        self.assertEqual(DBhandle.existCreds(email, False))
        CalHandle.buildService(email)
        self.assertEqual(DBhandle.existCreds(email, True))

#Checks creatCalendar(), addCalendar(), getCalendar(), getCal()   
    def testCreateCalendar(self):
        self.assertEqual(DBhandle.existCal(email, "test calendar"), False)
        CalHandle.createCalendar(email,"test calendar")
        self.assertEqual(DBhandle.existCal(email, "test calendar"), True)
        self.assertEqual(CalHandle.getCal(email, "test calendar")['summary'],"test calendar")

#checks creatEvent(), formateEvent(), getCalendar(), getEvents()
    def testCreateEvents(self):
        CalHandle.createEvent(email,"test calendar", "test 1", "2023-05-01T09:00:00-07:00","2023-05-01T17:00:00-07:00")
        CalHandle.createEvent(email,"test calendar", "test 2", "2023-05-12T09:00:00-07:00","2023-05-12T17:00:00-07:00")
        CalHandle.createEvent(email,"test calendar", "test 3", "2023-06-01T09:00:00-07:00","2023-06-01T17:00:00-07:00")
        CalHandle.createEvent(email,"test calendar", "test 4", "2023-06-27T09:00:00-07:00","2023-06-27T17:00:00-07:00")
        CalHandle.createEvent(email,"test calendar", "test 5", "2023-08-16T09:00:00-07:00","2023-08-16T17:00:00-07:00")
        calid = DBhandle.getCalendar(email,"test calendar")
        data = CalHandle.getEvents(calid, email)
        print(data)

if __name__ == '__main__':
    unittest.main()