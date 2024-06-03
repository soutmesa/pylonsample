# Project Title

Brief description of your project.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)

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
- **models**: Defines database models or ORM classes.
- **repository**: Houses repository classes responsible for database interactions.
- **routes**: Contains route definitions for various endpoints.
- **schemas**: Defines Pydantic schemas for request and response validation.
- **service**: Includes service classes implementing business logic.

## Installation

Describe how to install your project, including any dependencies and how to set up the environment.

```bash
# Clone the repository
git clone https://github.com/soutmesa/pylonsample.git

# Navigate to project directory
cd pylonsample

# Install dependencies
pip install -r requirements.txt or python3 -m pip install -r requirements.txt
```

## Configuration
```bash
DATABASE_URL="mssql+pyodbc://sa:DB_Password@localhost/PylonProductionData_ForTesting?driver=ODBC+Driver+17+for+SQL+Server"

// Basic auth credentials
USERNAME=TestUser1
PASSWORD="TestUs3r1#21"

// Expose port for running with docker only
CONTAINER_PORT=4000
```

## Usage
```bash
# Run the FastAPI application
uvicorn src.main:app --reload
```

## API Documentation

You can access these API documentations after running the application.
```bash
http://localhost:8000/docs
http://localhost:8000/redoc
```