from fastapi import FastAPI

# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from infrastructure.config.scheduler_services_config import start_scheduler_service
from infrastructure.config import logs_config
from infrastructure.web.api import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app):
    logs_config.config()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == '__main__':
    pass
    # obj = GiessenTHMParserInterfaceImpl()
    # obj.parse()

