from backend.auth_service.db.session import SessionLocal
from backend.auth_service.repositories.user_repository import UserRepository


db = SessionLocal()

try:

    user = UserRepository.create_user(
        db=db,
        email="kalpesh1@example.com",
        full_name="Kalpesh Patil",
        password_hash="dummy_hash"
    )

    print("User Created!")
    print(user.id)

finally:
    db.close()