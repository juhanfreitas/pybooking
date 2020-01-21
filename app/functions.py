import csv
import datetime

from criptography import cript, decript
from PyQt5.QtWidgets import QMessageBox


def signup(name, phone, email, username, password):
    '''
    A function that store the new user's data in the database.
  
        Parameters: 
            name (str): A string that contains the new user's name.
            phone (str): A string that contains the new user's phone.
            email (str): A string that contains the new user's email.
            username (str): A string that contains the new user's username.
            password (str): A string that contains the new user's password.    
    '''

    exists = False
    
    users_list = user_database_reader("databases/users.csv")
    for user in users_list:
        if username == user[3]:
            exists = True

    if not exists:
        new_user = [cript(name), cript(phone), cript(email), cript(username), cript(password)]
        csv.register_dialect("my_dialect", delimiter=",", lineterminator="\n")

        with open("databases/users.csv", "a") as csv_file:
            csv_writer = csv.writer(csv_file, dialect="my_dialect")
            csv_writer.writerow(new_user)

        with open("databases/current_section.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, dialect="my_dialect")
            csv_writer.writerow(["Name", "Phone", "Email", "Username", "Password"])
            csv_writer.writerow(new_user)
        
        return exists

    else:
        show_message("Erro", QMessageBox.Critical, "Nome de usuário indisponível!")


def login(screen):
    logged = False
    users = user_database_reader("databases/users.csv")
        
    if screen.campousuario.text() == "" or screen.camposenha.text() == "":
        show_message("Aviso", QMessageBox.Warning, "Um ou mais campos não foram preenchidos")
        
    for user in users:
        if screen.campousuario.text() == user[3] and screen.camposenha.text() == user[4]:
            user_data = user
            user_data = [
                cript(user_data[0]),
                cript(user_data[1]),
                cript(user_data[2]),
                cript(user_data[3]),
                cript(user_data[4])
            ]
            logged = True
                
    if logged:
        csv.register_dialect("my_dialect", delimiter=",", lineterminator="\n")
        with open("databases/current_section.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, dialect="my_dialect")
            csv_writer.writerow(["Name", "Phone", "Email", "Username", "Password"])
            csv_writer.writerow(user_data)

        return logged

    else:
        show_message("Erro", QMessageBox.Critical, "Usuário ou senha inválida!")


def book_database_reader(database):
    '''
    A function that read the books database.
  
        Parameters: 
            database (str): A string that contains the database directory.
          
        Returns: 
            books_list (list): A list that contains all the database books.    
    '''

    books_list = []

    csv_file = open(database)
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        book_name, release_date, author, copies, filename = row
        books_list.append([
            book_name,
            release_date,
            author,
            int(copies),
            filename
        ])

    csv_file.close()

    return books_list


def rewrite_books_database(book_list):
    csv.register_dialect("my_dialect", delimiter=",", lineterminator="\n")
    with open("databases/books.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, dialect="my_dialect")

        for book in book_list:
            if book_list.index(book) == 0:
                csv_writer.writerow(["Book name", "Release date", "Author", "Copies"])

            csv_writer.writerow(book)


def take_user_borrowed_books(database, from_user=False):
    borrow_list = []
    current_user = user_database_reader("databases/current_section.csv")

    csv_file = open(database)
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        book_name, release_date, author, user, borrow_date, return_date = row
        if from_user:
            if user == current_user[0][0]:
                borrow_list.append([
                    book_name,
                    release_date,
                    author,
                    user,
                    datetime.datetime.strptime(borrow_date , '%Y-%m-%d').date(),
                    datetime.datetime.strptime(return_date, '%Y-%m-%d').date()
                ])
        else:
            borrow_list.append([
                    book_name,
                    release_date,
                    author,
                    user,
                    datetime.datetime.strptime(borrow_date , '%Y-%m-%d').date(),
                    datetime.datetime.strptime(return_date, '%Y-%m-%d').date()
                ])
    csv_file.close()

    return borrow_list


def user_database_reader(database):
    '''
    A function that read the books database.
  
        Parameters: 
            database (str): A string that contains the database directory.
          
        Returns: 
            users_list (list): A list that contains all the database users.    
    '''

    users_list = []

    csv_file = open(database)
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        name, phone, email, username, password = row
        users_list.append([
            decript(name),
            decript(phone),
            decript(email),
            decript(username),
            decript(password)
        ])
    
    csv_file.close()

    return users_list


def call_screen(actual_screen, called_screen, hide=True):
    actual_screen.screen = called_screen
    actual_screen.screen.setupUi()
    actual_screen.screen.show()
    if hide:
        actual_screen.hide()


def show_message(message_title, message_icon, message_text):
    from PyQt5 import QtGui
    msg = QMessageBox()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("resources/closed_book_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setWindowTitle(message_title)
    msg.setIcon(message_icon)
    msg.setText(message_text)
    msg.exec()


def search_books(book_name):
    books = book_database_reader("databases/books.csv")
    found_books = []

    for book in books:        
        if book_name.lower() in book[0].lower():
            found_books.append(book)

    if book_name == "":
        return books

    else:
        return found_books


def borrow_book(borrowed_book):
    borrowed_book = borrowed_book[0:-2]
    books = book_database_reader("databases/books.csv")
    user = user_database_reader("databases/current_section.csv")
    user_borrowed_books = take_user_borrowed_books("databases/borrowed_books.csv", from_user=True)

    for book in books:
        if borrowed_book[0] == book[0]:
            if book[3] >= 1:
                sold_out_book = False
                book[3] -= 1
                break

            else: sold_out_book = True
    
    if not sold_out_book:
        rewrite_books_database(books)

        csv.register_dialect("my_dialect", delimiter=",", lineterminator="\n")

        current_date = datetime.date.today()
        return_date = current_date + datetime.timedelta(days=14)

        borrowed_book.append(user[0][0])
        borrowed_book.append(current_date)
        borrowed_book.append(return_date)

        if len(user_borrowed_books) < 3:
            if borrowed_book not in user_borrowed_books:
                with open("databases/borrowed_books.csv", "a") as csv_file:
                    csv_writer = csv.writer(csv_file, dialect="my_dialect")
                    csv_writer.writerow(borrowed_book)

                show_message("Sucesso", QMessageBox.Information, "O livro é todo seu, devolva-o em duas semanas.")

            else:
                show_message("Você é corno", QMessageBox.Warning, "Você já pegou um exemplar dessa obra.")
        else:
            show_message("Você é corno", QMessageBox.Warning, "Você já pegou as 3 obras limite.")

    elif sold_out_book:
        show_message("Esgotado", QMessageBox.Warning, "Todos os exemplares da obra foram pegos.")


def return_book(returned_book):
    books = book_database_reader("databases/books.csv")
    borrowed_books = take_user_borrowed_books("databases/borrowed_books.csv")

    for book in books:
        if returned_book[0] == book[0]:
            book[3] += 1
            break

        else: pass
    
    for book in borrowed_books:
        if returned_book[0] == book[0]:
            borrowed_books.remove(book)
            break
        else: pass

    rewrite_books_database(books)

    csv.register_dialect("my_dialect", delimiter=",", lineterminator="\n")

    with open("databases/borrowed_books.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, dialect="my_dialect")
        if len(borrowed_books) > 0:
            for book in borrowed_books:
                if borrowed_books.index(book) == 0:
                    csv_writer.writerow(["Book name", "Release date", "Author", "User", "Borrow Date", "Return Date"])

                csv_writer.writerow(book)

        else:
            csv_writer.writerow(["Book name", "Release date", "Author", "User", "Borrow Date", "Return Date"])

    show_message("Sucesso", QMessageBox.Information, "O livro foi devolvido.")
