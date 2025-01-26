from fastapi import FastAPI
from pydantic import BaseModel
import psutil
from typing import List

app = FastAPI()

class CPU_Usage(BaseModel):
    cpu: str
    percent: float

@app.get("/cpu_percent")
async def cpu_percent() -> List[CPU_Usage]:
    """
        Retrieves the current CPU usage in percent.

    Returns:
        List[float]: List of CPU usage in percent for each core.
    """
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    # return a list of CPU_Usage objects
    return [CPU_Usage(cpu=f"CPU{idx}", percent=usage) for idx, usage in enumerate(cpu_usage)]

# -------------------------------------------------------------------------