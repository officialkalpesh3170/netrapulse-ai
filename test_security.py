from backend.auth_service.core.security import(
    hash_password,
    verify_password,
)

password = "Password123"

hashed_password =hash_password(password)
print("Original password")
print(password)

print("Hashed password")
print(hashed_password)
print("Password verification")
print(verify_password(password, hashed_password))