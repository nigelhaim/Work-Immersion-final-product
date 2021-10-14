import os 

e_user = os.environ.get('ENCRYPT_USER')
e_pass = os.environ.get('ENCRYPT_PASS')
to_user = os.environ.get('TO_USER')

print(e_user)
print(e_pass)
print(to_user)