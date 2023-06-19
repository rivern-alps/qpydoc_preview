# QuecPython Standard Libraries

> - QuecPython provides built-in modules that reflect the Python standard libraries (e.g.  `os` , `time`) as well as QuecPython specific modules (e.g. `bluetooth` , `machine`).  <br><br>
> - Most standard library modules realize equivalent Python modules, and in a few cases provide some QuecPython-specific extension modules (e.g. `array`，`os`). <br><br>
> - To allow for extension, built-in modules can be extended from Python codes loaded into the device.

This article introduces QuecPython build-in modules (functions and libraries).

You can view all the built-in libraries that can be imported by entering the following code on the REPL:

```python
help('modules')
```

## List of QuecPython Standard Libraries

- [uos - Basic System Services](./uos.md)
- [gc - Reclaimg Memory Fragments](./gc.md)
- [ubinascii - Conversion between Binary and ASCII](./ubinascii.md)
- [ucollections - Collection and Container Types](./ucollections.md)
- [urandom - Random Number Generation](./urandom.md)
- [math - Mathematical Operation](./math.md)
- [usocket - socket Module](./usocket.md)
- [uio - Input and Output Streams](./uio.md)
- [ustruct - Packing and Unpacking the Raw Data Type](./ustruct.md)
- [ujson - Encoding and Decoding JSON](./ujson.md)
- [utime - Time Related Features](./utime.md)
- [sys - System Related Features](./sys.md)
- [uzlib - zlib Decompression](./uzlib.md)
- [thread - Multi-threading](./_thread.md)
- [uhashlib - Hash Algorithm](./uhashlib.md)

<!--Refer to https://python.quectel.com/wiki/#/zh-cn/api/pythonStdlib for the supplement-->