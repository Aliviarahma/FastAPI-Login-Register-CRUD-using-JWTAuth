# FastAPI using PostgreSQL (Login-Register and CRUD application)

FastAPI is a modern, high-performance web framework for building APIs in Python based on standard type hints. This is a backend development project using FastApi as framework and PostgreSQL as database and Poetry for dependency management. Besides that this backend SQLModel an asynchronous ORM and implements JWT Auth to authenticate and authorize users in web applications and APIs. So, once a user is authenticated, the user gets a secure token that they can use across all systems. This backend includes endpoint Registration, Login, Forgot Password and integrated with CRUD.

# Backend 
1. For run project install poetry to your pc check here [https://python-poetry.org/](https://python-poetry.org/) 
2. Run virtual environment or venv folder using script ```.\venv\Scripts\activate``` on windows
3. Add alembic using script: ```poetry add alembic```
4. Generate table to your database PostgreSQL
5. go to backend folder run: ```alembic upgrade head```
6. Run backend using script : ```poetry run start```

Open ```http://localhost:8000/docs``` with your browser to see the result.

