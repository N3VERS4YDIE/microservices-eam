from app.database import BaseSchema, engine


def init_db():
    BaseSchema.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
