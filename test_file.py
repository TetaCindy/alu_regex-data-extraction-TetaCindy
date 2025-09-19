#Test file for regex_extractor 
from regex_extractor import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards,
    uniq
)

sample_text = """
Emails: user@example.com, firstname.lastname@company.co.uk, bad@.com, hello+test@domain.co
URLs: https://www.example.com, http://example.org/page, https://sub.example.com/path?query=1
Phones: (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890
Cards: 1234 5678 9012 3456, 1234-5678-9012-3456, 1234567890123456
"""

def pretty_print(title, items):
    print(f"\n=== {title} ({len(items)}) ===")
    for i, it in enumerate(items, 1):
        print(f"{i}. {it}")

def main():
    emails = uniq(extract_emails(sample_text))
    urls = uniq(extract_urls(sample_text))
    phones = uniq(extract_phone_numbers(sample_text))
    cards = uniq(extract_credit_cards(sample_text))

    pretty_print("Emails", emails)
    pretty_print("URLs", urls)
    pretty_print("Phone Numbers", phones)
    pretty_print("Credit Cards", cards)

if __name__ == "__main__":
    main()
