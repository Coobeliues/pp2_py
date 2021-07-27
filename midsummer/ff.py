import re

inp = input()
pni = input()
nik, dom, su = [], [], []

email = re.findall(r"[a-zA-Z0-9!$%^&*@#_-]{3,32}#[0-9]{4}", inp)
email.sort()
pas = re.findall(r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,}", pni)

if pas and email:
    print('Welcome to Discord')
else:
    print('Invalid password or username')