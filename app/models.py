from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Post(Base):
    __tablename__="posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content =  Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, 
                        server_default=text('Now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
    job_status = Column(String, server_default='Available', nullable=False)


class User(Base):
    __tablename__="users"
    email = Column(String, nullable = False, unique=True)
    password = Column(String, nullable = False)
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, 
                        server_default=text('Now()'))
    phone_number = Column(String)
    course=Column(String, nullable=False)
    
class Job(Base):
    __tablename__="job"
    user_id = Column(Integer, ForeignKey(
        "user.id", ondelette="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelette="CASCADE"), primary_key=True)

