## STRING MANIPULATIONS (3 points)

`string` `str methods` `format`

### Task

Implement the following functions using the `str` methods.

**1. `capwords`**:  
Create a function that takes a string and an optional separator, returning a new string where each word starts with a capital letter. The splitting behavior should match the `str.split` method.

```
>>> capwords("foo,bar boo,", sep=",")
'Foo,Bar boo,'
>>> capwords("foo,bar boo,", sep="")
Traceback (most recent call last):
  ...
ValueError: empty separator
>>> capwords(" foo  \nbar\n")
'Foo Bar'
```

**2. `cut_suffix`**:  
Write a function that removes a specified suffix from a string, returning the modified string.

```
>>> cut_suffix("foobar", "bar")
'foo'
>>> cut_suffix("foobar", "boo")
'foobar'
```

**3. `boxed`**:  
Create a function that takes a string, a character `fill`, and a non-negative integer `pad`. The function returns the string inside a box made of the `fill` characters, with padding around the string.

```
>>> print(boxed("Hello world", fill="*", pad=2))
*****************
** Hello world **
*****************
>>> print(boxed("Fishy", fill="#", pad=1))
#########
# Fishy #
#########
```

**4. `find_all`**:  
Implement a function that returns a list of indices where a given substring occurs within a string.

```
>>> find_all("abracadabra", "a")
[0, 3, 5, 7, 10]
>>> find_all("arara", "ara")
[0, 2]
```

**5. `common_prefix`**:  
Create a function that calculates the longest common prefix of one or more strings.

* Example:
  ```
  >>> common_prefix("abra", "abracadabra", "abrasive")
  "abra"
  >>> common_prefix("abra", "foobar")
  ""
  ```

### About the Task

These tasks focus on essential string manipulation techniques that are commonly tested in technical interviews.

---
