import hashlib
import requests
from signal_handler import SignalHandler

API_URL = "https://api.pwnedpasswords.com/range/"
signal = SignalHandler()

def request_password_check(hashedpwd):
    response = requests.get(API_URL + hashedpwd, timeout=5)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch response, status code is {response.status_code}")
    return response

def count_pwned_passwords(response, hash_tail):
    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == hash_tail:
            return count
    return 0

def check_password(password):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    hash_head, hash_tail = hashed_password[:5], hashed_password[5:]
    response = request_password_check(hash_head)
    return count_pwned_passwords(response, hash_tail)

def main(filename):
    with open(filename, "r", encoding="utf-8") as pwdfile:
        for i, line in enumerate(pwdfile.readlines()):
            password = line.strip()
            pwned_count = check_password(password)
            print(f"Password {i} was breached {pwned_count} times")

if __name__ == "__main__":
    while signal.can_run():
        main("passwords.txt")
