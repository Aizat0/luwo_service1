from fastapi import FastAPI
from sqladmin import Admin
from mysite.database.db import engine
from mysite.admin.views import UserProfileAdmin

def setup_admin(app: FastAPI):
    admin = Admin(app, engine)
    admin.add_view(UserProfileAdmin)

