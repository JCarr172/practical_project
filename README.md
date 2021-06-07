# Practical Project

## Contents
* [Introduction](#introduction)
    * [Objective](#Objective)
    * [Plan](#Plan)
* [Architecture](#architecture)
    * [Database Structure](#Database-Structure)
    * [Project Tracking](#Project-Tracking)
    * [Risk Assessment](#Risk-Assessment)
* [CI Pipeline](#CI-Pipeline)
    * [Jenkins](#Jenkins)
    * [Services](#Services)
    * [Docker Swarm](#Docker-Swarm)
* [Development](#development)
    * [Testing](#Testing)
    * [Front end](#Front-end)
* [Further Sprints](#Further-sprints)

## Introduction
#
### **Objective**
The brief for this project was:

Create a application that is composed of at least 4 microservices that work together. Specifically these services will compromise of 1 front-end service, two back-end services, and a fourth back-end service that relies on data from the other back-end services. 

We were also to use all supporting tools and methodologies in core modules.

### **Plan**

To meet the requirements of the MVP I came up with the following application idea:

**DnD character creator**

* Service 1: This is the frontend and displays the final product of all the other services and shows the past five results.
* Service 2: This returned a randomly selected race and class for the character.
* Service 3: This returned a randomly selected list of attribute values for the character.
* Service 4: This took the generated attribute values and adjusted them according to which race was chosen in service 2.

## **Architecture**
#
### **Database Structure**

This application only uses one table, below is an entity diagram for the table. The original plan for the application didn't include the name value but I decided it would make a better app if the user could personalise the created character.

![Entity diagram](https://i.imgur.com/3AdioJa.png)

### **Project tracking**

My project tracking board can be seen below. I choose to use Trello over other providers as Trello is very lightweight and is ideal for smaller projects like this one.

![Trello board](https://i.imgur.com/c7RpyA4.png)

The full board can be found [here](https://trello.com/b/D2qI6f8O/practical-project)

### **Risk Assessment**

Below is the risk assessment table I created in order to outline the major and minor risks that could have an impact on the project. The bottom two rows were not in the original assessment but were added as the project went on.

![Risk assessment](https://i.imgur.com/kgmElwd.png)

The full risk assessment can be found [here](https://docs.google.com/spreadsheets/d/1g2WQ3jpbKXfgx4VQYWGFZtTy_JzJnI_8L0IMbFqrVeg/edit#gid=0)

## **CI Pipeline** ##
#
Continuous integration was used throughout this project as it allows for automation of testing and deployment. Below is a diagram to show the pipeline:

![CI Pipeline](https://i.imgur.com/KWcLJ8S.png)

### **Jenkins**

In order to implement this pipeline, Jenkins was used the CI server. 

![Jenkins Pipeline](https://i.imgur.com/ILleS2i.png)

As shown in the image above, there are five stages in the process:
* Testing: All tests are carried out and reports showing the coverage are produced. If any tests fail then the process stops to prevent push failed docker images.
* Build and Push: Provided all tests are passed then images of each service is created and pushed up to DockerHub.
* Anisble-Configuration: This makes sure ansible is install on the Jenkins VM.
* Install docker: This makes sure docker is installed on all the VM's that require it and then connect them all in a swarm.
* Deploy: Deploys the docker-compose file via the docker manager and then restarts the nginx incase their are any changes to the nginx.conf file.

### **Services**

As stated earlier, this application relies on four microsevers that work in tandem. The diagram below shows the system. Service one or the frontend creates the webpage that displays the created DnD characters. In order to create these characters service 2 and 3 create the race, class and attributes of the character then the race and attributes get sent to service four where it makes the nessecary adjustments before sending them back to service 1. 

![Service diagram](https://i.imgur.com/FI5rvPG.png)

### **Docker Swarm**

As this project makes use of containerised servies, I used Docker Swarm in order to create a network of virtual machines that can host the different containers. In order to limit the amount of access to the application I have implimented a NGINX loadbalancer which the user connects to, this improves additional security to the system. 

![Docker swarm diagram](https://i.imgur.com/uKyFxCR.png)

## Development
#
### **Testing**

Pytest was used to test the functions of the application. As this tests uses random generaters I used Unittest Mocking to make sure the random choices to be the same each time. The below reports show the coverage percentage for each of the serives. For the three background services 100% coverage was acheived ensuring the validity of the tests. However I could reach 100% on the frontend appliction which would have to be addressed in further development.

* Frontend
![Frontend Testing](https://i.imgur.com/bHVwNBz.png)
* Class-generator
![Class-generator Testing](https://i.imgur.com/k9EF3rE.png)
* Stats-generator 
![Stats-generator Testing](https://i.imgur.com/bHVwNBz.png)
* Calculator
![Calculator Testing](https://i.imgur.com/mLPiBnq.png)

These tests are automatically run by Jenkins ensuring that a faultly version of the application is not deployed.
### **Front end**

Below is an exmaple of what the user sees when they access the website. The user can iput their character name and then the application generates the rest of the data at random.
![Front end](https://i.imgur.com/kNBiI0r.png)

## Further Sprints
#

In future sprints I would like to:
* Improve test coverage percentage on the frontend service.
* Allow for limiting what type of character was made, i.e: Only magic users.
* Improve the aesthetics of the webpage.

## Author
#

James Carr

