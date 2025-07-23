
# E-Commerce API

This project is a RESTful E-Commerce API built with FastAPI, SQLAlchemy, and PostgreSQL. It provides functionalities for user management, product handling, order processing, and administrative tasks.

## Table of Contents

-   [Features](#features)
-   [Prerequisites](#prerequisites)
-   [Setup Instructions](#setup-instructions)
    -   [1. Clone the Repository](#1-clone-the-repository)
    -   [2. Create a Virtual Environment](#2-create-a-virtual-environment)
    -   [3. Install Dependencies](#3-install-dependencies)
    -   [4. Database Setup](#4-database-setup)
    -   [5. Environment Variables](#5-environment-variables)
    -   [6. Run the Application](#6-run-the-application)
-   [API Endpoints](#api-endpoints)
-   [Authentication](#authentication)
-   [Contributing](#contributing)
-   [License](#license)

## Features

* **User Management**: User signup, login, logout, password reset, and fetching user details.
* **Authentication & Authorization**: JWT-based authentication for secure access and role-based authorization (admin/user).
* **Product Management**: (Implicitly, through orders)
* **Order Management**: Create orders, cancel orders, view user-specific orders, get order details by ID, and check order status.
* **Admin Features**: Update user roles to admin, view all orders, and update order statuses.
* **Error Handling**: Centralized exception handling for various HTTP errors.
* **Database**: PostgreSQL integration with SQLAlchemy ORM.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Python 3.8+**
* **pip** (Python package installer)
* **PostgreSQL** database server

## Setup Instructions

Follow these steps to get the E-Commerce API up and running on your local machine.

### 1. Clone the Repository

First, clone the project repository to your local machine:

\`\`\`bash
git clone https://github.com/swarookali-3121/e-commerce-api.git
cd e-commerce-api/E-Commerce-API-76f2db33eae48e6f19a2aa1b68386117d1edb531
\`\`\`

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies:

\`\`\`bash
python -m venv venv
\`\`\`

Activate the virtual environment:

On Windows:

\`\`\`bash
.\venv\Scripts\activate
\`\`\`

On macOS/Linux:

\`\`\`bash
source venv/bin/activate
\`\`\`

### 3. Install Dependencies

Install all the required Python packages using pip:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

If you don't have a `requirements.txt`, create one with:

\`\`\`txt
fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
python-dotenv
passlib[bcrypt]
python-jose[cryptography]
pydantic
\`\`\`

Then run:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Database Setup

Create a PostgreSQL Database:

\`\`\`sql
CREATE DATABASE onlinestore;
\`\`\`

Ensure the user `postgres` with password `swaroop` has access, or adjust your connection string accordingly.

The application will automatically create tables when it starts.

### 5. Environment Variables

Create a `.env` file in the root directory with the following:

\`\`\`env
DATABASE_URL="postgresql://postgres:swaroop@localhost:5432/onlinestore"
ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="your_super_secret_key_here"
ALGORITHM="HS256"
\`\`\`

### 6. Run the Application

Run the FastAPI application using Uvicorn:

\`\`\`bash
uvicorn main:app --reload
\`\`\`

Access Swagger UI: http://127.0.0.1:8000/docs  
Access ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

- **Authentication**: `/auth` prefix for login, logout, forgot password, reset password.
- **Users**: `/users` prefix for signup and info.
- **Orders**: `/orders` prefix for order handling.
- **Admin**: Admin routes are secured and do not have a separate prefix.

Refer to `/docs` or `/redoc` for full endpoint details.

## Authentication

- **Login**: `/login` with email and password to get access token.
- **Token**: Access token is set as a cookie named `token`.
- **Protected Routes**: Require a valid token, verified with the `verify_token` dependency.

## Contributing

Contributions are welcome! Submit issues or pull requests.

## License

Specify your project's license here (e.g., MIT, Apache 2.0).
