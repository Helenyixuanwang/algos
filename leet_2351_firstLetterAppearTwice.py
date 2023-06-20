def first_letter_twice(str):
    seen = set()
    for c in str:
        if c in seen:
            return c
        seen.add(c)
    return "No letter appears twice"

str = "abcdefghia"
print(first_letter_twice(str))