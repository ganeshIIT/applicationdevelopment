# Push messages using - server-sent events

Welcome to the Modern Application Development - 2 Screencasts. In this screencast we will see how to push events from server.

- You will need Linux env
- You will have to install and run the Redis. We are going to use it. 



## Why
Cricket score.

# What is SSE
Traditionally, a web page has to send a request to the server to receive new data; that is, the page requests data from the server. With server-sent events, it's possible for a server to send new data to a web page at any time, by pushing messages to the web page. These incoming messages can be treated as Events + data inside the web page.

https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events


Supported in all browsers except IE.


# Install and setup


## Server side
https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format

```
"Content-Type: text/event-stream"
```
Data in the body

```
event: usermessage
data: {"username": "sean", "time": "02:34:36", "text": "Bye, bobby."}
```

Each message received has some combination of the following fields, one per line:

event - A string identifying the type of event described. A client can use addEventListener() to listen for named events. 

data - The data field for the message. Text

id - ID

retry - The reconnection time. If the connection to the server is lost, the browser will wait for the specified time before attempting to reconnect.

## Client side

https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events

```javascript
const evtSource = new EventSource("//api.example.com/ssedemo.php", { withCredentials: true } );
```

# Running
## Simple Controller and EventSource

## With Vue
https://bestofvue.com/repo/tserkov-vue-sse-vuejs-server-side-rendering
https://github.com/tserkov/vue-sse

# Log Running Job updates
## With Celery


# Advanced
https://flask-sse.readthedocs.io/en/latest/advanced.html
## Channels
Channel names can be any string you want, and are created dynamically as soon as they are referenced. The default channel name that Flask-SSE uses is “sse”.

```python
sse.publish({"user": "alice", "status": "Life is good!"}, channel="users.social")
```

On client. The url will change

Default will be
```javascript
 source = new EventSource("/stream");
```

Spcific channel will be
```javascript
 source = new EventSource("/stream?channel=users.social");
```
or you can use

```python
url_for("sse.stream", channel="users.social")
```

## Auth

Before allowing the user to subsrcibe to a channel. Check Auth.

```
@sse.before_request
def check_access():
    if request.args.get("channel") == "analytics" and not g.user.is_admin():
        abort(403)

app.register_blueprint(sse, url_prefix='/sse')
```

