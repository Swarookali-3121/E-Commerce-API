from fastapi import HTTPException,status, Depends
from sqlalchemy.orm import Session
from models import schemas, models
from settings import database
from utils import hash
from utils.jwt_token import verify_token
from utils.exceptions import ErrorHandler


def is_User(user_id: int, db: Session = Depends(database.get_db)):
    try:
        user = db.query(models.User).filter(models.User.user_id == user_id).first()
        if not user:
            return user
    except Exception as hala:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(hala))
    
def create_User(request: schemas.UserSignup, db: Session = Depends(database.get_db)):
    if db.query(models.User).filter(models.User.email == request.email).first():
        ErrorHandler.Conflict("Email already exists")

    hashed_password = hash.Encryption.bcrypt(request.password)

    user_data = request.model_dump(exclude={"password"})
    user_data["password"] = hashed_password

    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # optional but useful if you want to return the created user

    return {"message": "User created successfully"}


def get_All_User(db: Session = Depends(database.get_db),dependencies: Session = Depends(verify_token)):
    user = db.query(models.User).all()
    if not user:
        ErrorHandler.NotFound("No users found")
    return user

def get_User(email: str,db: Session = Depends(database.get_db), dependencies: Session = Depends(verify_token)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        ErrorHandler.NotFound("User not found")

def get_User_BY_ID(user_id: int, db: Session = Depends(database.get_db), dependencies: Session = Depends(verify_token)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        ErrorHandler.NotFound("User not found")
    return user