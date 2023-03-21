import sys
sys.path.insert(0,'/Users/luisgallegos/Desktop/Programming-Projects/SeniorProject/src') #will have to be updated once out

import eventML
import unittest


class TestEventRecognition(unittest.TestCase):

    def test_createDictionary(self):
        eventML.makeDict()
        self.assertEqual(eventML.getEventBoolean('Homework 2'),True)
        self.assertEqual(eventML.getEventBoolean('Lab 1'), True)
        self.assertEqual(eventML.getEventBoolean('Project 2'), True)
        self.assertEqual(eventML.getEventBoolean('Final Exam 2'), True)
        self.assertEqual(eventML.getEventBoolean('DC Writes! A Petworth Writers Workshop'), True)
        self.assertEqual(eventML.getEventBoolean('Family Story Time'), True)
        self.assertEqual(eventML.getEventBoolean('Legos After Lunch'), True)
        self.assertEqual(eventML.getEventBoolean('Written Assignment #2 due'), True)


        self.assertEqual(eventML.getEventBoolean('There is no cat swinging on a fan'),False)
        self.assertEqual(eventML.getEventBoolean('Hello There'),False)
        self.assertEqual(eventML.getEventBoolean('A man is moving gracefully'),False)
        self.assertEqual(eventML.getEventBoolean('You should read the following sections from the paper'),False)
        ##self.assertEqual(eventML.getEventBoolean('Define and describe a variety of parallel computer architectures and discuss '),False)
        ##self.assertEqual(eventML.getEventBoolean('Voting is the fundamental practice of democratic politi'),False)
        ##self.assertEqual(eventML.getEventBoolean(' There is a reflexive aspect to this course as it offers you the opportun'),False)
        self.assertEqual(eventML.getEventBoolean('Course Objectives and Expectations:'),False)

if __name__ == '__main__':
    unittest.main()