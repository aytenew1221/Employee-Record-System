# Employee Management System

A desktop-based **Employee Management System** built with **Python, Tkinter, and MySQL**. The application provides a graphical interface for managing employee information and connecting employee records to a MySQL database.

## 📌 Project Objective

The objective of this project is to develop a simple and user-friendly employee management application that allows authorized users to manage employee records efficiently.

The system provides a login interface and an employee management dashboard where employee information such as department, name, designation, email, address, date of birth, phone number, country, gender, ID proof, and salary can be entered and displayed.

## ✨ Features

- 🔐 Employee login system
- 👤 Employee information management
- 🏢 Department selection
- 📧 Employee email and contact information
- 💰 Employee salary information
- 📊 Employee dashboard
- 📋 Employee information table
- 🔎 Employee search interface
- 💾 MySQL database connectivity
- 🖼️ Image and logo support
- 🎬 Animated application title
- ⚠️ Input validation and error messages
- 🗃️ Employee record insertion into MySQL

The dashboard includes summary cards for total employees, HR employees, managers, software engineers, and total salary.

## 🛠️ Technologies Used

- **Python**
- **Tkinter** — GUI development
- **MySQL** — database management
- **mysql-connector-python** — Python/MySQL connection
- **Pillow (PIL)** — image handling
- **ttk.Treeview** — employee data table

The project imports Tkinter, Pillow, and MySQL Connector for its graphical interface, image processing, and database connection.

## ⚙️ Requirements

Make sure you have the following installed:

- Python 3.x
- MySQL Server
- MySQL database
- `mysql-connector-python`
- `Pillow`

````

## 🗄️ Database Setup

Create a MySQL database named:

```sql
CREATE DATABASE employee;
````

Create an `employee` table containing the fields required by the application.

The application currently connects to MySQL using the following configuration:

```python
conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="1234",
    database="employee"
)
```

The application then inserts employee information into the `employee` table.

### ⚠️ Important

Do **not** commit real database passwords or credentials to GitHub.

For a real project, use environment variables instead of storing passwords directly in the source code.

## ▶️ How to Run

Start the application with:

```bash
python employee.py
```

The application starts with the login window.

After successful login, the Employee Management System dashboard opens.

## 🔐 Login

The current project contains a simple login check.

```text
Username: admin
Password: 1234
```

> These credentials are currently hard-coded in the source code for demonstration purposes. They should be replaced with database-based authentication and secure password handling in a production application.

## 👨‍💼 Employee Information

The system provides fields for:

- Department
- Name
- Designation
- Email
- Address
- Married Status
- Date of Birth
- Date of Joining
- ID Proof
- Gender
- Phone
- Country
- Salary

These fields are displayed through the employee information form.

## 📊 Employee Table

Employee records are displayed using a Tkinter `Treeview`. The table contains columns for employee department, name, designation, email, address, marital status, DOB, DOJ, ID proof, gender, phone, country, and salary.

## 🔎 Search

The interface includes an employee search section with options to search by:

- Phone
- ID Proof

It also provides **Search** and **Show All** buttons.

## 💾 Database Operations

The current implementation demonstrates inserting employee records into MySQL.

When required fields are missing, the application displays an error message. Otherwise, it creates a MySQL connection, inserts the employee data, commits the transaction, and closes the connection.

## 🚀 Future Improvements

The project can be extended with:

- [ ] Implement Update functionality
- [ ] Implement Delete functionality
- [ ] Implement Search functionality
- [ ] Implement Show All functionality
- [ ] Load employee records automatically from MySQL
- [ ] Replace hard-coded login credentials with database authentication
- [ ] Add password hashing
- [ ] Add stronger form validation
- [ ] Move database credentials to environment variables
- [ ] Add employee profile images
- [ ] Add salary calculations and reports
- [ ] Add export to CSV/PDF
- [ ] Improve responsive UI design

## 🎯 Learning Outcomes

This project demonstrates practical use of:

- Python programming
- Object-oriented programming
- Tkinter GUI development
- MySQL database connectivity
- SQL `INSERT` operations
- Form validation
- GUI event handling
- Tkinter `Treeview`
- Image handling with Pillow
- Exception handling

## 👨‍💻 Author

**Aytenew Ayele**

GitHub: `https://github.com/YOUR-USERNAME`

## 📄 License
