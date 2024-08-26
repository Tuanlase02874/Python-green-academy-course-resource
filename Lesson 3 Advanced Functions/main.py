def main():
    """
    Main function that orchestrates the calling of other functions.
    """
    print("Main function started.")
    result = reply("How are you?")
    print(result)
    print("Main function ended.")

def reply(message):
    """
    Processes a message and returns a response.
    """
    print("Reply function started.")
    response = changePerson(message)
    print("Reply function ended.")
    return response

def changePerson(message):
    """
    Modifies the message and returns a new string.
    """
    print("ChangePerson function started.")
    modified_message = message.replace("you", "yourself")
    print("ChangePerson function ended.")
    return f"Modified message: {modified_message}"

# Call the main function
main()
