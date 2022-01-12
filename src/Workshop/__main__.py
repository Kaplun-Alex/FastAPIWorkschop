import uvicorn

#from src.Workshop.settings import settings
from Workshop.settings import settings

uvicorn.run(
    "src.Workshop.app:app",
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
