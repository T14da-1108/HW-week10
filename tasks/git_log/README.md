## GIT LOG (2 points)

`str.format` `split` `strip`

### Task

Write a program to reformat the output of the git log command. The function takes two arguments -- the input stream and the output stream.

#### Input Format

The function's input stream is given a log with a description of commits, each line of which has the following format:

`<sha-1>\t<date>\t<author>\t<email>\t<message>`

#### Output Format

The output stream should write log lines in the format: `<first 7 characters of sha-1>.....<message>`.
The total length of the output line should be 80 characters. It is assumed that the input is always correct.

### Example

```
0cd8619f18d8ecad1e5d2303f95ed206c2d6f92b	Fri Sep 23 10:59:32 2016 -0700	Brett Cannon	brettcannon@users.noreply.github.com	Update PEP 512 (#107)
94dbee096b92f10ab83bbcf88102c6acdc3d76d1	Thu Sep 22 12:39:58 2016 +0100	Thomas Kluyver	takowl@gmail.com	Update PEP 517 to use pyproject.toml from PEP 518 (#51)
```

Answer:

```
0cd8619....................................................Update PEP 512 (#107)
94dbee0..................Update PEP 517 to use pyproject.toml from PEP 518 (#51)
```

---
