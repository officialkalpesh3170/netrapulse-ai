from backend.auth_service.models import User
from backend.auth_service.db.base import Base
from backend.auth_service.db.session import engine


print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")