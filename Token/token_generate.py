import jwt
import datetime

def generate_token(secret_key, duration_days):
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(days=duration_days)
    token = jwt.encode({'exp': expiration_date}, secret_key, algorithm='HS256')
    return token

secret_key = 'lhhsa_youareinmyheart'
duration_days = 365  # Token有效期为30天
token = generate_token(secret_key, duration_days)
print(f"Generated Token: {token}")
