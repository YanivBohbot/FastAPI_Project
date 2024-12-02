from fastapi import FastAPI , Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel
from random import randrange


app = FastAPI()



class Post(BaseModel):
    
    title: str
    content: str
    published:bool = True
    rating: Optional[int] = None
    

my_posts = [ {"title": "title of post" , "content":"content of post 1 " , "id": 1 , "published": True} ,
              {"title": "title of post 2 " , "content":"content of post  2 " , "id": 2 , "published": True} ,
             ]
    
def find_post(id: int):
    return {"data": 2}
    
@app.get("/")
async def root():
    return {"message": "Hello ffrefrefere"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/createPosts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    
    print(post)
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000)
    my_posts.append(post_dict)
    return {"data": "new post"}


@app.get("/posts/{id}")
def get_post(id: int, reponse: Response):
    
    post = find_post(id)
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not fond")
      
    return {"post_detail": post}



@app.get("/posts/latest")
def get_latest_posts():
    my_posts[len(my_posts)-1]
    return {"details":"post"}



def find_index_post(id):
    
    for post in my_posts:
        if post['id'] == id:
            return post

@app.delete("/posts/{id}" ,status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #deleteing post
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"posts with id:{id} does not exist")
    
    my_posts.pop(index)
    return Response(status_code= status.HTTP_204_NO_CONTENT) 

    


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    #deleteing post
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"posts with id:{id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_post[index] = post_dict
    
    return {'message': 'coucou'} 

    