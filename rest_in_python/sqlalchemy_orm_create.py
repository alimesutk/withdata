from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://admin:secret@localhost:5432/postgres')
Base = declarative_base()

class AlbumsModel(Base):
    """Data model albums."""
    __tablename__ = 'albums'
    __table_args__ = {'schema': 'typicode'}

    userid = Column(Integer, primary_key=True, nullable=False)
    id = Column(Integer, nullable=False)
    title = Column(String(500), nullable=False)


Base.metadata.create_all(engine)