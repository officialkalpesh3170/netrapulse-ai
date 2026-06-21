from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.auth_service.core.config import settings

DATABASE_URL=(
    f"postgresql://{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)
#connection manager fastapi-->engine-->postgresql
engine = create_engine(DATABASE_URL)
#creats database session


SessionLocal =sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

