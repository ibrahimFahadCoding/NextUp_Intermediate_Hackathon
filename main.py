print("Ibrahim Fahad")

#Note: The terminal squishes all the emojis together, but they aren't actually like that.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

emoji_map = {
    "a": "👽", "b": "🍌", "c": "🚗", "d": "🧨", "e": "💥", "f": "🔥", 
    "g": "👻", "h": "🌶️", "i": "👀", "j": "🧃", "k": "🪁", "l": "⚡", "m": "🐵", 
    "n": "🤓", "o": "🛑", "p": "🥳", "q": "❓", "r": "🤖", "s": "🟦", "t": "🔺", 
    "u": "☂️", "v": "🧛", "w": "💦", "x": "❌", "y": "⁉️", "z": "🦓"
}

#Used for decoding
emoji_to_letter = {v: k for k, v in emoji_map.items()}

def encode_decode_msg(msg, is_encode):
    new_msg = []
    letter_index = 0  # Track letters separately

    for char in msg.lower():
        if char.isalpha():  # Only process letters
            shift = fibonacci(letter_index + 1)  # Use only letter index for Fibonacci shifts
            if is_encode:
                new_shifted_val = ord(char) + shift
            else:
                new_shifted_val = ord(char) - shift
            new_shifted_val = 97 + ((new_shifted_val - 97) % 26)  # Wrap within 'a' to 'z'
            new_msg.append(chr(new_shifted_val))
            letter_index += 1  # Increment only for letters
        else:
            new_msg.append(char)  # Keep spaces, punctuation, and numbers unchanged
    
    return "".join(new_msg)

def replace_with_emojis(text, is_encode):
    if is_encode:
        return "".join(emoji_map.get(char, char) for char in text)
    else:
        decoded_msg = []
        i = 0
        while i < len(text):
            if text[i] in emoji_to_letter:
                decoded_msg.append(emoji_to_letter[text[i]])
                i += 1
            elif i+1 < len(text) and text[i:i+2] in emoji_to_letter:
                decoded_msg.append(emoji_to_letter[text[i:i+2]])
                i += 2
            else:
                decoded_msg.append(text[i])
                i += 1
        
        return "".join(decoded_msg)
        

# Encoding Process
msg = input("Enter a message to encode: ")
encoded_msg = encode_decode_msg(msg, True)
emoji_encoded_msg = replace_with_emojis(encoded_msg, True)
print("Encoded Message: ", emoji_encoded_msg)

# Decoding Process
msg = input("Enter a message to decode: ")
decoded_letters = replace_with_emojis(msg, False)  # Convert emojis back to letters
decoded_msg = encode_decode_msg(decoded_letters, False)  # Decode letter shifts
print("Decoded Message: ", decoded_msg)
