# regex_extractor.py
import re

def extract_emails(text):
    # Regex for extracting emails
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(pattern, text)

def extract_urls(text):
    # Regex for extracting URLs
    pattern = r"https?://[^\s'\"<>]+"
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    # Regex for extracting phone numbers
    # Matches formats like: (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890
    pattern = r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
    return re.findall(pattern, text)

def extract_credit_cards(text):
    # Regex for extracting credit card numbers
    pattern = r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b"
    return re.findall(pattern, text)

# This functions ensures no duplicates in the extracted lists
def uniq(seq):
    seen = set()
    out = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
