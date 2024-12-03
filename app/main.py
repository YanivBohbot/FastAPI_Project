from fastapi import FastAPI , Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time 



app = FastAPI()



class Post(BaseModel):
    
    title: str
    content: str
    published:bool = True
    rating: Optional[int] = None
    

while True:
    try:
        conn= psycopg2.connect(host='localhost', database='postgres',user='postgres',
                            password='Mollokapi1' , cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database conection sucessfull")
        break
    except Exception as error:
        print("connection failed")
        print("error:",error)
        time.sleep(2)
    
    
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
    cursor.execute("""SELECT * from posts """)
    posts= cursor.fetchall
    print(posts)
    return {"data": my_posts}


@app.post("/createPosts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    
    cursor.execute("""INSERT INTO posts (title, content , published) VALUES (%s,%s,%s) RETURNING 
                   * """ ,(post.title , post.content, post.published))
    
    new_post= cursor.fetchone()
    
    conn.commit()
    
   
    return {"data": "new post"}


@app.get("/posts/{id}")
def get_post(id: int):
    
    cursor.execute("""SELECT * from posts WHERE id= %s""",(str(id),))
    post = cursor.fetchone()
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
    cursor.execute(""""DELETE FROM posts WHERE id = %s  returning *""", (str(id),))
    delete_post = cursor.fetchone()
    conn.commit()
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"posts with id:{id} does not exist")
    
    my_posts.pop(index)
    return Response(status_code= status.HTTP_204_NO_CONTENT) 

    


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
   
    
    cursor.execute(""" UPDATE post SET title =%s , content=%s , published =%s WHERE id= %s RETURNING *""",
                   (post.title, post.content, post.published , str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
   
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"posts with id:{id} does not exist")
    
    
    
    return {'message': updated_post} 

    