# IPL-management-System

---

# 🏏 IPL Management System

This project implements a basic **IPL (Indian Premier League) Management System** using **Object-Oriented Programming (OOP)** concepts in **Python**. It organizes player data, manages multiple teams, and identifies top performers such as good batsmen, good bowlers, and all-rounders based on their performance stats.

---

## 🚀 Features

* Player class using **Encapsulation**
* Teams with **11 players** each from 4 IPL franchises:

  * Mumbai Indians (MI)
  * Royal Challengers Bangalore (RCB)
  * Chennai Super Kings (CSK)
  * Gujarat Titans (GT)
* Player information includes:

  * Jersey Number
  * Name
  * Team Name
  * Runs Scored
  * Wickets Taken
* Utility functions to:

  * Display good batsmen (`Runs > 400`)
  * Display good bowlers (`Wickets > 10`)
  * Display all-rounders (`Runs > 200` **and** `Wickets > 5`)

---

## 🧱 Concepts Used

* **Encapsulation**:

  * Private player attributes (`__jersey_no`, `__name`, etc.)
  * Access through **getter** and **setter** methods.
* **Class Implementation**:

  * Single `Player` class managing all data.
* **Data Management**:

  * Player objects are grouped into teams using lists.
* **Filtering and Condition Checking**:

  * Logic to filter and display players based on performance metrics.

---

## 📂 File Structure

```bash
ipl_management_system.py  # Main script containing all logic
```

---

## 📝 Sample Output

```
*** Good Batsmen (Runs > 400) ***

Jersey No: 45
Name     : Rohit Sharma
Team     : MI
Runs     : 418

...

*** Good Bowlers (Wickets > 10) ***

Jersey No : 18
Name      : Trent Boult
Team      : MI
Wickets   : 22

...

*** All-Rounders (Runs > 200 and Wickets > 5) ***

-------------------------------
Jersey No   : 19
Name        : Hardik Pandya
Team        : MI
Runs Scored : 224
Wickets     : 14
-------------------------------
```

---

## 🛠️ How to Run

1. Install Python (version 3.x)
2. Save the code as `ipl_management_system.py`
3. Run using:

```bash
python ipl_management_system.py
```

---

## 📌 Additional Notes

* The code includes comments and structure for better understanding.
* Lambda + `filter()` examples are provided at the end for compact logic.
* This is a beginner-friendly implementation for learning OOP and data handling.

---

## 📚 Learning Objectives

* Understand the use of encapsulation and object attributes.
* Practice class design and object creation.
* Learn how to filter and process objects in Python based on conditions.
* Get hands-on experience with a real-world-like data structure project.

---

## 📬 Author

**Created by:** PRIYANSHU GAUTAM BAGDE
**Use Case:** Educational project for understanding Python OOP concepts with IPL data.

---
