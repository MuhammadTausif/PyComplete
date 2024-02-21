# Example 1: Detecting a Specific Word in User Input

user_message = "I need help with my account"
keyword_position = user_message.find("help")

if keyword_position != -1:
    print("Triggering help response...")
else:
    print("Standard response.")


# Example 2: Extracting a Substring Between Parentheses
    
note = "Remember to update the document (version 2.3)"
start = note.find("(")
end = note.find(")", start)

if start != -1 and end != -1:
    version = note[start+1:end]
    print(f"Document version: {version}")

# Example 3:
password = "user1234secure"
secret_sequence = "secure"

if password.find(secret_sequence) != -1:
    print("Password contains the secret sequence.")
else:
    print("Password is weak.")

# Example 4
filename = "report_2024.xlsx"
extension_start = filename.find(".")
if extension_start != -1:
    extension = filename[extension_start:]
    print(f"File extension: {extension}")
    

# Example 5:
post = "Loving the #sunset at the beach! #vacation"
hashtag_position = post.find("#")

if hashtag_position != -1:
    end_space = post.find(" ", hashtag_position)
    if end_space == -1:  # No space found, hashtag is at the end
        end_space = len(post)
    hashtag = post[hashtag_position:end_space]
    print(f"Found hashtag: {hashtag}")
    