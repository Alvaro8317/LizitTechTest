from fastapi import APIRouter

router = APIRouter()


@router.get('/items')
def get_items():
    pass
