import jwt


def is_token_valid(input):
    token = input  # 在实际应用中，从配置文件或输入获取Token
    secret_key = 'lhhsa_youareinmyheart'
    try:
        jwt.decode(token, secret_key, algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False