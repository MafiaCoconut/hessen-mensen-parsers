from fastapi import FastAPI, Depends

from application.interfaces import scheduler_interface
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from infrastructure.config import logs_config
from infrastructure.config.services_config import get_scheduler_service
from infrastructure.web.api import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app):
    logs_config.config()
    scheduler_service = get_scheduler_service()
    await scheduler_service.set_start_jobs()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == '__main__':
    pass
    # obj = GiessenTHMParserInterfaceImpl()
    # obj.parse()

