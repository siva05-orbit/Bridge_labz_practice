from fastapi import FastAPI
from card import FightCards
app = FastAPI()



items = [FightCards(name="Volk",age=40,category="featherweight",wins=17,loss=5),
            FightCards(name="Ilia",age=32,category="lightweight",wins=19,loss=0),
            FightCards(name="Olivera",age=43,category="lightweight",wins=32,loss=10),
            FightCards(name="JonBones",age=42,category="HeavyWeight",wins=29,loss=0)
            ]
@app.get("/")
async def cards_show():
    return items

@app.get("/{name}")
async def figher(name:str):
    for item in items:
        if item.name == name:
            return item

@app.get("/goat")
async def goat_list():
    goats = []
    for item in items:
        if item.loss == 0:
            goats.append(item)
    return goats
            

@app.post("/edit")
async def add_fighters(profile:FightCards):
    items.append(profile)
    return profile

@app.put("/edit")
async def update_fighters(profile:FightCards,wins:int):
    for i in range(len(items)):
        if items[i].wins == wins:
            items[i] = profile
    return "Update Successful"

@app.patch("/edit/{name}")
async def partial_update(name:str,age:int):
    for i in range(len(items)):
       if items[i].name == name:
           items[i].age = age
    return ("Update Done")

