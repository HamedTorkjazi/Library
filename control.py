from model import Category,Library,User,engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind = engine)
session = Session()

def add_category(name_category):

    category = Category(name = name_category , number = 0 )

    session.add(category)
    session.commit()


def add_book(bookname , author_name , pages_number , year_ , count , category_name):
    
    category = session.query(Category).filter_by(name = category_name).first()

    book = Library(book_name = bookname , author = author_name , pages = pages_number , year = year_ , read_count = count , category_id = category.id)
    
    session.add(book)
    category.number += 1

    session.commit()


def add_user(first_n , last_n , codemeli , birth_day = None):

    string = str(codemeli)
    if len(string) == 10:

        user = User(f_name = first_n , l_name = last_n , birthday = birth_day , code_meli = codemeli)

        session.add(user)
        session.commit()

    else:
        raise "code_meli must be exactly ten digits long."


def book_transfer(action , codemeli , bookname ):
    
    if action == "add":
        book = session.query(Library).filter_by(book_name = bookname).first()

        book.read_count += 1

        user = session.query(User).filter(User.code_meli == codemeli).first()

        user.book_id = book.id
        session.commit()

    elif action == "remove":

        user = session.query(User).filter(User.code_meli == codemeli).first()
        user.book_id = None
        
        session.commit()

    else:
        raise "Incorrect action, please choose 'add' or 'remove' "


def user_status(codemeli):
    
    user = session.query(User).filter(User.code_meli == codemeli).first()

    if user.book_id:
        print(f"\n\n{user.f_name} {user.l_name} is currently reading a book.\n\n")

    else:
        print(f"\n\n{user.f_name} {user.l_name} has not selected a book to read.\n\n")


def book_status(bookname):
    
    book = session.query(Library).filter_by(book_name = bookname).first()
    users = session.query(User).filter(User.book_id == book.id).all()

    counter = 0
    for user in users:
        counter += 1

    if book :
        print(f"This book has been downloaded {book.read_count} times.\nAnd {counter} people are currently reading this book.")


def remove_book(bookname):
        
    book = session.query(Library).filter_by(book_name = bookname).first()

    category = session.query(Category).filter_by(id = book.category_id).first()
    category.number -= 1

    session.delete(book)
    session.commit()


def remove_user(codemeli):

    user = session.query(User).filter(User.code_meli == codemeli).first()
    session.delete(user)

    session.commit()


# add_category(name_category = "Novel")

# add_book("1998" , "George Orwell" , 423 , 1930 , 0 , category_name = "Novel" )

# add_user("Hamed" , "Torkjazi" , codemeli="6125451220" , birth_day = date(2004,8,1))

# book_transfer("add" , "6125451220" , "1998")

# book_transfer("remove" , "6125451220" , "1998")

# user_status("6125451220")

# book_status("reza")

# remove_book("1998")

# remove_user("6125451220")




session.close()


# category = session.query(Category).filter_by(name = "Novel").first()
# session.delete(category)
# session.commit()