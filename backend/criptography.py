import math

def cript(message):
    message = message[::-1]
    cripted_message = ""
    message_lists = []

    for i in range(math.ceil(len(message)/2)):
        message_lists.append([])

    for i in range(len(message)):
        message_lists[i//2].append(message[i])
    
    for section in message_lists:
        section = section[::-1]
        for letter in section:
            cripted_message += letter

    return cripted_message


def decript(cripted_message):
    message_lists = []
    decripted_message = ""

    for i in range(math.ceil(len(cripted_message)/2)):
        message_lists.append([])
    
    for i in range(len(cripted_message)):
        message_lists[i//2].append(cripted_message[i])

    for section in message_lists:
        section = section[::-1]
        for letter in section:
            decripted_message += letter

    decripted_message = decripted_message[::-1]
    
    print(decripted_message)

cripted_message = cript("mensagem")

decript(cripted_message)
