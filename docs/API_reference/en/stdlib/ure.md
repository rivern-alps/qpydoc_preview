# ure – Regular Expression

This feature matches data by regular expression.

>Currently, only a few operators are supported. 

**Example**

```python
import ure

res = '''
$GNRMC,133648.00,A,3149.2969,N,11706.9027,E,0.055,,311020,,,A,V*18
$GNGGA,133648.00,3149.2969,N,11706.9027,E,1,24,1.03,88.9,M,,M,,*6C
$GNGLL,3149.2969,N,11706.9027,E,133648.00,A,A*7A
$GNGSA,A,3,31,26,11,194,27,195,08,09,03,193,04,16,1.41,1.03,0.97,1*31
'''

r = ure.search("GNGGA(.+?)M", res)
print(r.group(0))
```

## Compile and Generate Regular Expression

### `ure.compile`

```python
ure.compile(regex)
```

Compiles a regular expression and generates a regular-expression object, used by *ure.match()* and *ure.search()*.

**Parameter**

- `regex` – String type. A regular expression.


## Match Regular Expression

### `ure.match`

```python
ure.match(regex, string)
```

Matches the compiled regular expression against *string*. Match always happens from the start position in a string.

**Parameter**

- `regex` – String type. A regular expression.
- `string` – The string to be matched.

**Return Value**

- A matched object – Successful execution
- None – Failed execution

## Search Regular Expression

### `ure.search`

```python
ure.search(regex, string)
```

Searches for the compiled regular expression in *string* and returns the first successful match.

**Parameter**

- `regex` – String type. A regular expression.
- `string` – The string in which you search for the compiled regular expression

**Return Value**

- A matched object – Successful execution
- None – Failed execution


## Match Single String

### `match.group`

```python
match.group(index)
```

Matches objects as returned by *ure.match()* and *ure.search()*.

**Parameter**

- `index` – Integer type. The index of the groups of the match. In a regular expression, *match.group()* proposes the string captured by grouping. *index* is 0 for the entire match.  *index* is captured by the compiled regular expression and an error occurs when the group does not exist.

**Return Value**

- The string matching the entire regular expression.


## Constants

### Supported Operators
- `‘.’` – Character type. Match any character.
- `‘[]’` – Character type. Match set of characters. Individual characters and ranges are supported, including negated sets.
- `‘^’` – Character type. Match the start of the string.
- `‘$’` – Character type. Match the end of the string.
- `‘?’` – Character type. Match zero or one of the previous sub-pattern.
- `‘*’` – Character type. Match zero or more of the previous sub-pattern.
- `‘+’` – Character type. Match one or more of the previous sub-pattern.
- `‘??’` – Character type. Non-greedy version of `?`, match zero or one.
- `‘*?’` – Character type. Non-greedy version of `*`, match zero or more.
- `‘+?’` – Character type. Non-greedy version of `+`, match one or more.
- `‘\|’` – Character type. Match either the left-hand side or the right-hand side sub-patterns of this operator.
- `‘\d’` – Character type. Match digit. 
- `‘\D’` – Character type. Match non-digit. 
- `‘\s’` – Character type. Match whitespace.
- `‘\S’` – Character type. Match non-whitespace.
- `‘\w’` – Character type. Match "word characters" (ASCII only).
- `‘\W’` – Character type. Match "word characters" (ASCII only).


### Not Supported Operators
- `‘{m,n}’` – Counted repetitions.
- `‘(?P<name>...)’` – Named groups.
- `‘(?:...)’` – Non-capturing groups.
- `‘\b’` – More advanced assertions.
- `‘\B’` – More advanced assertions.
- `‘\r’` – Special character escapes – use Python’s own escaping instead.
- `‘\n’` – Special character escapes – use Python’s own escaping instead.

