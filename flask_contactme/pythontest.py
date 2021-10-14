from dotenv import load_dotenv
import os
load_dotenv()

e_user = os.getenv("ENCYPT_USER")
e_pass = os.environ.get("ENCRYPT_PASS")
To_user = os.environ.get('TO_USER')

print(e_user)
print(e_pass)
print(To_user)