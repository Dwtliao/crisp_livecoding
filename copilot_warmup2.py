"""
“What is this problem really asking?”
1. Normalize product SKUs
You receive a list of product SKUs that may contain inconsistent formatting:
["abc-123", "ABC123", "abc_123", "Abc-123 "]

Return a list of normalized SKUs where:
letters are uppercase;  separators are removed;  whitespace is trimmed

Real question:
Can you identify the canonical representation before coding?
Skills trained:
clarifying assumptions,  defining invariants,  designing helper functions
"""
skus = ["abc-123", "ABC123", "abc_123", "Abc-123 "]

# assumptions, looks like SKU pattern is x letters and x numbers and possible separators which can be multiple things
# like even white space but expect to have to remove some kind of separator

"""
A founder‑level assumption sounds like this:
“The only reliable signal is alphanumeric characters.
Anything that is not a letter or digit is noise.
The canonical form is uppercase letters + digits with no separators or whitespace.”
This avoids assuming: order, length, grouping, meaning of separators, presence of separators
It also aligns perfectly with the prompt’s real question:
Can you identify the canonical representation before coding?

The clearest single‑sentence statement of the canonical pattern is:
“A normalized SKU is the uppercase sequence of all alphanumeric characters in order, with all whitespace and separators removed.”
This is the version that sounds senior and calm:

“I’ll write a small helper that takes a character, uppercases it, and returns it only if it’s’ll write a small helper that takes a character, uppercases it, and returns it only if it’s a letter or digit. I can check that either with Python’s isalnum() or like A–Z and 0– by comparing ranges9. The key is that only alphanumeric characters survive.”
"""
skus = ["abc-123", "ABC123", "abc_123", "Abc-123 "]

def check_alphanumeric(c: str):
    # expect string to be passed
    C = c.upper()
    if ("A" <= C <= "Z") or ("0" <= C <= "9"):
        return C
    return None

def check_isalnum(c: str):
    # yes if char is alpha char or numbers
    if c.isalnum():
        return c.upper()
    else:
        return None

cleaned_skus = []
for sku in skus:
    norm = ""
    for c in sku:
        if check_isalnum(c) is not None:
            norm = norm + (check_isalnum(c))  # creates a new string each loop wasteful

    cleaned_skus.append(norm)

print(cleaned_skus)

#  version that balances clarity, correctness, and cleverness:
def normalize_sku(sku: str):
    chars = []  # 'ABC123' collect pieces in a list
    for c in sku:
        normalized = check_isalnum(c)
        if normalized is not None:
            chars.append(normalized)
            # idiomatic way to build strings.  join them once at the end
    return "".join(chars)

# ['ABC123', 'ABC123', 'ABC123', 'ABC123']
cleaned_skus = [normalize_sku(sku) for sku in skus]
print(cleaned_skus)