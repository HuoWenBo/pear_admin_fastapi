from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from pear_admin_fastapi.db.dependencies import get_db_session
from pear_admin_fastapi.db.models.user import User
from pear_admin_fastapi.settings import settings
from pear_admin_fastapi.utils.auth import get_current_user, authenticate_user, create_access_token, get_password_hash
from pear_admin_fastapi.web.api.users.schema import UserCreate, UserRead

router = APIRouter()


@router.post(
    '/register'
)
async def register(user: UserCreate, session: AsyncSession = Depends(get_db_session)) -> UserRead:
    user = User(**user.model_dump())
    user.password = get_password_hash(user.password)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    user = UserRead.model_validate(user)
    return user


@router.get(
    '/me'
)
async def me(user: User = Depends(get_current_user)) -> UserRead:
    return UserRead.model_validate(user)


@router.post(
    '/token'
)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_db_session)):
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# router.include_router(
#     api_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )
#
# router.include_router(
#     api_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )
#
# router.include_router(
#     api_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["auth"],
# )
#
# router.include_router(
#     api_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )
#
# router.include_router(
#     api_users.get_auth_router(auth_jwt),
#     prefix="/auth/jwt",
#     tags=["auth"],
# )
