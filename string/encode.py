# Example 0

message = "Python 🐍 is awesome!"
encoded_message = message.encode('utf-8')
print(encoded_message)

# Example 1: Encoding for Web URLs
title = "Café & Bistro – Your Go-To Place!"
encoded_title = title.encode('utf-8').hex()
url_safe_title = f"https://example.com/articles/{encoded_title}"
print(url_safe_title)

# Example 2: Secure password storage
password = "P@ssw0rd!"
encoded_password = password.encode('utf-8')
# This encoded_password can now be hashed securely
print(encoded_password)

# Example 3: Data Serialization for Network Transmission
data = "Data with special characters: £€$¥"
encoded_data = data.encode('utf-8')
# This encoded_data can now be transmitted over a network
print(encoded_data)

# Handling Emojies
comment = "Great job team! 👏👏🥳"
encoded_comment = comment.encode('utf-8')
print(encoded_comment)

print(type(encoded_comment))

