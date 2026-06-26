from pydantic import BaseModel,Field

class FightCards(BaseModel):
    name:str
    age:int
    
    category:str 
    wins:int
    loss:int