
## Overview and Goals
In this project we will be working on a pdf reader in order to help create a calendar or scheduler type of tool to aid in understanding event times or deadlines easier for users. The goal of this project is to make it easier for users to view upcoming events and know what is due on their schedule without having to worry about going through their bags in an attempt to find a packet they likely already lost.  The goal of this project is to enable users to have an easier time looking at their schedules based on what was put on a syllabus, schedule, or otherwise. It aims to put all details of what is required to be done before class and not just assignments due. For example some teachers like to put their reading assignments or practice assignments on the syllabus or hidden somewhere within canvas but won’t put it on the main calendar just the assignments needed to be turned in. With this automatized system we’d be able to create an easy schedule for users to look at and get everything they need to know for a specific class. 
## Design and Implementation Strategy
For the project potentially the best way to approach going about it would be to create a website for this rather than creating an app for it. Typically managment will put up their syllabus or business calander on a website like canvas or they’ll email it to you for you to download; coaches will send out practice/game schedules via email and pdf documentation; your boss may email you a pdf of upcoming meetings, trips, etc. Rather than trying to take a picture and get an app to read it for you. We’ll make it easier with a pdf reader that takes in the physical copy of a pdf from a file uploaded by the user.
There will also be a “general use” feature where users can add a specific event exactly as they would in a regular calendar app. 

## APIs/Interfaces Between Components
- We will be using a variety of APIs to decrease the amount of time we set for the front end and focus more on the backend and creating the AI that would handle the main function of our website. To do this, we plan on using the Google API that already has built in functions to create and set deadlines. The data will be determined by our AI software that would then be sent to the front-end for user confirmation; when confirmed the information would then be sent to the Google API interface and added to the calendar object that was created. In order to retrieve the data and display it on a calendar for the user, the software will call for the list of deadlines that match the calendar ID and display it. 
Users will also be able to drag and drop their assignments/events/meetings/etc and our site will automatically update the assignment to its new date. 
- Another API we are choosing to use is BootStrap to help increase productivity therefore giving us more time to put into building our AI. Using the API does not necessarily utilize data the way the Google API does, the data is used for the front-end part of our website. The data will determine where a tab should be placed on the calendar board and determine the design characteristics it will display. An example would be the color of the table, whether it is complete, or how many days left until the deadline.
- Bootstrap will also be the tool we use to do the drag and drop feature of our site.
## Data Storage
By using Google API, all the data surrounding the dates and deadlines will be stored in Google servers. Each user will have a map with all the assignment names as keys and deadlines as the value as well as their log-in information (Username, password, recovery email). This means that only a small amount of data will be stored in our databases which we will choose based on efficiency and security. There are various Authentication API’s that help for security when creating and login into our website. If we choose to go through a less secure way, we can store login information into a relational database system and use PostgreSQL to get and put data for login in.  
## Testing Plan
1. The first phase of testing should consist of just checking functions to make sure that the code can recognize dates and implement them and any information onto the scheduler. We need to be able to know that the pdf reader will only read the dates up until it recognizes another date. The pdf reader also needs to be able to separate different forms of dates such as “12/1/22” versus “December 1st 2022” . We need to be able to test it with different forms for all cases. It needs to be able to recognize in cases like the 2nd one that “December” and the “1st” isn’t part of an assignment due. Then after these dates we need to ensure that any assignment can be put on the scheduler based on any text put after or below a date before the pdf reader can read a second date. 
2. Next with our next phase in testing we should be able to use a similar pdf to the first however we should add loads   of standard information before we read the due dates of the syllabus just to make sure that the scheduler will mainly ignore that information as it becomes unnecessary. 
3. Once we have a format that has been tested until it works well: 
Change the formatting as much as possible to help ensure that any style of pdf information can be interpreted by our AI
## Alternative Designs
We thought about designing an app that would not require a log in, however because most syllabi are downloaded to students' computers instead of phones, we opted to create a website so the uploading process of files is easier for users.
Instead of creating one calendar that is fixed (aka having to create a whole new calendar when a date is moved) we decided to have an interactive calendar when, in editing mode, allows users to drag and drop assignments, class times, and office hours to its new location. 
Each class is toggleable. Meaning that users can select a whole class on and off, and if a class is toggled, users can more specifically toggle if they want to view office hours, assignments, or class time.
We also are adding the ability to keep track of grades on assignments AND the weights of each course’s assignments. This way as students complete assignments they will be prompted to enter their grade if they choose to, we will keep track of their overall grades.
Initially: This calendar was only geared towards students. We have abstracted from our original design so that our AI (should) be able to read any schedule and format all wanted information into an interactive calendar. 
## Technical Dependencies
We will have to have a login system, but no third party user authentication. We will have to use a data service to store log-in information, passwords, and calendars associated with each user. We are planning to use the Rhodes database storage to achieve login information and passwords, while the calendars would be stored in google servers. 
Each account will be linked to an email in which we can send password resets, complete calendar pdfs, notifications, etc.
## Project Risks (from a technical standpoint).
The biggest risk we can see occurring is errors when it comes to reading through the pdf, the idea of looking through a pdf, and how to distinguish assignments reliably from each other, where to put something on your scheduler, keeping the scheduler accurate. For example, let's say the teacher decides to put an unimportant date for whatever reason in the middle of the pdf then we don’t want it to be reading that specific date and putting random info about things that just aren’t important to the class in the scheduler. 
Another thing that could occur would be providing too much information when it comes to a date. For example, if a reading was due on a certain day in the syllabus yet the professor likes to put down an entire bibliography citation of that reading down rather than a simple name and author. Then we are getting a large amount of unneeded info which would cause someone reading the schedule to feel as though they have more work than they need to or potentially miss an important detail caught up in unnecessary details. 
## Timeline 
For the first two weeks of the spring semester we would be planning out schedules for when groupmates are available and deciding on a time to meet. 
Because we have two group members who are waiting to hear back with athletic schedules we do not have a concrete meeting plan installed yet.
Our first focus will be coding an AI that can reliably read multiple date formats and creates an internal list of the assignments for each class.
Syllabi:
Class 1:
Assignments 
Class Times
Office Hours
Class 2:
Assignments 
Class Times
Office Hours
Class 3:
Assignments 
Class Times
Office Hours
Class 4:
Assignments 
Class Times
Office Hours
Sports Calendar:
Team (Lacrosse):
Practice:
Games:
Work Meetings
Meeting (With time/location)
Description
Our second focus will be implementing the AI into the website and testing to ensure that all outputs are as expected and that the AI is prompting the user to:
Check that the information it has read from the documentation is correct and as the user desired.
Confirm dates / repeated class times
Prompting the user about notifications (if the user wishes to have notifications sent to their email)
Users can select which of the togglable tabs they wish to get notifications for as well as customizing when they receive notifications and what they say.








