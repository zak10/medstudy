import os

with open(os.path.dirname(os.path.abspath(__file__)) + "/data/free_domains.csv") as f:
    free_domains = set([l.strip() for l in f.readlines()])


def is_business_email(email: str) -> bool:
    """
    Validates if an email address appears to be a business email rather than a personal one.

    Args:
        email: String containing the email address to validate

    Returns:
        bool: True if it appears to be a business email, False otherwise
    """
    try:
        # Basic email format validation
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")

        # Extract domain
        domain = email.lower().split("@")[1]

        # Check if domain is in known personal email providers
        if domain in free_domains:
            return False

        # Additional checks could be added here:
        # - Domain registration date
        # - MX record verification
        # - Company domain database lookup
        # - Domain age verification

        return True

    except Exception as e:
        raise ValueError(f"Error validating email: {str(e)}")
