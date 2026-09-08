# passwd_manager

# Password Crypto

A lightweight command-line application for encrypting and decrypting passwords using **AES-256-GCM**.

The application is designed as a simple educational and personal password encryption tool. It uses a single AES-256 key for all passwords while generating a unique cryptographically secure nonce for every encryption operation.

---

## Features

- AES-256-GCM authenticated encryption
- Single master key shared across all encrypted passwords
- Cryptographically secure random 12-byte nonce for every encryption
- Authentication tag provided by AES-GCM to detect data tampering
- Base64 encoding for convenient storage and manual transcription
- Password encryption and decryption from a command-line interface
- No database or external storage required
- No passwords or encryption keys are automatically saved to disk

---

## How It Works

The application uses **AES-256-GCM** (Advanced Encryption Standard with a 256-bit key in Galois/Counter Mode).

The encryption process can be represented as:

```text
                    AES-256-GCM
                         │
                         ▼
Password ────────► Encryption ────────► Ciphertext
                         ▲
                         │
                    Random Nonce
                         │
                         ▼
                    12 bytes
```
For every encrypted password, the application generates a new random nonce.

The same key can therefore be safely used to encrypt multiple passwords, provided that the nonce is never reused with the same key.

---

## Stored Data

For each password, the application produces:

```text
NONCE
CIPHERTEXT
```

The nonce does not need to be kept secret. It is required together with the ciphertext during decryption.

The AES key must remain secret.