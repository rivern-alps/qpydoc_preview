## About document

* **Revision history**

| Version | Date       | Author | Description     |
| ------- | ---------- | ------ | --------------- |
| 1.0     | 2021-04-07 | Chic   | Initial Version |
| 1.1     | 2021-09-06 | Chic   | Initial Version |



## Introduction on Encryption

MD5, SHA1 and SHA256, one-way hash function, are commonly used. Currently, it is SHA256 algorithm that is used frequently. 

**Three Features**

1. **Convert the data of arbitrary length into that with fixed length**
     (Whether the inputted data is 1 bit or 100,000,000 bits, the length of outputted data is fixed. For detailed length, we should adhere to different algorithm. Take MD5 as an example, the outputted length is 128 bits)

2.  **Strong Anti-collision** 
     The unique outcome, that means it is nearly impossible for you to find the same H(x1)=H(x2).

3.  **Irreversibility**
    
    It is unachievable to find out the corresponding inputted value via hash, that means, you can't find out the corresponding X via the value of H(X).

Capability supported by QuecPython module: Fulfill the hash algorithm of binary data such as MD5, SHA 1 and SHA256. 

Take the 60M file as the test sample and calculate the average time after 1000 times test,  please check the outcomes: 

- **MD5**            The average time for running 1000 times is 226ms

- **SHA1**           The average time for running 1000 times is 308ms

- **SHA256**       The average time for running 1000 times is 473ms


From the perspective of security, it is suggested to use SHA256 Also named SHA2) for its highest security level. 

## Common Applicable Scenarios

1. **Save user password in database**

   Since if the account password of user is displayed with a way of plain-text, there is a high risk and irresponsibility under the circumstance that tons of materials are exposed. The most appropriate way is to input the user password into database via one-way bash function, as a result, it is simple to compare the hash value when login. As the one-way hash function is irreversible, even if the database is stolen, it is still a failure to get the user info.

   Some so-called websites declared that they have decrypted one-way hash function. However,  it is a fake new; what they deployed is just the enumeration of lower level. It is inappropriate to save too much hash value of common plain-text. Actually, there are multiply ways to handle it such as "adding salt "- add characters like "$%*^&" to the end of user info uniformly, then calculate the hash value and save into database, or you can count the hash value of itself,  which can ensure the security at maximum. 

2. **Prevent Malicious Modification**

   Currently, most of websites that providing download service will have the SHA256 value of file accompanying since the one-way hash function is equipped with the anti-modification. If the file SHA256 is not complied with the value provided by website after downloading, which means the file has been modified maliciously or virus or piracy included. In addition, we will count the file SHA256 in the sequent codes.  

3. **Data Signature (Aliyun and Tencent Cloud)**

   Data signature and stamp,  a behavior that used in data signature actually, will be worked in digital area also. Since it is time-consuming during the process of data signature, we will calculate the hash value of info via one-way hash function beforehand instead of using data signature on the whole info directly, then encrypt this hash value via private key, the data signature will be received. 

4. **Pseudo-random Number Generator**

   It is also available to use one-way hash function to build pseudo-random number generator. 

   The random number used in encryption should be implement with attribute of impossibility to predict the future random array according to previous random array actually. In order to assure the unpredictability, the "one-way" characteristic should be deployed.

5.  **Transient Transmission**

   Actually, the transient transmission has been widely used in Cloud storage by certain companies for the characteristics of one-way hash function. 

   Generally，the one-way hash way is as similar as the file footprint. When the user uploads file, it will count the one-way hash value and check it over on the database. If there exists the same value, which proves that there is the same file as that uploaded by user, as a result, you just share it without uploading it again. By this way, it can reduce the bearer of the server heavily as well as the storage. 

 

## Encrypt Binary Data

Demo Codes

```python
import uhashlib
import ubinascii
# Temporarily, it supoorts md5, sha1, sha256 only

data = b"QuecPython"  # Data going to encrypt
data2 = b"QuecPython"  # Data going to encrypt

hash_obj = uhashlib.md5()
hash_obj.update(data)
# hash_obj.update(data2)
res = hash_obj.digest()
hex_msg = ubinascii.hexlify(res)
print("Data encrypted by md5：", hex_msg)
# b'37b8419ee7cdb3c64d7e66019216117c'

hash_obj = uhashlib.sha1()
hash_obj.update(data)
# hash_obj.update(data2)
res = hash_obj.digest()
hex_msg = ubinascii.hexlify(res)
print("Data encrypted by sha1：", hex_msg)
# b'614a4247ef68e9f9793e11353cc86acb932badab'

hash_obj = uhashlib.sha256()
hash_obj.update(data)
# hash_obj.update(data2)
res = hash_obj.digest()
hex_msg = ubinascii.hexlify(res)
print("Data encrypted by sha256：", hex_msg)
# b'1ec66771b3a9ac3ea4c44f009e545797d42e9e7d426fff8275895468fe27c6cd'

res = b'\x11\x22\x33123'
print("Origial data：", res)
res = ubinascii.b2a_base64(res)
print("Compile base64 data：", res)
res = ubinascii.a2b_base64(res)
print("Retrive base64 data：", res)

```

The following figure displays the executed result.

![image-20210906190809839](media\image-20210906190809839.png)



## Others 

**For more info, please refer to the official website**

https://python.quectel.com/wiki/#/zh-cn/api/?id=pin

**Official website**

https://python.quectel.com/

**For related tools, routines, drivers and files, please download via address as described below.**

https://python.quectel.com/download

Or you can also follow QuecPython Wechat official account. 

 

 