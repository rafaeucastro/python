from fastapi import FastAPI, HTTPException, Query, Path, Depends
from models import MusicForm, Music, Genre, MusicUpdate
from contextlib import asynccontextmanager
from db import create_db_and_tables, get_session
from sqlmodel import Session, select
from exceptions.notfound import NotFoundException

#https://fastapi.tiangolo.com/advanced/events/?h=life#lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

music_list = [
    Music(id=0, name="Butter", artist="BTS", genre=Genre.K_POP),
    Music(id=1, name="Seven", artist="Jungkook feat. Latto", genre=Genre.K_POP),
    Music(id=2, name="As It Was", artist="Harry Styles", genre=Genre.POP),
    Music(id=3, name="Blinding Lights", artist="The Weeknd", genre=Genre.POP),
    Music(id=4, name="Levitating", artist="Dua Lipa", genre=Genre.POP),
    Music(id=5, name="On The Ground", artist="Rosé", genre=Genre.K_POP),
    Music(id=6, name="Stay", artist="The Kid LAROI & Justin Bieber", genre=Genre.POP),
    Music(id=7, name="Starlight", artist="Martin Garrix & DubVision", genre=Genre.ELECTRONIC),
    Music(id=8, name="You", artist="Regard, Troye Sivan, Tate McRae", genre=Genre.ELECTRONIC),
    Music(id=9, name="Titanium", artist="David Guetta feat. Sia", genre=Genre.ELECTRONIC),
]

#https://fastapi.tiangolo.com/tutorial/path-params/?h=pydant    
@app.get('/music/{id}', response_model=Music)  
async def get_music_by_id(
    id: int = Path(description="Music Unique Identification"), 
    session: Session = Depends(get_session)
):
    music = session.get(Music, id)
    if(music == None): raise HTTPException(status_code=404)
    return music

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

    music_data = form.model_dump(exclude_unset=True)
    music.sqlmodel_update(music_data)
    session.add(music)
    session.commit()
    session.refresh(music)
    return music

@app.delete('/music/{id}')
async def delete_music(
    session: Session = Depends(get_session),
    id: int = Path(description="Unique identifier of the music to be removed"),
):
    music = session.get(Music, id)

    if not music:
        raise NotFoundException()

    session.delete(music)
    session.commit()
    return {"message": f"The music with ID: {id} was succesfully removed!"}