# app_fota - User File Upgrade

The `app_fota` module is used for user file upgrades.

**Example**：

```python
import app_fota
from misc import Power

fota = app_fota.new()
download_list = [{'url': 'http://www.example.com/app.py', 'file_name': '/usr/app.py'}, {'url': 'http://www.example.com/test.txt', 'file_name': '/usr/text.txt'}]
fota.bulk_download(download_list) # Download
fota.set_update_flag() # Set update flag
Power.powerRestart() # Restart
```

## Initialization

### `app_fota.new`

```python
app_fota.new()
```

Creates an app_fota object.

**Return Value:**

- app_fota object.

**Example**：

```python
import app_fota
fota = app_fota.new()
```

## Download

### `fota.download`

```python
fota.download(url, file_name)
```

Downloads a single file.

**Parameter:**

- `url`-String type. The URL of the file to be downloaded. 
- `file_name`-String type. The absolute path of the local file to be upgraded. 

**Return Value**：

- `0`-Successful execution;  `-1`-Failed execution.

### `fota.bulk_download`

```python
fota.bulk_download(info=[])
```

Downloads bulk files.

**Parameter:**

- `info`-List type. The bulk download lists. Each elements of the list is a dictionary containing `url` and `file_name`. 

**Return Value**：

- Returns the list of failed downloads in list type when the download fails.  
- Returns NULL when the download succeeds.

**Example**：

```python
download_list = [{'url': 'http://www.example.com/app.py', 'file_name': '/usr/app.py'}, {'url': 'http://www.example.com/test.txt', 'file_name': '/usr/text.txt'}]
fota.bulk_download(download_list)
```

In the example above, assuming that it fails to download  `http://www.example.com/test.txt`, the return value is `[{url: 'http://www.example.com/test.txt', file_name: '/usr/text.txt'}]`.

## Set Upgrade Flag

### `fota.set_update_flag`

```python
fota.set_update_flag()
```

Sets the upgrade flag. After the upgrade flag is set, call the restart interface to restart the module. After that, the upgrade process can be started. You can enter the application once the upgrade completes. 

