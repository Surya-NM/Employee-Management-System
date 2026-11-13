# Employee Management System – REST API

A backend REST API built using **Python, Django, Django REST Framework, and MySQL** to manage company departments and employees.

## Features

- Create, View, Update and Delete Departments.
- Create, View, Update and Delete Employees.
- Manage employee details.
- Connect employees with departments using ForeignKey.
- Store employee information in MySQL database.
- Use Django REST Framework Generic Class-Based Views.
- Serialize and validate API data.

## Technologies Used

- Python 3.13
- Django 6.1.2
- Django REST Framework 3.18.3
- MySQL
- mysqlclient 2.3.0
- Postman

## Project Structure

```text
Employee Management System/
│
├── CURD/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── managementsystem/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## Database Models

### 1. Department

- name
- description
- created_at

### 2. Employee

- name
- email
- phone
- department
- salary
- joining_date
- is_active
- created_at

**Relationship:** Employee has a ForeignKey relationship with the Department model.

## API Endpoints

Base URL: `http://127.0.0.1:8000/`

| Method                  | Endpoint             | Description                            |
| ----------------------- | -------------------- | -------------------------------------- |
| GET, POST               | `/Departments/`      | List and Create Departments            |
| GET, PUT, PATCH, DELETE | `/Departments/<id>/` | Retrieve, Update and Delete Department |
| GET, POST               | `/Employees/`        | List and Create Employees              |
| GET, PUT, PATCH, DELETE | `/Employees/<id>/`   | Retrieve, Update and Delete Employee   |
| GET                     | `/admin/`            | Django Admin                           |

## Installation and Setup

### 1. Clone Repository

```bash
git clone <your-github-repository-url>
cd "Employee Management System"
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install Django==6.1.2 djangorestframework==3.18.3 mysqlclient==2.3.0
```

### 5. Create MySQL Database

```sql
CREATE DATABASE emp_db;
```

### 6. Configure Database

Update your MySQL database settings in `managementsystem/settings.py`.

Configure your database name, username, password, host and port.

### 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Open your browser:

`http://127.0.0.1:8000/`

## API Testing

All API endpoints can be tested using **Postman**.

## Author

Surya N
