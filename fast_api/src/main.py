from fastapi import FastAPI, HTTPException, Query, Path, Depends
from models import MusicForm, Music, Genre, MusicUpdate
from sqlmodel import Session, select
from exceptions.notfound import NotFoundException
from config.database import create_db_and_tables, get_session

# Used to initialize database at the very begining of the program
# As this API is using alembic (migrations) there is no need for that
#https://fastapi.tiangolo.com/advanced/events/?h=life#lifespan
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield

app = FastAPI()

#https://fastapi.tiangolo.com/tutorial/path-params/?h=pydant    
@app.get('/music/{id}', response_model=Music)  
async def get_music_by_id(
    id: int = Path(description="Music Unique Identification"), 
    session: Session = Depends(get_session)
):
    music = session.get(Music, id)
    if(music == None): raise HTTPException(status_code=404)
    return music

#https://fastapi.tiangolo.com/tutorial/query-params/?h=query
@app.get('/music', response_model=list[Music])  
async def get_musics(
    genre: Genre = Query(None, description="Filter by genre"), 
    name: str = Query(None, description="Search by name"),
    session: Session = Depends(get_session)
):
    results = session.exec(select(Music)).all()
    if genre:
        results = [music for music in results if music.genre == genre.value]
    if name: 
        results = [music for music in results if name.lower() in music.name.lower()]

    return results

@app.post('/music', response_model=Music)
async def add_music(form: MusicForm, session: Session = Depends(get_session)):
    new_music = Music(**form.model_dump())
    session.add(new_music)
    session.commit()
    # update music object with post changes (it receives the ID from the database)
    session.refresh(new_music)
    return new_music

@app.put('/music/{id}', response_model=Music)
async def update_music(
    form: MusicUpdate,
    session: Session = Depends(get_session),
    id: int = Path(description="Unique identifier of the music to be updated"),
):
    music = session.get(Music, id)

    if not music:
        raise NotFoundException()

    # copy form fields as a dict to_data
    music_data = form.model_dump(exclude_unset=True)
    # update the fields in the music object model
    music.sqlmodel_update(music_data)
    # re add the music updated
    session.add(music)
    # persist the changes in the database
    session.commit()
    session.refresh(music)
    return music

@app.delete('/music/{id}')
async def delete_music(
    # inject a session dependency
    session: Session = Depends(get_session),
    id: int = Path(description="Unique identifier of the music to be removed"),
):
    music = session.get(Music, id)

    if not music:
        raise NotFoundException()

    session.delete(music)
    session.commit()
    return {"message": f"The music with ID: {id} was succesfully removed!"}