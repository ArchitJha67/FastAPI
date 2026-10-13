# FastAPI Blog

A blog application built with FastAPI while following Corey Schafer's Python FastAPI Tutorials series on YouTube. It has a JSON API for users and posts, plus server-rendered pages using Jinja2 templates.

This is a learning project. I'm building it along the way and pushing each stage to GitHub as I go.

Features (so far)
REST API for users and posts with create, read, update (PATCH) and delete
Server-rendered pages: home feed, single post, per-user posts and a custom error page
SQLAlchemy models with a SQLite database and a user-to-posts relationship
Pydantic schemas for request validation and responses
Path parameter validation and error handling
Profile pictures with a default fallback
Static files (CSS, JS, icons) and a web manifest
Tech Stack
Python 3.11
FastAPI for the web framework
SQLAlchemy for the ORM
SQLite for the database
Jinja2 for templates
Pydantic for data validation
uv for dependency management
Project Structure
fastapi_blog/
├── main.py            # App setup, API routes and page routes
├── models.py          # SQLAlchemy models (User, Post)
├── schemas.py         # Pydantic schemas
├── database.py        # Database engine, session and get_db dependency
├── templates/         # Jinja2 templates (layout, home, post, user_posts, error)
├── static/            # CSS, JS, icons, default profile picture
├── media/             # Profile pictures
├── pyproject.toml     # Project dependencies
└── uv.lock            # Locked dependency versions
Getting Started
Prerequisites
Python 3.11
uv
Installation
bash
git clone https://github.com/ArchitJha67/FastAPI.git
cd FastAPI/fastapi_blog
uv sync
Run the app
bash
uv run fastapi dev main.py

The app runs at http://127.0.0.1:8000.

API Documentation

FastAPI generates interactive docs automatically:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Example Routes
Method	Route	Description
GET	/	Home page with all posts
GET	/users/{user_id}/posts	Posts by a specific user (page)
PATCH	/api/users/{user_id}	Update a user

See /docs for the full, up-to-date list of endpoints.

Progress Through the Tutorial Series

The series has 19 parts. Checked items are done.

 Part 1: Getting started, web app and REST API
 Part 2: HTML frontend with Jinja2 templates
 Part 3: Path parameters, validation and error handling
 Part 4: Pydantic schemas
 Part 5: Database with SQLAlchemy models and relationships
 Part 6: Completing CRUD (PUT, PATCH, DELETE)
 Part 7: Sync vs async
 Part 8: Routers with APIRouter
 Part 9: Frontend forms with JavaScript
 Part 10: Authentication with JWT
 Part 11: Authorization and protected routes
 Part 12: File uploads and image processing
 Part 13: Pagination
 Part 14: Password reset with email and background tasks
 Part 15: PostgreSQL and Alembic migrations
 Part 16: AWS S3 file storage
 Part 17: Testing with pytest
 Part 18: Deploy to a VPS
 Part 19: Deploy with Docker
Acknowledgements

This project follows the Python FastAPI Tutorials series by Corey Schafer on YouTube. The structure and approach come from his series, and I'm adding to it as I work through each part.

Author

Archit Jha - GitHub
