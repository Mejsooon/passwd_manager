import base64
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_key():
    """Generuje nowy klucz AES-256."""

    key = AESGCM.generate_key(bit_length=256)

    print("\n" + "=" * 60)
    print("NOWY KLUCZ AES-256")
    print("=" * 60)

    key_text = base64.b64encode(key).decode("ascii")

    print("\nTwój klucz:")
    print(key_text)

    print("\nZAPISZ TEN KLUCZ NA KARTCE.")
    print("Ten sam klucz będzie używany do wszystkich haseł.")

    print("=" * 60)

    return key


def read_key():
    """Wczytuje istniejący klucz AES-256."""

    print("\n=== PODAWANIE KLUCZA ===")

    key_text = input("Podaj klucz AES-256: ").strip()

    try:
        key = base64.b64decode(key_text, validate=True)

        if len(key) != 32:
            raise ValueError

        return key

    except Exception:
        print("\nBŁĄD: Nieprawidłowy klucz AES-256.")
        return None


def encrypt_password(key):
    """Szyfruje hasło przy użyciu AES-256-GCM."""

    print("\n=== SZYFROWANIE HASŁA ===")

    password = input("Podaj hasło do zaszyfrowania: ")

    # Generujemy nowy, losowy nonce dla każdego hasła.
    nonce = os.urandom(12)

    # Tworzymy obiekt AES-GCM.
    aes = AESGCM(key)

    # Szyfrowanie.
    ciphertext = aes.encrypt(
        nonce,
        password.encode("utf-8"),
        None
    )

    # Zamieniamy dane binarne na tekst Base64,
    # żeby można było je zapisać na kartce.
    nonce_text = base64.b64encode(nonce).decode("ascii")
    ciphertext_text = base64.b64encode(ciphertext).decode("ascii")

    print("\n" + "=" * 60)
    print("ZASZYFROWANE HASŁO")
    print("=" * 60)

    print("\nNONCE:")
    print(nonce_text)

    print("\nCIPHERTEXT:")
    print(ciphertext_text)

    print("\n" + "=" * 60)
    print("Zapisz NONCE oraz CIPHERTEXT.")
    print("Klucz pozostaje taki sam dla wszystkich haseł.")
    print("=" * 60)


def decrypt_password(key):
    """Odszyfrowuje hasło przy użyciu AES-256-GCM."""

    print("\n=== ODSZYFROWYWANIE ===")

    nonce_text = input("\nPodaj NONCE: ").strip()
    ciphertext_text = input("Podaj CIPHERTEXT: ").strip()

    try:
        nonce = base64.b64decode(
            nonce_text,
            validate=True
        )

        ciphertext = base64.b64decode(
            ciphertext_text,
            validate=True
        )

        if len(nonce) != 12:
            raise ValueError

    except Exception:
        print("\nBŁĄD: Nieprawidłowy nonce lub ciphertext.")
        return

    try:
        aes = AESGCM(key)

        plaintext = aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        password = plaintext.decode("utf-8")

    except Exception:
        print("\nBŁĄD: Nie można odszyfrować hasła.")
        print("Sprawdź klucz, nonce oraz ciphertext.")
        return

    print("\n" + "=" * 60)
    print("ODSZYFROWANE HASŁO:")
    print("=" * 60)

    print(password)

    print("=" * 60)


def main():

    print("=" * 60)
    print("              PASSWORD CRYPTO")
    print("=" * 60)

    print("\n1. Wygeneruj nowy klucz")
    print("2. Użyj istniejącego klucza")

    choice = input("\nWybierz: ").strip()

    # -----------------------------------------
    # GENEROWANIE NOWEGO KLUCZA
    # -----------------------------------------

    if choice == "1":

        key = generate_key()

        input(
            "\nNaciśnij ENTER po zapisaniu klucza na kartce..."
        )

    # -----------------------------------------
    # UŻYCIE ISTNIEJĄCEGO KLUCZA
    # -----------------------------------------

    elif choice == "2":

        key = read_key()

        if key is None:
            return

    else:

        print("\nNieprawidłowy wybór.")
        return

    # -----------------------------------------
    # GŁÓWNE MENU
    # -----------------------------------------

    while True:

        print("\n")
        print("=" * 40)
        print("MENU")
        print("=" * 40)

        print("1. Zaszyfruj hasło")
        print("2. Odszyfruj hasło")
        print("3. Wyjście")

        choice = input("\nWybierz: ").strip()

        # SZYFROWANIE
        if choice == "1":

            encrypt_password(key)

        # ODSZYFROWYWANIE
        elif choice == "2":

            decrypt_password(key)

        # WYJŚCIE
        elif choice == "3":

            print("\nKoniec programu.")
            break

        else:

            print("\nNieprawidłowa opcja.")


# Uruchomienie programu
if __name__ == "__main__":
    main()