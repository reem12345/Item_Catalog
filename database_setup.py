from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Book(Base):
    __tablename__ = 'book'

    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)
    file_link = Column(String(250))
    picture = Column(String(250))
    author = Column(String(80), nullable=False)
    yearOfEmission = Column(String(10))
    numOfPage = Column(String(50))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'file_link': self.file_link,
            'picture': self.picture,
            'author': self.author,
            'yearOfEmission': self.yearOfEmission,
            'numOfPage': self.numOfPage
        }


engine = create_engine('postgresql://catalog:password@localhost/catalog')


Base.metadata.create_all(engine)
