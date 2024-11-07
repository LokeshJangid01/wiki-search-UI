from sqlalchemy import Column, Integer, String
from database import Base
from typing import List

class FavoriteArticle(Base):
    __tablename__ = "favorite_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(String)
    tags = Column(String)  # Store tags as a comma-separated string
    
