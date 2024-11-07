from fastapi import FastAPI, Depends,Form, Request, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import wikipediaapi
from auto_tag import get_tags_from_textrazor
from database import SessionLocal, engine
from models import FavoriteArticle, Base
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app and Wikipedia API with a user agent
app = FastAPI()
wiki = wikipediaapi.Wikipedia(language='en', user_agent="LokiTheGod")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class Article(BaseModel):
    title: str
    summary: str
    

class SearchKeyword(BaseModel):
    keyword: str

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": None, "summary": None})

@app.post("/search/", response_class=HTMLResponse)
async def search_articles(request: Request, keyword: str = Form(...)):
    page = wiki.page(keyword)
    print(page)
    
    if not page.exists():
        return templates.TemplateResponse("index.html", {
            "request": request,
            "title": None,
            "summary": "Article not found. Please try another keyword."
        })
    
    # Send the title and summary to the template
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": page.title,
        "summary": page.summary[0:1000],  # Show only the first 1000 characters
        "keyword": keyword  # Pass keyword for the add-to-favorites form
    })
# Auto-tagging the article's summary

# Save favorite article
@app.post("/favorites/")
async def save_favorite(
    request: Request, 
    keyword: str = Form(...),
    db: Session = Depends(get_db)
):
    # Fetch article data from Wikipedia API based on the keyword
    article_data = wiki.page(keyword)
    
    if not article_data:
        raise HTTPException(status_code=404, detail="Article not found")
    
    title = article_data.title
    summary = article_data.summary[0:1000]
    
    # Check if the article already exists in favorites
    db_article = db.query(FavoriteArticle).filter(FavoriteArticle.title == title).first()
    if db_article:
         return templates.TemplateResponse("index.html", {
                "request": request,
                "article_already_favorite": True,  # Add a flag for the popup message
                "title": title,
                "summary": summary,
            })
    
    # Auto-tagging the article's summary
    tags = get_tags_from_textrazor(summary)
    
    # Create a new favorite article entry
    favorite_article = FavoriteArticle(
        title=title,
        summary=summary,
        tags=tags
    )
    db.add(favorite_article)
    db.commit()
    db.refresh(favorite_article)
    
    # Return to the main template with a success message
    return templates.TemplateResponse("index.html", {
        "request": request,
        "favorite_added": True,
        "article": favorite_article
    })
# Retrieve all favorite articles
@app.get("/favorites/", response_class=HTMLResponse)
async def get_favorites(request: Request, db: Session = Depends(get_db)):
    favorites = db.query(FavoriteArticle).all()
    return templates.TemplateResponse("favorites.html", {"request": request, "favorites": favorites})
