# Fitness Management System

This project is a Python-based fitness management system that uses MySQL for database operations. It allows you to manage members of a gym, including checking the list of members, adding new members, finding members, and updating member information.

## Features

- **Check List of Members**: View all registered gym members.
- **Add New Member**: Register a new member with details such as GYM ID, Name, Age, Membership type, and Days Fixed.
- **Find Member**: Search for a member by their ID or Name.
- **Update Member Information**: Update membership type or age of an existing member.

## Setup Instructions

### Requirements

- Python 3.x
- MySQL

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/fitness-management-system.git
    cd fitness-management-system
    ```

2. **Install MySQL Connector**:
    ```bash
    pip install mysql-connector-python
    ```

3. **Setup Database**:
    ```sql
    CREATE DATABASE fitness;
    USE fitness;
    CREATE TABLE MEMBER (
        GYM_ID VARCHAR(10) PRIMARY KEY,
        NAME VARCHAR(100),
        AGE INT,
        MEMBERSHIP VARCHAR(20),
        DAYS_FIXED VARCHAR(20)
    );
    ```

## Usage

Run the main script to start the application:
```bash
python project.py
