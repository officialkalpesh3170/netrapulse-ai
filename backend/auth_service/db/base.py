from sqlalchemy.orm import DeclarativeBase


# every model will inherit from this
#SQLAlchemy provides a special parent class.


class Base(DeclarativeBase):
    pass

#from backend.auth_service.models.user import User

#Blueprint Manager