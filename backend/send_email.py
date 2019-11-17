import csv

books = list()
wait_list = list()

with open("books.csv", "r") as file:
    for line in file:
        books.append(line[0:-1].split(","))

with open("wait_list.csv", "r") as file:
    for line in file:
        wait_list.append(line[0:-1].split(","))

def devolver_livro():
    livro = input("Que livro?")
    for book in books:
        if book[0] == livro:
            book[1] = "disponivel"
            search_waitlist(livro)

def search_waitlist(book):
    for entry in wait_list:
        if entry[1] == book:
            send_email(entry)

def send_email(entry):
    print(f"Email enviado para {entry[2]}")

def reservar():
    name = input("seu nome:")
    livro = input("livro:")
    email = input("email:")
    wait_list.append([name, livro, email])

reservar()
reservar()
devolver_livro()
devolver_livro()