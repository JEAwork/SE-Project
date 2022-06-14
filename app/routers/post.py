from fastapi import Response, status, HTTPException, Depends, APIRouter
from app import oauth2
from .. import models, schemas, oauth2
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import Optional, List
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

#get all posts
@router.get("/", response_model=List[schemas.PostOut])
def get_post(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
limit: int = 10, skip: int = 0, search: Optional[str] = ""): #limit number of posts | skip a number of posts | search 
#sql get all posts code
    #cursor.execute("""SELECT * FROM posts""")
    #posts = cursor.fetchall()
    posts = db.query(models.Post, func.count(models.Job.post_id)).join(models.Job, models.Job.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

#create post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
#create dependency so that user has to be logged in
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#sql create posts code
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
    #                (post.title, post.content, post.published))
    #new_post =  cursor.fetchone()
    #conn.commit()
    new_post = models.Post(owner_id=current_user, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

#see a post
@router.get("/{id}", response_model=schemas.Post)
#create dependency so that user has to be logged in
def get_post(id: int,  db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#sql get post code
    #cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    #post = cursor.fetchone()
    post = db.query(models.Post, func.count(models.Job.post_id)).join(models.Job, models.Job.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
#check if post is not found
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} was not found")
    return post

#delete a post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
#create dependency so that user has to be logged in
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#sql delete a post code
    #cursor.execute("""DELETE FROM posts WHERE id = %s returning * """, (str(id)))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
#check if deleted and display error
    if post == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
         detail= f"post with id: {id} does not exist")
#check if post is the current users
    if post.owner_id != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to perform action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
#updating a post
@router.put("/{id}", response_model=schemas.Post)
#create dependency so that user has to be logged in
def update_post(id: int, updated_post:schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#sql update post code
    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published =%s WHERE id = %s RETURNING *""", 
    #(post.title, post.content, post.published, str(id)))
    #updated_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()
#check if there are post with that number
    if post == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
         detail= f"post with id: {id} does not exist")
#check if post is the current users
    if post.owner_id != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to perform action")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()