import re

def extract_emails(text):
    return re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w{2,}\b', text)

def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)

def extract_phone_numbers(text):
    return re.findall(r'(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})', text)

def extract_hashtags(text):
    return re.findall(r'#\w+', text)

# Sample test input
sample_text = """
Contact me at user@example.com or support@company.co.uk. Visit https://www.example.com or https://subdomain.example.org/page.
My number is (123) 456-7890 or 123-456-7890 or 123.456.7890. Let's go viral with #RegexPower and #CodeLife!
"""

print("Emails:", extract_emails(sample_text))
print("URLs:", extract_urls(sample_text))
print("Phone Numbers:", extract_phone_numbers(sample_text))
print("Hashtags:", extract_hashtags(sample_text))
