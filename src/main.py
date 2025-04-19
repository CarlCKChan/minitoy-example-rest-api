import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     stock: int
#     id: int
#
#
# items = {
#     i: Item(
#         name='Item#{}'.format(i + 1),
#         price=(i + 1) ** 2,
#         stock=(i + 2) * 10,
#         id=i
#     )
#     for i in range(3)
# }
#
#
# @app.get("/")
# def root() -> dict[str, dict[int, Item]]:
#     return {"items": items}

@app.get("/")
def root():
    return {"message": "This is the root of the project"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)