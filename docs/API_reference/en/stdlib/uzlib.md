# uzlib - zlib Decompression

```
This article introduces the use of QuecPython's uzlib module and describes features of the latest version of the uzlib module.
```

The module uses the  binary data compressed by [DEFLATE Algorithm](https://en.wikipedia.org/wiki/DEFLATE) to decompress (generally used in the zlib library and the gzip archiver). This module realizes subsets of the corresponding CPython module. See CPython file [zlib](https://docs.python.org/3.5/library/zlib.html#module-zlib) for more detailed information.


> Note: 1. Compression has not been realized. 2. Before decompressing, the available space in the module should be checked to ensure that there is enough space to decompress.


## Constructor

### `uzlib.decompress`

```python
uzlib.decompress(data, wbits=0, bufsize=0)
```

Returns the compressed bytes object. `wbits` is the window size of DEFLATE dictionary when decompressing. (8–15, the dictionary size is the power of 2 of `wbits` value). If this value is positive, `data` is assumed to be the zlib stream (with the zlib header). If the value is negative, `data` is assumed to be the original DEFLATE stream. `bufsize` is for compatibility with CPython and will be ignored.


### `uzlib.DecompIO`

```python
class uzlib.DecompIO(stream, wbits=0)
```

Creates a `stream` decorator that allows data to be transparently compressed in another stream. This indicates the data can be greater than the compressive stream of available heap size. In addition to the values described above, wbits can have values 24.. 31 (16 + 8.. 15), which indicates that the input stream has the gzip header.

