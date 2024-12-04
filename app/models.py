from .database import Base
from sqlalchemy import Column , Integer ,String,boolean
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import TIMESTAMP

from typing import Annotated




# table that create a Post Model in the Db 
# with all the columns
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key =True ,nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False , server_default= text('now()') )
    
    
    
# table that create a User Model in the Db     
# with all the columns
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
# table that create a Vote Model in the Db     
#  with ForeignKeys from User Table and Post table
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)
