from controllers.greettings_cnt import GreetingCont
from fastapi import APIRouter
router = APIRouter()

greettings_cnt =   GreetingCont("greetings cnt")
@router.get("/hello", tags=["greettings"], summary="saluer un utilisateur")
async def hello():
    return greettings_cnt.say_hello

@router.get("/bye", tags=["greettings"], summary="dire aurevoir à utilisateur")
async def hello():
    return greettings_cnt.say_bye