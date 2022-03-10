# QA-DevOps-Fundamental-Project- Recruitment Agency Employee App:-
This repository includes all deliverables for the DevOps Fundamentals project

## Contents:

- Project Brief
- App Design
- CI Pipeline
- Risk Assessment
- Testing
- The App
- Updates
- Current Issues

## Project Brief:

The brief for this project stated that we were to build and design an web app usinf Flask, Python and SQL. The app must follow the CRUD criteria which means it has to Create, Read, Update and Delete information on the web app. The data that was being stored must be held in a minimum of 2 entity tables with at least a one to many relationship

## App Design:

The design I have chosen for my web app is a Recruitment Agency's Employee Database app. This app allows the user to add new employees and jobs to the system and then after employ that employee to a specifiied role(create functionality.) After each element is created they can be viwed all on the hompeage(read functionality.) If any data needs updating then with a click on the element that needs updating such as if an employee has been assigned to the wrong role or their personal details are incorrect(update functionality). If any element needs deleting then it can also be deleted(delete functionality). This fufills the CRUD functionality of the web app. 2 one to many relationships were made with the employment table being the join table. An ERD was made to show this.

![erd2](https://user-images.githubusercontent.com/99325859/157317506-1ca0fe9d-6bdc-45c3-aefb-638a32d7dc8b.png)

## CI Pipeline:

The Project aslo required a few of the CI pipeline stages being implemented. These were in the form of tracking, version control, development environment and build server. For tracking my project I used Trello for their tracking board. I created user stories and tasks which helped me track what I was currently doing, what needed doing and what needed reviewing and I could check off what was completed. Here is a snapchat of my board near the end of the project.

![Trello board](https://user-images.githubusercontent.com/99325859/157636066-a2f944f9-4c2f-4104-afad-b0d2aad9cbc4.png)
Trello board can be accessed here https://trello.com/b/vaRB1pcm/qa-project

![ci pipeline](https://user-images.githubusercontent.com/99325859/157665986-dd55a1c5-8ce0-46d8-a90f-04435bc7cc4c.png)

For version control I decided to use git hosted by github. This version control host allows easy updating and saving changes to the project via its commit command which you can also leave a note for. GitHub is where the commit's and file are sent and is a repository hosting service.

For the development environment python3 was used in this project. As we used a virtual environment on python3 it made sense to use flask for the web development as python and flask go hand in hand.

Jenkins is what was intended to be used to run the app on however due to a internal Server issue it was not possible to do this. Ideally the app would have its own independent server from which the app would run on. 

## Risk Assesment

In the initial planning stages of the project a risk assessment was conducted to pinpoint any potential risks that may occur during or after deployment of the web app. With this now done it helps identify where measures are need more than others and are the probability of the incident occuring. 

![Risk-Assesment](https://user-images.githubusercontent.com/99325859/157317984-c48cf0bb-802d-4e68-9403-7ad889647f78.png)

The risk assesment shows some of the control measures implemented to reduce any risks. Some of these include:



## Testing 

Testing the app is a crucial part of the development of the app. The tests were carried out in two different ways:

- The first test was carried out within the app with unit testing. This allowed for me to check that each of the CRUD functions were working as intended
- The second test was an intergration test which allows me to see how the app performs in a live-environment where hundred of thousands of interactions withint the app could be happening every second. Again this would help test if the functionality of the app were working as intended. As seen by the screenshot below the jenkins test concluded it as a success
![jenkins test result](https://user-images.githubusercontent.com/99325859/157643398-a93f71d9-f484-46d5-aca9-a03ed16e277e.png)

The coverage report shows the % of all codes which were tested and provides a html document detailing the coverage of the test. As seen below the coverage was a 100% meaning everything in the project was tested for failure and everything has been checked and been ticked of to successful 
![coverage](https://user-images.githubusercontent.com/99325859/157643413-67ca00a4-e575-4cce-9212-e16e5b2f3db0.png)


# The App:

When intially opening up the app the user is directed striaght to the homepage. This page will show all information that has been previously imputed or none if its the users first time. It has all the infomation split into its respective headers and spaced out between each other. It has the Read, Update and Delete functionality all there with the Create functionality on the navigation bar.

![qa-1-home](https://user-images.githubusercontent.com/99325859/157319275-a5ae591f-f142-4035-9fec-c63ac8bd9e57.png)

The navigation bar holds the create functionality for each of the tables. Clicking on one redirets the user to the respective create page. On this example clicking the create employee page redirects the user ot the page where they can input the details of a new employee an then submit the details when done. 

![qa-2-add](https://user-images.githubusercontent.com/99325859/157319613-a12847bd-6e86-4ae1-97b7-afd457e4c211.png)

Like the previous create page the create job and crete employment will do the same and provide a page to fill in information. The major difference with the create employment page is that it uses the information from the job and employment page to bring the user a drop down menu for choices. This is how the 2 tables link. Notice how the headers of the create pages are different to the update page and this was done using ptitles. 

![qa-3-addjob](https://user-images.githubusercontent.com/99325859/157320080-f932aac9-bc0b-44ea-a6d7-68576aec032d.png)
![qa-4-employ](https://user-images.githubusercontent.com/99325859/157320099-1f76d881-9464-4201-ad8a-eaf9959ca04e.png)

## Updates:

10.03.2022
 - Deleting a job or employee will now delete its related employment saving having to delete more than 1 entity

## Current Issues:

- Hard to validate employees in employement with the same name as employement doesnt give employee information just a name
