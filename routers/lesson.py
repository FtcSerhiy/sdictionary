from fastapi import APIRouter

router = APIRouter()

@router.get('/get-alls')
async def helloWorld():
    return 'ok'