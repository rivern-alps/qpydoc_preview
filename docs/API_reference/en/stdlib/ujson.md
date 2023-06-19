# ujson - JOSN Encoding and Decoding
`ujson` module realizes the convertion between the Python data object and the JSON data format, and subsets of the corresponding CPython module. See CPython file [json](https://docs.python.org/3.5/library/json.html#module-json) for more detailed information.


## Encoding JSON Data

Encodes `Python` object to JSON character string.

### `ujson.dump`

```python
ujson.dump(obj, stream)
```

Serializes  `obj` data object, converts it to `JSON` character string, and writes it to the specified `stream`.

### `ujson.dumps`

```python
ujson.dumps(obj)
```

Converts the data in dictionary type of `obj` to `JSON` character string.

## Decoding JSON Data

Decodes JSON data to `Python` object.

### `ujson.load`

```python
ujson.load(stream)
```

Parses the specified `stream` into `JSON` character string and deserializes it into `Python` object, finally returns the object.

### `ujson.loads`

```python
ujson.loads(str)
```

Parses `JSON` character string `str` and returns a `Python` object.

