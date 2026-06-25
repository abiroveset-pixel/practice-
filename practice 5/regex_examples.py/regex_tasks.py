import re

# 1. 'a' followed by zero or more 'b'
print("1.")
text = "abbb"
print(bool(re.fullmatch(r"ab*", text)))

# 2. 'a' followed by two to three 'b'
print("\n2.")
text = "abbb"
print(bool(re.fullmatch(r"ab{2,3}", text)))

# 3. Lowercase letters joined with underscore
print("\n3.")
text = "hello_world test_string Hello_World"
print(re.findall(r"\b[a-z]+_[a-z]+\b", text))

# 4. One uppercase letter followed by lowercase letters
print("\n4.")
text = "Hello World ABC Test"
print(re.findall(r"\b[A-Z][a-z]+\b", text))

# 5. 'a' followed by anything, ending in 'b'
print("\n5.")
text = "axxxb"
print(bool(re.fullmatch(r"a.*b", text)))

# 6. Replace space, comma, or dot with colon
print("\n6.")
text = "Hello, world. Python regex"
print(re.sub(r"[ ,.]", ":", text))

# 7. Snake case to camel case
print("\n7.")
text = "hello_world_python"

parts = text.split("_")
camel = parts[0] + "".join(word.capitalize() for word in parts[1:])
print(camel)

# 8. Split a string at uppercase letters
print("\n8.")
text = "HelloWorldPython"
print(re.findall(r"[A-Z][a-z]*", text))

# 9. Insert spaces between words starting with capital letters
print("\n9.")
text = "HelloWorldPython"
print(re.sub(r"([A-Z])", r" \1", text).strip())

# 10. Camel case to snake case
print("\n10.")
text = "HelloWorldPython"

snake = re.sub(r"([A-Z])", r"_\1", text).lower().lstrip("_")
print(snake)