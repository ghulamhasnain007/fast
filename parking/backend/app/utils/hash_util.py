from passlib.hash import bcrypt

async def hash_password(password: str) -> str:
    try:
        return await bcrypt.hash(password)
    except Exception as e:
        print(f"Error hashing password: {e}")
        raise ValueError("Failed to hash password")
