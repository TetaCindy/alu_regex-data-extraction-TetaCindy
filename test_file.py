from regex_extractor import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards
)

# Sample text with all the examples from assignment
sample_text = """
Email addresses:
user@example.com
firstname.lastname@company.co.uk

URLs:
https://www.example.com
https://subdomain.example.org/page

Phone numbers (various formats):
(123) 456-7890
123-456-7890
123.456.7890

Credit card numbers:
1234 5678 9012 3456
1234-5678-9012-3456

Time:
14:30
2:30 PM

HTML tags:
<p>
<div class="example">
<img src="image.jpg" alt="description">

Hashtags:
#example
#ThisIsAHashtag

Currency amounts:
$19.99
$1,234.56
"""
# This function runs the extractor on the sample text and prints results.
def main():
    print("Emails:", extract_emails(sample_text))
    print("URLs:", extract_urls(sample_text))
    print("Phones:", extract_phone_numbers(sample_text))
    print("Credit Cards:", extract_credit_cards(sample_text))


# This is to ensure no duplicates in the extracted lists (placeholder comment).
if __name__ == "__main__":
    main()
