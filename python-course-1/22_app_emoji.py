emojis = {
    ":(": "☹️",
    ":)": "🙂",
    ":D": "😀",
    ":|": "😐",
    ":P": "😛",
    ":*": "😘"
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

