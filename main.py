from fastapi import FastAPI
# from os import getenv
# import uvicorn

app = FastAPI(title='FastApi on vercel')

@app.get('/')
async def root():
    return "Welcome to FastAPI on Vercel"


# if __name__ == "__main__":
#     port = int(getenv("PORT", 8000))
#     uvicorn.run("main:app", host="127.0.0.1", port=port ,reload=True)