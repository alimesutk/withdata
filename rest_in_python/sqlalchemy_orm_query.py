from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://admin:secret@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class AlbumsModel(Base):
    """Data model albums."""
    __tablename__ = 'albums'
    __table_args__ = {'schema': 'typicode'}

    userid = Column(Integer, primary_key=True, nullable=False)
    id = Column(Integer, nullable=False)
    title = Column(String(500), nullable=False)


# CREATE TABLE
Base.metadata.create_all(engine)

# DROP TABLE
Base.metadata.drop_all(engine)

# SELECT (GET)
result = session.query(AlbumsModel).filter(AlbumsModel.userid == 3)
[print('UserId:', row.userid, 'Id:', row.id, 'Title:', row.title) for row in result]

# INSERT (POST)
session.add(AlbumsModel(userid=1, id=4, title='mesut'))

# UPDATE (PUT OR PATCH)
session.query(AlbumsModel).filter(AlbumsModel.userid == 2).update({AlbumsModel.id: 3}, synchronize_session=False)

# DELETE (DELETE)
session.query(AlbumsModel).filter(AlbumsModel.userid == 2).delete()

# DELETE ALL
session.query(AlbumsModel).delete()

# Query Samples
print('\n', session.query(AlbumsModel).options())
print('\n', session.query(AlbumsModel).count())
print('\n', session.query(AlbumsModel).get_execution_options())

session.commit()
session.close()
