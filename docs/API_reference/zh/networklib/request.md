# request - HTTP客户端

`request`模块用于向服务器发起 HTTP 请求，它可以被用于从一个服务器获取数据，或者将数据提交到服务器上，支持多种请求方法（如 GET、POST、PUT等）。

## HTTP请求

### `request.get`

```python
response = requtes.get(url)
```

发送GET请求。

**参数描述：**

- `url`- 必填参数，请求的远端地址。
- `data`-可选参数，请求中需要携带参数，JSON格式。
- `headers`-可选参数，请求头信息，字典类型。
- `decode`-可选参数，将请求成功后的响应结果解码（UTF8），默认为True,输入False则返回bytes，仅配合response.content使用。
- `sizeof`-可选参数，读取缓冲区的数据块大小，默认255 个字节，建议255-4096， 数值越大读取的速度越快。
- `ssl_params`-可选参数，SSL认证时传入密钥，格式为{"cert": certificate_content, "key": private_content} 

**返回值描述：**

- 返回响应对象，对象包含了服务器返回的所有信息，例如响应状态码、响应头、响应体等。

### `request.post`

```python
response = requtes.post(url,data)
```

发送POST请求。

**参数描述：**

- `url`- 必填参数，请求的远端地址。
- `data`-可选参数，请求中需要携带的参数，JSON格式。
- `headers`-可选参数，请求头信息，字典类型。
- `decode`-可选参数，将请求成功后的响应结果解码（UTF8），默认为True,输入False则返回bytes，仅配合response.content使用。
- `sizeof`-可选参数，读取缓冲区的数据块大小，默认255 个字节，建议255-4096， 数值越大读取的速度越快。

**返回值描述：**

- 返回响应对象，对象包含了服务器返回的所有信息，例如响应状态码、响应头、响应体等。

**Content-Type介绍：**

当使用POST方法提交数据时，对于提交的数据主要有如下四种形式：

- application/x-www-form-urlencoded：form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）
- multipart/form-data ： 需要在表单中进行文件上传时，就需要使用该格式
- application/json： JSON数据格式
- application/octet-stream ： 二进制流数据（如常见的文件下载）

**示例：**

```python
import request

url = "http://httpbin.org/post"
data = {"key1": "value1", "key2": "value2", "key3": "value3"}
resp = request.post(url, data=ujson.dumps(data))

for i in resp.text:
    print(i)

```


### `request.put`

```python
response = request.put(url)
```

发送PUT请求。

**参数描述：**

- `url`- 必填参数，请求的远端地址。
- `data`-可选参数，请求中需要携带的参数，JSON格式。
- `headers`-可选参数，请求头信息，字典类型。
- `decode`-可选参数，将请求成功后的响应结果解码（UTF8），默认为True,输入False则返回bytes，仅配合response.content使用。
- `sizeof`-可选参数，读取缓冲区的数据块大小，默认255 个字节，建议255-4096， 数值越大读取的速度越快。

**返回值描述：**

- 返回响应对象，对象包含了服务器返回的所有信息，例如响应状态码、响应头、响应体等。

### `request.head`

```python
response = request.head(url)
```

发送HEAD请求。

**参数描述：**

- `url`- 必填参数，请求的远端地址。
- `data`-可选参数，请求中需要携带的参数，JSON格式。
- `headers`-可选参数，请求头信息，字典类型。
- `decode`-可选参数，将请求成功后的响应结果解码（UTF8），默认为True,输入False则返回bytes，仅配合response.content使用。
- `sizeof`-可选参数，读取缓冲区的数据块大小，默认255 个字节，建议255-4096， 数值越大读取的速度越快。

**返回值描述：**

- 返回响应对象，对象包含了服务器返回的所有信息，例如响应状态码、响应头、响应体等。

## 获取响应

`request` 库发送请求后，会返回一个响应对象。响应对象包含了服务器返回的所有信息，例如响应状态码、响应头、响应体等。

### `response.status_code`

使用 `response.status_code` 属性获取响应状态码。

```python
response.status_code
```

**返回值描述：**

- int类型，请求状态码

**示例：**

```python
import request

response = request.get("http://httpbin.org/get")
print(response.status_code)
```

### `response.headers`

使用 `response.headers` 属性获取响应头信息。

```python
response.headers
```

**返回值描述：**

- dict类型，请求头信息

**示例：**

```python
import request

response = request.get("http://httpbin.org/get")
print(response.headers)
```

### `response.text`

使用 `response.text` 属性获取响应体文本数据。

```python
response.text
```

**返回值描述：**

- 生成器对象，通过for遍历读取全部返回的文本数据

**示例：**

```python
import request

response = request.get("http://httpbin.org/get")
for i in response.text:
    print(i)
```

### `response.content`

使用 `response.content` 属性获取响应体信息。

```python
response.content
```

**返回值描述：**

- 生成器对象，通过for遍历读取全部返回的响应体数据

**示例：**

```python
import request

response = request.get("http://httpbin.org/get")
for i in response.content:
    print(i)
```

### `response.json`

使用 `response.json` 属性获取JSON类型的响应体信息。

```python
response.json()
```

**返回值描述：**

- 字典类型的响应体数据

**示例：**

```python
import request

response = request.get("http://httpbin.org/get")
data = response.json()
print(data)
```

