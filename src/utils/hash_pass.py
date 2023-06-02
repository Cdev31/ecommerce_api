import bcrypt

def hash_password(pasword:str) -> str:
    hashing:bytes = bcrypt.hashpw(pasword.encode('utf-8'),bcrypt.gensalt(rounds=8))
    return str(hashing)

def check_password(password:str,hash:bytes)-> bool:
    checking:bool = bcrypt.checkpw(password.encode('utf-8'),hash)
    return checking