import random
import string

def generate_secure_password(length=16):
    if length < 8:
        raise ValueError("Passwortlänge sollte mindestens 8 Zeichen betragen.")

    # Zeichengruppen definieren
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    # Mindestens ein Zeichen aus jeder Kategorie
    password_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Restliche Zeichen zufällig auffüllen
    remaining_length = length - len(password_chars)
    all_chars = uppercase + lowercase + digits + symbols
    password_chars += random.choices(all_chars, k=remaining_length)

    # Zeichen mischen
    random.shuffle(password_chars)

    return ''.join(password_chars)

# Beispiel:
print("Generiertes Passwort:", generate_secure_password(16))
