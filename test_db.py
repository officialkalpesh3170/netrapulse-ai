from sqlalchemy import text

from backend.auth_service.db.session import engine


try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT version();")
        )

        print("Database Connected Successfully!")
        print(result.fetchone())

except Exception as error:
    print("Database Connection Failed!")
    print(error)