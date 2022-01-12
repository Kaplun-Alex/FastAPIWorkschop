import uvicorn

uvicorn.run(
    "src.Workshop.app:app",
    reload=True,
)