from fastapi import FastAPI

from .routers import admin, users

app = FastAPI(debug=True)

app.include_router(admin.router, tags=['admin'])
app.include_router(users.router)
