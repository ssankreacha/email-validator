import re
import dns.resolver
import difflib

# List of known common email domains for typo correction
KNOWN_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "protonmail.com", "icloud.com", "aol.com"]


def is_valid_format(email):
    """
    Checks if the email follows a valid format using regex.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_domain(email):
    """
    Checks if the email's domain has valid MX records (mail server records).
    """
    try:
        domain = email.split('@')[1]
        dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.LifetimeTimeout):
        return False


def suggest_correction(email):
    """
    Suggests a correction if the email domain is mistyped.
    """
    user, domain = email.split('@')
    closest_match = difflib.get_close_matches(domain, KNOWN_DOMAINS, n=1, cutoff=0.7)

    if closest_match:
        corrected_email = f"{user}@{closest_match[0]}"
        return corrected_email
    return None


def validate_email(email):
    """
    Main function that validates an email address.
    """
    if not is_valid_format(email):
        print("❌ Invalid email format. Please check the email structure.")
        return

    if not is_valid_domain(email):
        print("❌ The email domain does not exist or has no mail server.")
        return

    suggested_email = suggest_correction(email)
    if suggested_email and suggested_email != email:
        print(f"⚠️ Did you mean: {suggested_email}?")

    print("✅ The email is valid!")


if __name__ == "__main__":
    user_email = input("Enter an email address to validate: ").strip()
    validate_email(user_email)
