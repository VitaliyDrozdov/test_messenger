from fastapi import FastAPI

app = FastAPI(title="test_messanger")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8005)
