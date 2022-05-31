def get_emojis(input_message):
    emojis = {
        ":(": "☹️",
        ":)": "🙂",
        ":D": "😀",
        ":|": "😐",
        ":P": "😛",
        ":*": "😘",
        ":O": "😯"
    }
    words = input_message.split(" ")
    output_message = ""
    for word in words:
        output_message += f"{emojis.get(word, word)} "
    return output_message


while True:
    message = input("> ")
    if message == "exit":
        break
    result = get_emojis(message)
    print(result)

# print(emojis(input("> ")))  # Shortcut
