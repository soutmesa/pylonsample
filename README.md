# Project Title

This project aims to provide a comprehensive solution for managing employee data using FastAPI, SQLAlchemy, and a Microsoft SQL Server database.
It includes functionalities for viewing, updating, and exporting employee data, as well as implementing basic authentication for securing access to the APIs.

## Features
- **Employee Data Management**: Allows users to view and update employee details such as designation, project, team, supervisor, join date, and resign date.
- **CSV Export**: Provides an endpoint to export employee data in CSV format.
- **Basic Authentication**: Implements basic authentication to secure access to the APIs.
- **API Documentation**: Generates interactive API documentation using Swagger UI and Redocly.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation and Setup](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Usage](#usage)

## Project Structure
```bash
.
├── core
│ ├── init.py
| ├── connection.py
| └── dependencies.py
├── middleware
│ ├── init.py
| └── basic_auth_middleware.py
├── models
│ ├── init.py
| └── sample_manpower_list_model.py
├── repository
│ ├── init.py
│ ├── base_repository.py
│ └── sample_manpower_list_repository.py
├── routes
│ ├── init.py
| └── sample_manpower_list_routes.py
├── schema
| └── sample_manpower_list_schema.py
├── service
│ └── init.py
│ ├── base_service.py
│ └── sample_manpower_list_service.py
├── main.py
```
Briefly describe the structure of the project and the purpose of each directory:

- **core**: Contains core functionalities such as database connection and dependencies.
- **middleware**: Includes custom middleware, such as authentication middleware.
- **model**: Defines database models or ORM classes.
- **repository**: Houses repository classes responsible for database interactions.
- **routes**: Contains route definitions for various endpoints.
- **schema**: Defines Pydantic schemas for request and response validation.
- **service**: Includes service classes implementing business logic.

## Installation and Setup

### Python 3 Installation
Before proceeding, ensure that Python 3 is installed on your machine. If not, follow these steps to install Python 3:

1.  Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python 3 for your operating system.

2.  Run the installer and follow the installation instructions.

3.  Verify that Python 3 is installed by opening a terminal or command prompt and running the following command:
```bash
python3 --version
```
### Project Setup
To set up the project environment, follow these steps:

```bash
# Clone the repository
git clone https://github.com/soutmesa/pylonsample.git

# Navigate to project directory
cd pylonsample

# Install dependencies
pip install -r requirements.txt

or

python3 -m pip install -r requirements.txt
```

## Configuration
Set up the environment variables
- Create a .env file in the project root directory.
- Add the following configurations to the .env file
```bash
DB_HOST=localhost
# or DB_HOST=sqlserver enable sqlserver in docker-compose.yml
DB_USER=sa
DB_PASSWORD="DB_Password"
DATABASE_URL="mssql+pymssql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}/PylonProductionData_ForTesting"

# Basic auth credentials
USERNAME=user
PASSWORD="pass"

# Expose port for running with docker only
CONTAINER_PORT=4000
```

## Running the Application
Once the project environment is set up, you can run the FastAPI application:
### Running with uvicorn
```bash
# Run the FastAPI application
uvicorn src.main:app --reload
```

### Running with Docker Compose
To run the application using Docker Compose, follow these steps:

1. Ensure Docker is installed on your machine.

2. Build and start the Docker containers:

```bash
docker-compose up -d
```

## API Documentation

You can access these API documentations after running the application.

- [Swagger UI (http://localhost:8000/docs)](http://localhost:8000/docs)
- [Redoc UI (http://localhost:8000/redoc)](http://localhost:8000/redoc)

## Usage
### Example with cURL
Here are some example cURL commands to interact with your FastAPI application using Basic Authentication:

1. Encode your credentials (USERNAME
) in base64. You can do this using an online tool or with the following command in a Unix-based terminal:
```bash
echo -n "USERNAME:PASSWORD" | base64
```
Replace USERNAME and PASSWORD with your actual credentials. This will output a base64 encoded string.

2. Use the encoded credentials in your cURL requests.
For example, if the encoded string is dXNlcm5hbWU6cGFzc3dvcmQ=, you can use it as follows:

- Retrieve all employees:
```bash
curl -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" http://localhost:8000/api/v1/employees
```
- Update employee details (replace {manpowerId} with the actual ID):
```bash
curl -X PATCH -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" -H "Content-Type: application/json" -d '{"designation": "New Designation", "project": "New Project", "team": "New Team", "supervisor": "New Supervisor", "joinDate": "2024-01-01", "resignDate": "2024-12-31"}' http://localhost:8000/api/v1/employees/{manpowerId}
```
- Download employee data as CSV
```
curl -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" -o employees.csv http://localhost:8000/api/v1/employees/csv
```
Replace dXNlcm5hbWU6cGFzc3dvcmQ= with your actual base64 encoded credentials and http://localhost:8000 with the appropriate URL if your FastAPI application is hosted elsewhere.

![Swagger UI](assets/swagger.png)
![Redoc UI](assets/redoc.png)