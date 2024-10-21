# Inventory Management System API
A Django REST Framework-based backend API for managing inventory items. This API supports CRUD operations, JWT-based authentication for secure access, and caching with Redis for improved performance. PostgreSQL is used as the database, and unit tests ensure API functionality.

# Features
    1. CRUD Operations: Create, Read, Update, and Delete inventory items.
    2. JWT Authentication: Secure access to all endpoints using JSON Web Tokens.
    3. PostgreSQL: Robust database for storing inventory data.
    4. Redis Caching: Caches frequently accessed items for improved performance.
    5. Logging: Integrated logging for API activity and error tracking.
    6. Unit Tests: Comprehensive tests to ensure API functionality.

# Table of Contents
    Requirements
    Installation
    Environment Setup
    Migrations
    Running the Server
    API Endpoints
    Testing
    Notes
    License

# Requirements
    Python 3.9+
    Django 4.x
    Django REST Framework
    PostgreSQL
    Redis
    Docker (optional, for running Redis)

# Installation
1. Clone the Repository:

    git clone https://github.com/yourusername/inventory-management-api.git
    cd inventory-management-api

2. Create and Activate a Virtual Environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies:

    pip install -r requirements.txt

# Environment Setup

    1. Create a .env file in the root directory and add the following variables:

        makefile
        SECRET_KEY=your_secret_key
        DEBUG=True
        DATABASE_NAME=your_db_name
        DATABASE_USER=your_db_user
        DATABASE_PASSWORD=your_db_password
        DATABASE_HOST=localhost
        DATABASE_PORT=5432

    2. Run Redis: If using Docker, you can run Redis with:

        docker run -p 6379:6379 -d redis:latest

# Migrations
    1. Make Migrations:
    python manage.py makemigrations

    2. Apply Migrations:
    python manage.py migrate

# Running the Server
Start the Django development server:

    python manage.py runserver

# API Endpoints
## Authentication
    POST /auth/register/ - Register a new user.
    POST /auth/login/ - Obtain a JWT token for authentication.

# Inventory Management

    GET /items/ - List all items.
    POST /items/create/ - Create a new item.
    GET /items/<int:id>/ - Retrieve details of an item.
    PUT /items/<int:id>/update/ - Update an item.
    DELETE /items/<int:id>/delete/ - Delete an item.

# Example Request Body for Creating an Item
    json
    {
    "name": "Test Item",
    "description": "A sample item for testing.",
    "quantity": 10,
    "price": "99.99"
    }

# Testing
Run unit tests to ensure all functionality is working as expected:

    python manage.py test inventory

# Notes
    Caching: Caching is implemented using Redis for the GET item endpoint. Items are cached for 5 minutes.
    Logging: Logs are stored for tracking API usage and errors.
    Handling Redis Keys Issue: If redis-cli KEYS '*' returns an empty list, we will address this after completing the setup.



