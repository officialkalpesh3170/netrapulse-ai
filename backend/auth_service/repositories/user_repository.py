from sqlalchemy.orm import Session
#Database se baat karne ka ek middleman

from backend.auth_service.models.user import User
class UserRepository:

    @staticmethod
    def create_user(
        db:Session,
        email:str,
        full_name:str,
        password_hash:str,
        role:str ="analyst"

    )->User:
        user=User(
            email=email,
            full_name=full_name,
            password_hash=password_hash,
            role=role
        ) 
        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def get_user_by_email(
        db:Session,
        email:str
    )->User | None:
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )