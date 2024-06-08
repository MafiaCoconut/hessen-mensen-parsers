from fastapi import FastAPI

from infrastructure.config.scheduler_services_config import set_all_scheduler_service
from infrastructure.web.api import router
app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    # TODO добавить сюда scheduler
    set_all_scheduler_service.execute()



# if __name__ == '__main__':
#     pass

