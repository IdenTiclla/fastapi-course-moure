from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="juan", surname="juancho", url="htpps://juancho.com", age=20),
         User(id=2, name="cristino", surname="cr7", url="htpps://cris.com", age=21),
         User(id=3, name="messi", surname="pulga", url="htpps://messi.com", age=22),
         User(id=4, name="roberto", surname="robert", url="htpps://robertlewandowski.com", age=23)]

@app.get("/users")
async def usersjson():
    # return [{"name": "illo", "surname": "juan", "url": "http://users.com"}]
    return users_list

# path parameters
@app.get('/user/{id}')
async def get_specific_user(id: int):
    return search_user(id)

# query parameters
@app.get('/user/')
async def get_query_user(id: int):
    return search_user(id)
    
@app.post('/users')
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "usuario ya esta registrado."}
    else:
        users_list.append(user)
        return user

def search_user(id:int):
    users = filter(lambda x: x.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "can't find that user", "status": 404}