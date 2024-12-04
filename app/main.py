from fastapi import Depends, FastAPI , Response , status , HTTPException
from fastapi.params import Body
from typing import Optional
from . import models , schemas
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from passlib.context import CryptContext
from . import models
from .database import engine
from .routers import post, user, auth, vote

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
models.Base.metatdata.create_All(bingd=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}

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
    

    
@app.get("/")
async def root():
    return {"message": "Hello ffrefrefere"}



@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    
    db.query(models.Post).all()
    return {"data": posts}



@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * from posts """)
    # posts= cursor.fetchall
    posts = db.query(models.Post).all()
    print(posts)
    return {"data": posts}


@app.post("/createPosts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    
    # cursor.execute("""INSERT INTO posts (title, content , published) VALUES (%s,%s,%s) RETURNING 
    #                * """ ,(post.title , post.content, post.published))
    # new_post= cursor.fetchone()
    # conn.commit()
    
   
    
    models.Post()
    
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

    