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

**DnD character creater**

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

## **CI Pipeline** ##
#

![CI Pipeline](https://i.imgur.com/KWcLJ8S.png)



![Frontend Testing](https://i.imgur.com/bHVwNBz.png)
![Class-generator Testing](https://i.imgur.com/k9EF3rE.png)
![Stats-generator Testing](https://i.imgur.com/bHVwNBz.png)
![Calculator Testing](https://i.imgur.com/mLPiBnq.png)