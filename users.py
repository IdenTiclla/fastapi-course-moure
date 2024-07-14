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
    
@app.put('/users')
async def update_user(user: User):
    for saved_user in users_list:
        if saved_user.id == user.id:
            saved_user.name = user.name
            saved_user.surname = user.surname
            saved_user.url = user.url
            saved_user.age = user.age
            return user
        
    return {"error": "user not found."}

@app.delete('/users/{id}')
async def delete_user(id: int):
    for saved_user in users_list:
        if saved_user.id == id:
            users_list.remove(saved_user)
            return {"msg": "user deleted successfully."}
    return {"msg": "user wasn't found."}

def search_user(id:int):
    users = filter(lambda x: x.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "can't find that user", "status": 404}