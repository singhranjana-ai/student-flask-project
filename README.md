# student-flask-project
# Flask Student Registration Project

A beginner-friendly Flask web application that registers students and stores their details in Amazon RDS MySQL.

## Technology Stack

- Python
- Flask
- MySQL
- Amazon EC2
- Amazon RDS
- Git and GitHub
- Gunicorn

## Project Features

- Student registration form
- Save student name and email to MySQL
- Display registered student records
- Deploy application on AWS EC2

## Repository Structure

```text
student-flask-project/
├── app.py
├── requirements.txt
├── schema.sql
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## Database Configuration

The application uses these environment variables:

- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`
- `DB_PORT`
- `SECRET_KEY`

Never commit database credentials or secrets to GitHub.

## Deployment Plan

1. Create an Amazon RDS MySQL database.
2. Create an EC2 instance.
3. Install Git and Python on EC2.
4. Clone this repository.
5. Install dependencies from `requirements.txt`.
6. Configure environment variables.
7. Run the application using Gunicorn.
8. Test student registration and database storage.

## Database Schema

Execute `schema.sql` against your RDS MySQL instance after creating the database user and configuring access.

## Important

Keep RDS private where possible. Configure security groups to allow MySQL access only from the application EC2 instance. Use HTTPS for production access.
