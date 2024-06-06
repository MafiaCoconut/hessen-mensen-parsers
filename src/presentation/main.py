from fastapi import FastAPI
from infrastructure.web.api import router
app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    pass


