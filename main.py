import re

def extract_emails(text):
    "extracts all email addresses"
    return re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w{2,}\b', text)

def extract_urls(text):
    "extracts all urls"
    return re.findall(r'https?://[^\s]+', text)

def extract_phone_numbers(text):
    "extracts all phone numbers"
    return re.findall(r'(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})', text)

def extract_hashtags(text):
    "extracts all hastags"
    return re.findall(r'#\w+', text)

def extract_credit_card_numbers(text):
    """Extracts credit card numbers in formats like 1234-5678-9012-3456 or 1234567890123456."""
    return re.findall(r'\b(?:\d[ -]*?){13,16}\b', text)

# Sample test input
if __name__ == "__main__":
    sample_text = """\nContact me at user@example.com or support@company.co.uk. Visit https://www.example.com or https://subdomain.example.org/page.
My number is (123) 456-7890 or 123-456-7890 or 123.456.7890. Let's go viral with #RegexPower and #CodeLife! Here is my card number: 1234-5678-9012-3456 and 4111 1111 1111 1111.
"""

print("Emails:", extract_emails(sample_text))
print("URLs:", extract_urls(sample_text))
print("Phone numbers:", extract_phone_numbers(sample_text))
print("Hashtags:", extract_hashtags(sample_text))
print("Credit card numbers:", extract_credit_card_numbers(sample_text))

#edge case test
print("\nTesting with empty string:")
empty = ""
print("Emails:", extract_emails(empty))
print("URLs:", extract_urls(empty))
print("Phone numbers:", extract_phone_numbers(empty))
print("Hashtags:", extract_hashtags(empty))
print("Credit card numbers:", extract_credit_card_numbers(empty)) 