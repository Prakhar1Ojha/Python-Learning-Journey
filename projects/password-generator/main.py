"""Secure random password generator (CLI)."""

import argparse
import secrets
import string


def generate_password(
    length: int = 12,
    use_digits: bool = True,
    use_symbols: bool = True,
    use_upper: bool = True,
) -> str:
    pool = string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += "!@#$%^&*()-_=+"
    return "".join(secrets.choice(pool) for _ in range(length))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("--length", type=int, default=12)
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")
    parser.add_argument("--no-upper", action="store_true")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols,
        use_upper=not args.no_upper,
    )
    print(password)


if __name__ == "__main__":
    main()
