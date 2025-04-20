from typing import Dict, List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    stock: int
    id: int


items = {
    i: Item(
        name='Item#{}'.format(i + 1),
        price=(i + 1) ** 2,
        stock=(i + 2) * 10,
        id=i
    )
    for i in range(3)
}


@app.get("/items")
async def items__get_all(max_price: float = None) -> Dict[str, List[Item]]:
    if max_price is not None:
        found = [item for item in items.values() if item.price <= max_price]
        return {"items": found}
    return {"items": list(items.values())}


@app.get("/items/{item_id}")
async def items__get_by_id(item_id: int) -> Dict[str, Item]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"items": items[item_id]}


@app.put("/items")
async def items__put(item: Item) -> Dict[str, str]:
    items[item.id] = item
    return {"message": "Success"}


@app.patch("/items/{item_id}")
async def items__patch(item_id: int, item: Item) -> Dict[str, str]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"message": "Success"}


@app.delete("/items/{item_id}")
async def items__delete(item_id: int) -> Dict[str, str]:
    if item_id in items:
        del items[item_id]
        return {"message": "Success"}
    else:
        return {"message": "Item not found"}


@app.get("/")
async def index():
    return {"message": "This is the root of the project.  Go to /docs."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)