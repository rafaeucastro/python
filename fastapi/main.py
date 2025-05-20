from fastapi import FastAPI, HTTPException, Query, Path, Body
from music import MusicForm, Music, Genre
from typing import Optional

api = FastAPI()

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
    
@api.get('/music/{id}', response_model=Music)  
async def get_music_by_id(id: int = Path(description="music unique identification")):
    music = next((m for m in music_list if m.id == id), None)
    if(music == None): raise HTTPException(status_code=404)
    return music

@api.get('/music', response_model=list[Music])  
async def get_music_by_genre_and_name(
    genre: Genre = Query(None, description="Filter by genre"), 
    name: str = Query(None, description="Search by name")
):
    results = music_list
    if genre:
        results = [music for music in results if music.genre == genre.value]
    if name: 
        results = [music for music in results if name.lower() in music.name.lower()]

    return results

@api.post('/music', response_model=Music)
async def add_music(form: MusicForm):
    global next_id
    next_id = 10
    new_music = Music(id=next_id, **form.model_dump())
    music_list.append(new_music)
    return form