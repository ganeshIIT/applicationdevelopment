# Webhooks

Welcome to the Modern Application Development - 2 Screencasts. In this screencast we will see how to use webhooks

- You will need Linux env
- You will have to install and run the Redis. We are going to use it. 

https://requestbin.com/blog/working-with-webhooks/

## Why
Server side push events.

Instead of one server asking other server details. One server sends the details to other server as the event happens.

When something happens on one server it sends the details to another server.

- something - event
- details - payload - usually JSON
- sending server - provider
- receiving server - consumer
- medium - HTTP Post
- Validation - in headers

Its also called HTTP Callback.

# Popular webhook providers
- Courier or Shipping
    - status updates

- Stripe/RazorPay
    - https://stripe.com/docs/webhooks
    - https://razorpay.com/docs/webhooks/
- Gitlab/Github
     - https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks
     - https://docs.gitlab.com/ee/user/project/integrations/webhooks.html


# How is it different from API calls
- Push instead of pull
- It uses existing technology, no new technologies

# Setup a controller

# Study the input

# Use the input

# What if its long
- Add to queue and start a async job