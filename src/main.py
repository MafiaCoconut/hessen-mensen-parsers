from fastapi import FastAPI

from infrastructure.config.scheduler_services_config import start_scheduler_service
from infrastructure.config import logs_config
from infrastructure.web.api import router

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    start_scheduler_service.execute()
    logs_config.config()



if __name__ == '__main__':
    pass
    # obj = GiessenTHMParserInterfaceImpl()
    # obj.parse()

