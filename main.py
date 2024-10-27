from fastapi import FastAPI

app = FastAPI()
items = ["banana", "apple","cherry"]

@app.get("/items")
async def read_items():
    return {"items" :items}
