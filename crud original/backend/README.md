# Student Management System — Backend (Django REST Framework + MySQL)

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the MySQL database:
   ```sql
   CREATE DATABASE sms_db CHARACTER SET utf8mb4;
   ```

4. Copy `.env.example` to `.env` and fill in your real values (DB password, secret key, etc.). Never commit `.env`.

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create an admin user (optional, for `/admin/`):
   ```bash
   python manage.py createsuperuser
   ```

7. Run the dev server:
   ```bash
   python manage.py runserver
   ```
   API is now live at `http://127.0.0.1:8000/api/students/`.

## API Endpoints

| Operation | Method | Endpoint                | Notes                                  |
|-----------|--------|--------------------------|-----------------------------------------|
| Create    | POST   | `/api/students/`         | JSON body, see fields below             |
| Read all  | GET    | `/api/students/`         | Supports `?search=`, `?department=`, `?year=`, `?ordering=` |
| Read one  | GET    | `/api/students/<id>/`    |                                          |
| Update    | PUT/PATCH | `/api/students/<id>/` | PUT = full update, PATCH = partial      |
| Delete    | DELETE | `/api/students/<id>/`   |                                          |

### Student fields
`first_name`, `last_name`, `email` (unique), `phone`, `department`, `year` (1–4), `enrollment_date` (read-only, auto-set)

## Testing with Postman
- Import the endpoints above into a Postman collection.
- Test Create with valid data, missing required fields, and a duplicate email — confirm validation errors return HTTP 400 with clear messages.
- Test Update/Delete with a valid ID and then a non-existent ID (expect 404).
- Test Read with an empty table and a populated one.
