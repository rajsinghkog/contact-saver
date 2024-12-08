from fastapi import FastAPI, Depends, Request, Form, status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from owndatabase import SessionLocal, engine
import model  # make sure the import refers to the correct model2 file


model.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get("/")
async def home(req: Request, db: Session = Depends(get_db)):
    contactlist = db.query(model.ContactList).all()  # Use ContactList model
    return templates.TemplateResponse("contactlist.html", { "request": req, "contactlist": contactlist })

@app.post("/add")
def add(req: Request, title: str = Form(...), number: str = Form(...), db: Session = Depends(get_db)):
    # Creating a new contact using the ContactList model
    new_contact = model.ContactList(name=title, phone=number)  # Use ContactList
    db.add(new_contact)
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
@app.get("/delete/{todo_id}")
def add(req: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.ContactList).filter(model.ContactList.id == todo_id).first()
    db.delete(todo)
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update/{todo_id}")
def add(req: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.ContactList).filter(model.ContactList.id == todo_id).first()
    
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
