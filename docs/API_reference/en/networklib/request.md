# request - HTTP Client

The `request` feature is used for sending an HTTP request to a server, fetching data from a server, or submitting data to a server. Multiple request methods, including GET, POST, and PUT are supported. 

## HTTP Request

### `request.get`

```python
response = requtes.get(url)
```

Sends a GET request.

**Parameter**

- `url` - Required parameter. The server IP address in the request.
- `data` - Optional parameter. Parameters to be carried in JSON format in the request.
- `headers` - Dictionary type. Optional parameter. The header information in the request.
- `decode` - Boolean type. Optional parameter. Decode the response result with UTF-8 after the request is successful. True: Decode. False: Not decode. Default value: True. Bytes will be returned if False is entered. This parameter is only used for *response.content*. 
- `sizeof` - Optional parameter. The size of the data blocks in the buffer. Recommended value: 255–4096. Default value: 255. The larger the value, the faster the read speed. Unit: byte.
- `ssl_params` - Optional parameter. The secret key information in the SSL authentication. Format: {"cert": certificate_content, "key": private_content}.

**Return Value**

- A response object containing all information returned by the server, such as response status codes, response headers, and response bodies.

### `request.post`

```python
response = requtes.post(url,data)
```

Sends a POST request.

**Parameter**

- `url` - Required parameter. The server IP address in the request.
- `data` - Optional parameter. Parameters to be carried in JSON format in the request.
- `headers` - Dictionary type. Optional parameter. The header information in the request.
- `decode` - Boolean type. Optional parameter. Decode the response result with UTF-8 after the request is successful. True: Decode. False: Not decode. Default value: True. Bytes will be returned if False is entered. This parameter is only used for *response.content*.
- `sizeof` - Optional parameter. The size of the data blocks in the buffer. Recommended value: 255–4096. Default value: 255. The larger the value, the faster the read speed. Unit: byte.

**Return Value**

- A response object containing all information returned by the server, such as response status codes, response headers, and response bodies.

**Content-Type Introduction:**

There are four types of data submitted in the POST method:

- application/x-www-form-urlencoded: The form data is encoded in key/value pairs and is sent to the server. It is the default type for the data submission in the form.
- multipart/form-data: This type is required for uploading files in the form.
- application/json: JSON format.
- application/octet-stream: Binary data stream. This type is used for downloading files.

### `request.put`

```python
response = requtes.put(url)
```

Sends a PUT request.

**Parameter**

- `url` - Required parameter. The server IP address in the request.
- `data` - Optional parameter. Parameters to be carried in JSON format in the request.
- `headers` - Dictionary type. Optional parameter. The header information in the request.
- `decode` - Boolean type. Optional parameter. Decode the response result with UTF-8 after the request is successful. True: Decode. False: Not decode. Default value: True. Bytes will be returned if False is entered. This parameter is only used for *response.content*.
- `sizeof` - Optional parameter. The size of the data blocks in the buffer. Recommended value: 255–4096. Default value: 255. The larger the value, the faster the read speed. Unit: byte.

**Return Value**

- A response object containing all information returned by the server, such as response status codes, response headers, and response bodies.

### `request.head`

```python
response = requtes.head(url)
```

Sends a HEAD request.

**Parameter**

- `url` - Required parameter. The server IP address in the request.
- `data` - Optional parameter. Parameters to be carried in JSON format in the request.
- `headers` - Dictionary type. Optional parameter. The header information in the request.
- `decode `- Boolean type. Optional parameter. Decode the response result with UTF-8 after the request is successful. True: Decode. False: Not decode. Default value: True. Bytes will be returned if False is entered. This parameter is only used for *response.content*.
- `sizeof` - Optional parameter. The size of the data blocks in the buffer. Recommended value: 255–4096. Default value: 255. The larger the value, the faster the read speed. Unit: byte.

**Return Value**

- A response object containing all information returned by the server, such as response status codes, response headers, and response bodies.

## Get Response

After the `request` library sends a request, a response object will be returned which contains all information sent by the server, such as response status codes, response headers, and response bodies.

### `response.status_code`

Gets the request status codes.

```python
response.status_code
```

**Return Value**

- Integer type. The request status codes.

**Example**

```python
import request

response = request.get("http://httpbin.org/get")
print(response.status_code)
```

### `response.headers`

Gets the request header.

```python
response.headers
```

**Return Value**

- Dict type. The request header.

**Example**

```python
import request

response = request.get("http://httpbin.org/get")
print(response.headers)
```

### `response.text`

Gets the text data of the response body.

```python
response.text
```

**Return Value**

- A generator object reading all returned text data through a for loop.

**Example**

```python
import request

response = request.get("http://httpbin.org/get")
for i in response.text:
    print(i)
```

### `response.content`

Gets the response body. 

```python
response.content
```

**Return Value**

- A generator object reading all returned response body data through a for loop.

**Example**

```python
import request

response = request.get("http://httpbin.org/get")
for i in response.content:
    print(i)
```

### `response.json`

Gets the response body in JSON format.

```python
response.json()
```

**Return Value**

- The response data in dictionary type.

**Example**

```python
import request

response = request.get("http://httpbin.org/get")
data = response.json()
print(data)
```

