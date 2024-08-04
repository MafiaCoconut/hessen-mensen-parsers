from datetime import datetime
from typing import List
from typing import Optional, Callable
from pydantic import BaseModel, Field


class Job(BaseModel):
    func: Callable = Field(default=None)
    trigger: str = Field(default=None)
    run_date: datetime = Field(default=None)
    args: list = Field(default=None)
    job_id: Optional[str] = Field(default=None)
    job_type: Optional[str] = Field(default=None)

