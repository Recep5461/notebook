from fastapi import FastAPI
from pydantic import BaseModel

from db_fonks import get_user_id, user_ekle, user_sil, not_ekle, not_sil, notes_getir, not_guncelle

app = FastAPI()

class Login(BaseModel):
    user:str
    passw:str

class User_Ekle(BaseModel):
    user:str
    passw:str

class Not_Ekleme(BaseModel):
    user_id:int
    title:str
    content:str

class Not_Guncelle(BaseModel):
    not_id:int
    guncel_baslik:str
    guncel_not:str

class Not_and_User_Silme(BaseModel):
    not_or_user_id:int
   
# ////////////////////////////////////////////////////////////////////////////
#                        ___ user işlemleri ___

@app.post("/user_ara")
def home(UserData: Login):
    return {"status":get_user_id(UserData.user, UserData.passw)}

@app.post("/user_ekle")
def user_ekleme(user_data: User_Ekle):
    user_ekle(
        user_data.user,
        user_data.passw
    )
    return {"status": "User Eklendi!"}

@app.post("/user_sil")
def user_silme(user_data: Not_and_User_Silme):
    user_sil(
        user_data.not_or_user_id,
    )
    return {"status": "User silindi"}
# /////////////////////////////////////////////////////////////////////////////
#                        ___ not işlemlei ___

@app.get("/notlari_getir")
def home(uid: str):
    return {"status": notes_getir(uid)}

@app.post("/not_ekle")
def not_ekleme(not_data: Not_Ekleme):
    not_ekle(
        not_data.user_id,
        not_data.title,
        not_data.content
    )
    return {"status": "Notlar eklendi"}

@app.post("/not_silme")
def not_silme(not_data: Not_and_User_Silme):
    not_sil(
        not_data.not_or_user_id,
    )
    return {"status": "Not silindi"}

@app.post("/not_guncelle")
def not_guncelleme(not_data: Not_Guncelle):
    not_guncelle(
        not_data.not_id,
        not_data.guncel_baslik,
        not_data.guncel_not
    )
    return {"status": "Not güncellendi"}



# ////////////////////////////////////////////////////////////////////////////////
#                              ___ Aktif Mi ___
@app.get("/aktifmi")
def home():
    return {
        "status": f"Online NoteBook API aktif!"
    }
