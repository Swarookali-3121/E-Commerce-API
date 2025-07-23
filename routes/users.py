from fastapi import APIRouter,Depends,status
from settings import database
from sqlalchemy.orm import Session
from typing import List
from models import schemas
from utils.jwt_token import verify_token
from handlers.userhandler import create_User, get_All_User, get_User, get_User_BY_ID


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(request: schemas.UserSignup, db: Session = Depends(database.get_db)):
    new_user = create_User(request, db)
    return new_user

@router.get("/getallusers", response_model=List[schemas.ShowAllUser], status_code=status.HTTP_200_OK)
async def get_all_user(db: Session = Depends(database.get_db), dependencies: Session = Depends(verify_token)):
    user = get_All_User(db, dependencies)
    return user

@router.get("/getuser/{email}", response_model=schemas.ShowParticularUser, status_code=status.HTTP_200_OK)
async def get_user_info_by_email(email: str, db: Session = Depends(database.get_db), dependencies: Session = Depends(verify_token)):
    user_details_email = get_User(email, db)
    return user_details_email

@router.get("/getuserbyid/{user_id}", response_model=schemas.ShowParticularUser, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, db: Session = Depends(database.get_db)):
    user_by_id = get_User_BY_ID(user_id, db)
    return user_by_id