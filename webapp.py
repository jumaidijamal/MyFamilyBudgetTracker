from fastapi import FastAPI
from fastapi.staticfiles import (
    StaticFiles
)

from api.dashboard_api import (
    router as dashboard_router
)

app = FastAPI(
    title="Budget Tracker Dashboard"
)

app.include_router(
    dashboard_router
)

app.mount(
    "/static",
    StaticFiles(
        directory="web/static"
    ),
    name="static"
)