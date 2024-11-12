## EXTRACT ME IF YOU CAN (3 points)

`re` `group pattern` `search` `findall`

### Task

Implement the following functions using regular expressions and string manipulation.

**1. `extract_emails`**:  
Create a function to extract full email addresses from a string. Assume that usernames, domains, and tlds are strings of letters, digits, and underscores.

```
>>> extract_emails("Hello mister_egor228@gmail.com, I am a Nigerian prince and I want to offer you a business opportunity." \
...                "Please send me your bank account number to authentic_nigerian_prince@zoo.poo")
['mister_egor228@gmail.com', 'authentic_nigerian_prince@zoo.poo']
```

**2. `has_vowel`**:  
Write a function that accepts a string and returns True if the string contains a vowel (a, e, i, o, or u), and False otherwise.

```
>>> has_vowel("Hello")
True

>>> has_vowel("rhythm")
False
```

**3. `parse_number`**:  
Create a function that parses phone numbers in the format `{area code}-{local exchange}-{line number}`, where `{area code}`, `{local exchange}`, and `{line number}` are strings of digits of length 3, 3, and 4 respectively. The function should return `None` if no match is found, and the first match if several are found.

```
>>> parse_number("My phone number is 123-456-7890.")
('123', '456', '7890')

>>> parse_number("My phone number is 123-456-789.")
None
```

### About the Task

These tasks are designed to test your understanding of regular expressions, a powerful tool for pattern searching in strings. This is a common task in data extraction and text processing tasks in real-world applications.

---
