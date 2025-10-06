import base64
# {level},{money},{gold},{gold_claim},0,0,0,{black_bricks},0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{boss_level},{skill_points},0,0,0,

money = input('How much money do you want?: ')
level = input('What level do you want to be at?: ')
gold = input('How much gold do you want?: ')
gold_claim = input('How much gold should you claim on reset?: ')
black_bricks = input('How many BB (black bricks) do you want?: ')
skill_points = input('How many skill points do you want?: ')

boss_level = '0'

code = f'{level},{money},{gold},{gold_claim},0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{black_bricks},0,0,0,{boss_level},{skill_points},0,0,0,'
# Encode the string to bytes (UTF-8)
code_bytes = code.encode("utf-8")

# Base64-encode those bytes
encoded_bytes = base64.b64encode(code_bytes)

# Convert the Base64 bytes back to a string for printing or saving
encoded_str = encoded_bytes.decode("utf-8")

print(encoded_str)

