
# Secret Message

This WebApp allows you to create messages and set a password to your messages, so that others can view your message by entering the correct password of that message.
                     It provides you a unique link of the message you create, which you can share it to anyone whom you want to see that message and they can view your message by entering the password you created for that message.

**[💻 Visit WebApp -->](https://secretmessage.pythonanywhere.com/)**


## API Reference

#### Show Message History

```http
  GET /api/message-history/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Show Message

```http
  POST /api/message/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`  `api_key` | `string` | **Required**. Id of item to fetch and Your API key. |

#### Create Message

```http
  POST /api/message-create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `data`  `api_key` | `string` | **Required**. Data to create message and Your API key. |


## Demo

[🖥️ View Demo -->]()


## Usage/Examples

#### Create Message
```
import request

url = "API Url"

# Add Your Token Key in the header
header = {
    "Authorization" : "Token YOUR_TOKEN_KEY"
   }

# Data needed to create the message
data = {
        "body" : "YOUR TEXT MESSAGE",
        "file" : None,
        "password" : "CREATE THE PASSWORD FOR THIS MESSAGE"
        }

response = requests.post(
                url, 
                headers = header, 
                data = data
            )
print(response.json())
```

#### Show Message
```
import request

url = "API Url"

# Add Your Token Key in the header
header = {
    "Authorization" : "Token YOUR_TOKEN_KEY"
   }

# Password of the message 
data = {
        "password" : "Message_Password"
       }

# If the message belongs to the other person.
try:
    response = request.post(
                 url,
                 headers = header,
                 data = data
             )
# If the message belongs to yourself.
except:
    response = requests.post(
                url, 
                headers = header, 
            )
print(response.json())
```

#### Message History
```
import request

url = "API Url"

# Add Your Token Key in the header
header = {
    "Authorization" : "Token YOUR_TOKEN_KEY"
   }

response = requests.get(
                url, 
                headers = header,
            )
print(response.json())
```






## Author

- [@PurpleBird7613](https://purplebird.pythonanywhere.com/)

