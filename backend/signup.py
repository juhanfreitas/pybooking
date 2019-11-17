import csv

users = {username: "juhan", email: "juhanfreitas@gmail.com", password: "saas"}

print(users.keys())
'''
with open ("users.csv", "w") as file:
    writer = csv.Dictreader(file, users.keys())
    reader.readlines()

def signup(username, email, password):'''
    