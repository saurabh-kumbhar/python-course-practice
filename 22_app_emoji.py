emojis = {
    ":(": "âšī¸",
    ":)": "đ",
    ":D": "đ",
    ":|": "đ",
    ":P": "đ",
    ":*": "đ"
}


while True:
    message = input("> ")

    if message == "exit":
        break

    words = message.split(" ")

    message = ""
    for word in words:
        message += f"{emojis.get(word, word)} "

    print(message)
    print("[exit: to exit]")

