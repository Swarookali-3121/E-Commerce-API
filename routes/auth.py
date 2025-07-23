from fastapi import APIRouter, Response, status,Depends
from sqlalchemy.orm import Session
from settings import database
from models import schemas
from fastapi.security import OAuth2PasswordRequestForm
from handlers.authhandler import Login_User, LogOut, Forgot_Password, Reset_Password


router = APIRouter(tags=["Authentication"])

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user_login = Login_User(request, db)
    return user_login

@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(res: Response):
    logout_user = LogOut(res)
    return logout_user

@router.post("/forgot-password", status_code=status.HTTP_200_OK)
async def forgot_password(request: schemas.ForgotPassword, db: Session = Depends(database.get_db)):
    reset_token = Forgot_Password(request, db)
    return reset_token

@router.post("/reset-password", status_code=status.HTTP_200_OK)
async def reset_password(reset_token: str, new_pass:str, db: Session = Depends(database.get_db)):
    reset = Reset_Password(reset_token, new_pass, db)
    return reset