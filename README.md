# Python-Encryptor

Portable **pure-Python** CLI for encrypting and decrypting files, folders, or text using pluggable codecs—including from-scratch **AES/Rijndael** modes, **ChaCha20** / **ChaCha20-Poly1305**, and common encodings.

> Educational toolkit. Review cipher parameters carefully before use. This is not a substitute for vetted libraries (OpenSSL, cryptography.io, libsodium) in production systems.

## Overview

Python-Encryptor dynamically loads a codec from `./codec` and runs `encrypt` or `decrypt` against an input path (or interactive text). Several codecs support **iterative encryption** (`--repeat`), padding schemes, and authenticated modes that produce/verify tags. Built to practice applied cryptography and CLI design without external crypto dependencies.

## Features

- Symmetric block & stream ciphers (AES/Rijndael modes, ChaCha20 family)
- Authenticated encryption (AES-GCM, ChaCha20-Poly1305)
- Encoding codecs treated as transforms (Base16/32/64/85/91, ASCII85, etc.)
- File, folder, or interactive text I/O
- Iterative encryption where the codec supports it
- Stdlib-only — no `pip` crypto packages required

## Requirements

- Python 3.x
- Run from the project root so `./codec` resolves correctly

## Quick start

```bash
python encryptor.py -h
python encryptor.py --list-codecs

# Example: AES-CBC encrypt a file
python encryptor.py -c rijn-cbc.encrypt -i secret.txt -o secret.enc --key <16|24|32-char-key> --iv <16-char-iv>

# Decrypt
python encryptor.py -c rijn-cbc.decrypt -i secret.enc -o secret.out --key <key> --iv <iv>

# Iterative encryption (codecs with IE support)
python encryptor.py -c rijn-cbc.encrypt -i secret.txt -o secret.enc --key <key> --iv <iv> -r 3
```

## CLI reference

| Flag | Description |
|------|-------------|
| `-h` | Help |
| `--list-codecs` / `-lc` | List available codecs |
| `-c` / `--codec` | `CODEC.METHOD` where method is `encrypt` or `decrypt` |
| `-i` / `--in-dir` | Input file or folder |
| `-o` / `--out-dir` | Output file or folder |
| `-r` / `--repeat` | Encryption iterations (default `1`) |

Codec-specific parameters (e.g. `--key`, `--iv`, `--ad` / `--aad`, `--tag`, `--counter`) are defined in each module’s `encrypt_args` / `decrypt_args`. If omitted, the CLI prompts for required values.

## Included codecs

| Codec | Notes |
|-------|--------|
| `rijn-ecb`, `rijn-cbc`, `rijn-cfb`, `rijn-ofb`, `rijn-ctr`, `rijn-gcm` | AES/Rijndael modes (GCM is authenticated) |
| `chacha20`, `chacha20-poly1305` | Stream / AEAD |
| `base2` … `base91`, `ascii85` | Encoding transforms |

## Project layout

```
encryptor.py      # CLI entry point
codec/            # Pluggable cipher & encoding modules
LICENSE           # GPL-3.0
```

## License

GPL-3.0 — see `LICENSE`.

## Author

**Aydon Fauscett** — [github.com/aydon14](https://github.com/aydon14)
