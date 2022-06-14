from telnetlib import STATUS
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix ="/job",
    tags=['Job']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(job: schemas.job, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == job.post_id).first()
#check if posts exists
    if not post:
        raise HTTPException(STATUS==status.HTTP_404_NOT_FOUND, detail = f"Post with id:, {job.post_id} does not exist")
    job_query = db.query(models.Job).filter(
        models.votepost_id == job.post_id, models.Job.user_id == current_user.id)
    found_job = job_query.first()
    if (vote.dir == 1):
        if found_job:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already applied for post {job.post_id}")
        new_job = models.Vote(post_id = job.post_id, ser_id=current_user.id)
        db.add(new_job)
        db.commit()
        return {"message": "successful added vote"}
    else:
        if not found_job:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job does not exist")

        job_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successful deleted words"}