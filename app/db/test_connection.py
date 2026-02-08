from app.db.session import engine


def test_db():
    with engine.connect() as connection:
        print("Database connected successfully")




test_db()