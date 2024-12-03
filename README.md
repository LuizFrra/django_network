
# Django Career Post API

This is a simple REST API built with Django for managing career-related posts. The API supports creating, retrieving, updating, and deleting posts. The project uses modern tools and technologies such as Django, PostgreSQL, Docker, and Poetry for dependency management.

---

## **Technologies Used**
- **Django**: Web framework for rapid development.
- **Django REST Framework (DRF)**: For building REST APIs.
- **PostgreSQL**: Database for data persistence.
- **Docker & Docker Compose**: For containerized development.
- **Poetry**: Python dependency management.
- **Pytest**: For testing the application.

---

## **Project Structure**

```plaintext
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── config/
│   ├── asgi.py
│   ├── prod_settings.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── network/
│   ├── migrations/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── apps.py
├── tests/
│   ├── test_models/
│   ├── test_serializers/
│   ├── test_views/
```

---

## **Endpoints**

### 1. **Create a Post**
   - **URL**: `/careers/`
   - **Method**: `POST`
   - **Payload**:
     ```json
     {
       "username": "john_doe",
       "title": "Senior Developer",
       "content": "Looking for a senior developer position."
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "username": "john_doe",
       "title": "Senior Developer",
       "content": "Looking for a senior developer position.",
       "created_datetime": "2024-12-03T12:34:56Z"
     }
     ```
   - **Example CURL**:
     ```bash
     curl -X POST http://127.0.0.1:8000/careers/ \
     -H "Content-Type: application/json" \
     -d '{"username": "john_doe", "title": "Senior Developer", "content": "Looking for a senior developer position."}'
     ```

---

### 2. **Retrieve Posts**
   - **URL**: `/careers/`
   - **Method**: `GET`
   - **Response**:
     ```json
     {
       "count": 2,
       "next": null,
       "previous": null,
       "results": [
         {
           "id": 1,
           "username": "john_doe",
           "title": "Senior Developer",
           "content": "Looking for a senior developer position.",
           "created_datetime": "2024-12-03T12:34:56Z"
         },
         {
           "id": 2,
           "username": "jane_doe",
           "title": "Junior Developer",
           "content": "Looking for a junior developer position.",
           "created_datetime": "2024-12-03T12:45:00Z"
         }
       ]
     }
     ```
   - **Example CURL**:
     ```bash
     curl -X GET http://127.0.0.1:8000/careers/
     ```

---

### 3. **Update a Post**
   - **URL**: `/careers/<int:post_id>/`
   - **Method**: `PATCH`
   - **Payload**:
     ```json
     {
       "title": "Lead Developer",
       "content": "Looking for a lead developer position."
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "username": "john_doe",
       "title": "Lead Developer",
       "content": "Looking for a lead developer position.",
       "created_datetime": "2024-12-03T12:34:56Z"
     }
     ```
   - **Example CURL**:
     ```bash
     curl -X PATCH http://127.0.0.1:8000/careers/1/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Lead Developer", "content": "Looking for a lead developer position."}'
     ```

---

### 4. **Delete a Post**
   - **URL**: `/careers/<int:post_id>/`
   - **Method**: `DELETE`
   - **Response**: `204 No Content`
   - **Example CURL**:
     ```bash
     curl -X DELETE http://127.0.0.1:8000/careers/1/
     ```

---

## **How to Run the Project**

### Prerequisites
- Install Docker and Docker Compose.
- Install Poetry for dependency management.

### Steps
1Start the project using Docker Compose:
   ```bash
   docker-compose up -d
   ```
2Access the application at `http://127.0.0.1:8000`.

---
