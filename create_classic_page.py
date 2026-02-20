import re
import os

input_file = r"c:\Downloaded Web Sites\aurora-wedding.webflow.io\rj-events.html"
output_file = r"c:\Downloaded Web Sites\aurora-wedding.webflow.io\classicweddingplanners.html"

print(f"Reading from {input_file}...")
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

print("Performing replacements...")

# 1. Branding
# Replace "RJ EVENTS" with "Classic Wedding Planners"
text = text.replace("RJ EVENTS", "Classic Wedding Planners")

# 2. Phone Numbers
# Remove the second phone number link entirely
# Matches <a href="tel:+918778335667" ... > ... </a>
# We use [\s\S]*? to match across newlines non-greedily
text = re.sub(r'<a href="tel:\+918778335667"[\s\S]*?</a>', '', text)

# Update the first phone number
# Update href
text = text.replace('href="tel:+918637616669"', 'href="tel:+919489747455"')

# Update display text (handling potential newlines/spaces)
# Finds +91 followed by whitespace and the old number parts
text = re.sub(r'\+91\s*86376\s*16669', '+91 94897 47455', text)

print(f"Writing to {output_file}...")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print("Conversion complete.")
