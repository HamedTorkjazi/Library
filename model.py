from sqlalchemy import create_engine, Column, Integer, String,ForeignKey , Date
from sqlalchemy.orm import declarative_base, relationship

Database_url ='postgresql+psycopg://hamed:1234qwer@localhost/library'

engine = create_engine(Database_url,echo=True)

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer , primary_key = True)
    name = Column(String, unique = True, nullable = False)
    number = Column(Integer)

    library = relationship("Library" , back_populates = "category")


class Library(Base):
    __tablename__ = "library"

    id = Column(Integer , primary_key = True)
    book_name = Column(String, unique = True)
    author = Column(String, unique = True)
    pages = Column(Integer, nullable = False)
    year = Column(Integer, nullable = False)
    read_count = Column(Integer)
    category_id  = Column(Integer ,ForeignKey('categories.id'))


    category = relationship("Category" , back_populates = "library") 

    user = relationship("User", back_populates = "book")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key = True)
    f_name = Column(String, nullable = False)
    l_name = Column(String, nullable = False)
    birthday = Column(Date, nullable = True)
    code_meli = Column(String, unique = True , nullable = False)
    book_id = Column(Integer , ForeignKey('library.id'))

    book = relationship("Library" , back_populates = "user")



