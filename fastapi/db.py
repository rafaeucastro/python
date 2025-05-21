from sqlmodel import create_engine, SQLModel, Session

#https://fastapi.tiangolo.com/tutorial/sql-databases/?h=database
sqlite_file_name = 'fastapi.db'
DATABASE_URL = f'sqlite:///{sqlite_file_name}'

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)