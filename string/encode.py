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

print(" string.encode() ".center(50, "*"))

text = "Caf B &/ Bistro - In Go-To Place!"
encoded_text = text.encode('utf-8')
print("Text: ", "\t"*4, text)

print("Encoded Text: ", encoded_text)
print(" bytes.decode() ".center(50, "*"))
# Decoding encoded objects/strings
# For the URL-safe title encoded as hex
encoded_title_hex = '436166204220262f2042697374726f202d20496e20476f2d546f20506c61636521'
decoded_title = bytes.fromhex(encoded_title_hex).decode('utf-8')
print("Decoded Text: ",decoded_title)

# # For the encoded password
# encoded_password = b'P@ssw0rd!'
# decoded_password = encoded_password.decode('utf-8')
# print(decoded_password)

# # For the data serialization example
# encoded_data = b'Data with special characters: \xc2\xa3\xe2\x82\xac$\xc2\xa5'
# decoded_data = encoded_data.decode('utf-8')
# print(decoded_data)

# # For the emoji in text data
# encoded_comment = b'Great job team! \xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\xa5\xb3'
# decoded_comment = encoded_comment.decode('utf-8')
# print(decoded_comment)

# # For ASCII compatibility example (Note: Original characters lost during encoding cannot be recovered)
# ascii_encoded_name = b'Jos Rodrguez'
# decoded_name = ascii_encoded_name.decode('ascii')
# print(decoded_name)


