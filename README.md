**Banking Management System**

Project Overview
The Banking Management System is a Python-based application that simulates a simplified banking environment, enabling users to create accounts, log in, manage funds, and track transactions. The system supports both CLI and GUI interfaces, demonstrating strong object-oriented programming, modular design, and robust data handling practices.

**Tech Stack**
Programming Language: Python 3.13+
**Libraries:**
json – for persistent data storage
CustomTkinter – for GUI interface
Concepts Applied: Object-Oriented Programming (Abstraction, Encapsulation), Modular Functions, Exception Handling, Data Persistence
Data Storage: JSON file (Bank_Data.json) for user accounts and transaction history

**Prerequisites**
Python 3.13 or higher installed
Required Python libraries: customtkinter (can be installed via pip install customtkinter)
Basic knowledge of running Python scripts in CLI or IDE (VS Code, PyCharm, etc.)

**JSON file (Bank_Data.json) initialized with a structure like:**
{
    "users": {}
}

**Impact by Concept**

**Abstraction**
**Used where:** Operations class methods (deposit, withdraw, check balance)
**Purpose:** Hide internal implementation details from users
**Impact:** Simplifies interface and enhances code maintainability

**Encapsulation**
**Used where:** Operations class storing user data and transactions
**Purpose:** Protect sensitive account information
**Impact:** Ensures data integrity and prevents unauthorized modifications

**Functions & Modular Design**
**Used where:** Login, signup, and banking operations functions
**Purpose:** Separate responsibilities and organize code logically
**Impact:** Improves reusability, readability, and scalability

**Login & Signup Functionality**
**Used where:** login.py and signup.py
**Purpose:** Authenticate users and create accounts securely
**Impact:** Reduces invalid access attempts and prevents duplicate accounts

**Banking Operations**
**Used where:** Operations.py methods for deposit, withdrawal, and balance check
**Purpose:** Execute core banking functionalities
**Impact:** Ensures accurate account management and transaction tracking

**Persistent Data Handling (JSON)**
**Used where:** Bank_Data.json file for storing accounts and transactions
**Purpose:** Maintain data persistence across sessions
**Impact:** Guarantees consistent data integrity and enables auditability

**GUI Integration (CustomTkinter)**
**Used where:** gui.py to interact with backend operations
**Purpose:** Provide a user-friendly interface
**Impact:** Enhances accessibility and separates frontend from backend logic

**Exception Handling & Input Validation**
**Used where:** Across all modules (login, signup, operations)
**Purpose:** Handle invalid inputs and prevent runtime errors
**Impact:** Increases system reliability and ensures a smooth user experience
