from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()



class Post(BaseModel):
    
    title: str
    content: str
    published:bool = True
    rating: Optional[int] = None
    

my_posts = [ {"title": "title of post" , "content":"content of post 1 " , "id": 1 , "published": True} ,
              {"title": "title of post 2 " , "content":"content of post  2 " , "id": 2 , "published": True} ,
             ]
    
    
    
@app.get("/")
async def root():
    return {"message": "Hello ffrefrefere"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/createPosts")
def create_posts(new_post: Post):
    
    print(new_post.rating)
    print(new_post.dict())
    return {"data": "new post"}

#title str , content str, category