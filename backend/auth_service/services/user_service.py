from sqlalchemy.orm import Session

from backend.auth_service.repositories.user_repository import UserRepository
from backend.auth_service.schemas.user_schema import UserCreate


class UserService:

    @staticmethod
    def create_user(
        db: Session,
        user_data: UserCreate
    ):

        existing_user = UserRepository.get_user_by_email(
            db=db,
            email=user_data.email
        )

        if existing_user:
            raise ValueError(
                "Email already registered"
            )

        user = UserRepository.create_user(
            db=db,
            email=user_data.email,
            full_name=user_data.full_name,
            password_hash=user_data.password,
        )

        return user