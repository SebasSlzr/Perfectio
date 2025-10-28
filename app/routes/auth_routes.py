from app.database import get_db
router = APIRouter()

### Router.post("/register")
@router.post("/register")
async def register_user(db: AsyncSession = Depends(get_db)):
    return {"msg": "Usuario registrado exitosamente"}

### Router.post("/login")
@router.post("/login")
async def login_user(db: AsyncSession = Depends(get_db)):
    return {"msg": "Login exitoso", "access_token": "token_jwt_aqui"}

### Router.post("/logout")
@router.post("/logout")
async def logout_user(db: AsyncSession = Depends(get_db)):
    return {"msg": "Logout exitoso"}