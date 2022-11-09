# How to secure the API end points

Welcome to the Modern Application Development - 2 Screencasts. In this screencast we will add Token based authentication to our APIs.

- Terminal
- Browser
- Editor
- Python

# Upgrade
- Upgrade the Flask Security to new package. Almost all of the things remain the same. It's a fork and maintianed version. So we will use that.


# Cookie based login
- Like usual once you login, you dont need to do anything special. You can just use it along with sending cookie. By default it goes as its the same domain.

if you are using the Fetch call then use, 'same-origin'

https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials

```javascript
fetch("http://localhost:8080/api/test", {credentials: "same-origin"})
  .then(response => response.json())
  .then(data => console.log(data));


fetch("http://localhost:8080/api/test", {credentials: "include"})
  .then(response => response.json())
  .then(data => console.log(data));

```

For example you can login first, then you can do cookie based using

http://localhost:8080/api/test


# Auth Token based

## Update the Package

- Old: https://pythonhosted.org/Flask-Security/
- New: https://flask-security-too.readthedocs.io/en/stable/

## Use Toke based
https://github.com/mattupstate/flask-security/tree/develop/flask_security
https://flask-security-too.readthedocs.io/en/stable/features.html#token-authentication


## Config
-  WTF_CSRF_ENABLED = False
-  SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
-  Add new column - fs_uniquifier

```sh
openssl rand -base64 12
openssl rand -hex 12
```

Use

```python
@auth_required("token")
```



curl --request POST \
  --url http://localhost:8080/api/article_likes \
  --header 'Authentication-Token: WyJhc2Rhc2RzZHMiXQ.YgQMvA.kp0XF4OrI6cvmKva1tMCp3e27T4' \
  --header 'Content-Type: application/json' \
  --data '{
    "article_id" : 1
}'