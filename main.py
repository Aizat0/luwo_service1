from fastapi import FastAPI
from mysite.api import user, auth
import uvicorn
from mysite.database.db import Base, engine

Base.metadata.create_all(bind=engine)
auth_app = FastAPI(title='Auth Project')
auth_app.include_router(user.user_router)
auth_app.include_router(auth.auth_router)

if __name__ == '__main__':
    uvicorn.run(auth_app, host='127.0.0.1', port=8001)