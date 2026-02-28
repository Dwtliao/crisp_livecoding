skus = ["abc-123", "ABC123", "abc_123", "Abc-123 "]


def check_isalnum(c: str):
    # yes if char is alpha char or numbers
    if c.isalnum():
        return c.upper()
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