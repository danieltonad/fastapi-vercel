from fastapi import FastAPI

app = FastAPI(title='FastApi on vercel')

@app.get('/')
async def root():
    return "Welcome to FastAPI on Vercel"