## CAESAR CIPHER (1 point)

`str.maketrans`

### Task

Write a function `caesar_encrypt` that encrypts the string passed to it using the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) with a key `n`.
Don't forget to properly handle lowercase and uppercase letters.

The function takes 2 parameters:
- the string to be encrypted
- an integer, which can also be negative – the cipher key

### Example
```
>>> caesar_encrypt('This is stupid song stupid stupid stupid song', 10)
'Drsc sc cdezsn cyxq cdezsn cdezsn cdezsn cyxq'
```

---
