from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://admin:secret@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

class AlbumsModel(Base):
    """Data model albums."""
    __tablename__ = 'albums'
    __table_args__ = {'schema': 'typicode'}

    userid = Column(Integer, primary_key=True, nullable=False)
    id = Column(Integer, nullable=False)
    title = Column(String(500), nullable=False)


#Base.metadata.create_all(engine)

result = session.query(AlbumsModel).all()

for row in result:
   print ("UserId: ", row.userid, "Id:", row.id, "Title:", row.title)

print('\n', session.query(AlbumsModel).options())
print('\n', session.query(AlbumsModel).count())
print('\n', session.query(AlbumsModel).filter)