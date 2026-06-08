# 🧑‍💻 Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to manage users and items.

## 📝 Tasks

### 🛠️  Build the FastAPI app

#### Description

Create a FastAPI application with endpoints for managing users and items.

#### Requirements

Completed assignment should:

- Use FastAPI and run with `uvicorn starter-code:app --reload`
- Implement at least one endpoint for users and one endpoint for items
- Support JSON request bodies for creating and updating resources
- Return appropriate HTTP status codes for success and errors
- Keep data in memory using Python lists or dictionaries

### 🛠️  Add validation and documentation

#### Description

Use Pydantic models to validate request data and make the API self-documenting.

#### Requirements

Completed assignment should:

- Define request and response models with Pydantic
- Return validation errors for invalid input
- Include example request payloads in code blocks
- Verify API docs at `/docs`
