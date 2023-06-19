# sys - System Related Features 

> The new architecture code has upgraded the MPY version, and sys is changed to usys. It is recommended to import the module with the following methods.

```python
try:
    import usys as sys
except ImportError:
    import sys
```

## Constant

### `sys.argv`

The list of variable parameters of enabling the current program.

### `sys.byteorder`

Byte order (‘little’  - little-endian,  ‘big’ - big-endian).

### `sys.implementation`

Returns the current version information of MicroPython. MicroPython has following attributes:

- name - Character string“ micropython”

- version - Tuple (major, minor, micro), such as (1, 7, 0)

- _mpy - The version information of mpy file. The parse method is below. mpy_cross needs to adapt to this version information when generating mpy.

```python
import sys
sys_mpy = sys.implementation._mpy
arch = [None, 'x86', 'x64',
    'armv6', 'armv6m', 'armv7m', 'armv7em', 'armv7emsp', 'armv7emdp',
    'xtensa', 'xtensawin'][sys_mpy >> 10]
print('mpy version:', sys_mpy & 0xff)
print('mpy sub-version:', sys_mpy >> 8 & 3)
print('mpy flags:', end='')
if arch:
    print(' -march=' + arch, end='')
print()
```

It is recommended to use this object to distinguish MicroPython from other Python implementations.

### `sys.maxsize`

The maximum value of QuecPython module integers which can retain on the current platform. If it is less than the maximum value in the platform, it is the maximum value represented by the MicroPython integer (this is the case for MicroPython ports that do not support the long integer).

### `sys.modules`

Returns the imported modules in the current Python in dictionary form.

### `sys.platform`

MicroPython Operation Platform.

### `sys.stdin`

Standard Input (Default: USB virtual serial port. Other serial ports are optional).

### `sys.stdout`

Standard Output (Default: USB virtual serial port. Other serial ports are optional).

### `sys.version`

String type. MicroPython version.

### `sys.version_info`

Integer tuple type. MicroPython version.

## **Methods**

### `sys.exit`

```python
sys.exit(retval=0)
```

Exits the current program with the given parameters.

**Parameter**

* `retval` - Integer type. Exiting parameter.

This function triggers a  `SystemExit` exit. If a parameter is given, its value is assigned as a parameter to `SystemExit`.

### `sys.print_exception`

```python
sys.print_exception(exc, file=sys.stdout)
```

Prints the exception information to the file object. The generated file is sys.stdout by default, which is the standard output of the exception information.

* `exc` - Exception object.

* `file` - The specified output file. The generated file is sys.stdout by default.

