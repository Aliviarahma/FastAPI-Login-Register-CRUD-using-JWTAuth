# Backend 
1. For run project install poetry to your pc check here [https://python-poetry.org/](https://python-poetry.org/) 
2. Run virtual environment or venv folder using script ```.\venv\Scripts\activate``` on windows
4. Add alembic using script: ```poetry add alembic```
3. Generate table to your database PostgreSQL
- Activate Port Forwarding on Termius, using port: ```5433```
- go to backend folder run: ```alembic upgrade head```
5. Run backend using script : ```poetry run start```

Open ```http://localhost:5000/docs``` with your browser to see the result.

## Cek Port Active 
```netstat -tlnp```

## Run on Server
- Up service on server: ```uvicorn app.main:app --host 0.0.0.0 --port 5000 --log-config log.ini --reload &```
- Turn off service: ```kill -9 $(lsof -t -i:5000)```