# How to secure the API end points

Welcome to the Modern Application Development - 2 Screencasts. In this screencast we will see how to setup vue in a simple flask app.

- Terminal
- Browser
- Editor
- Python

# Simple Approach
Done by bringing the vue like any other library. Use it inside HTML or Jinja templates. Use where it is required.

- Diagram
    - API
    - Intial page can be redered by jinja or could be a simple html too
    - Everything else happens on vue
    - It's a mixed approach

Pro:
- Simple as everything is together
- Simple deployment
- You can use Cookie based login or token based login. As they are sure to be on the same server.
- You can mix match

Con: 
- You have to import Vue on and set up each page individually. Or you have to set it up in the base template
- Some of CLI based tooling

Where to use:
    - Good for simple apps where everything lives together
    - Good for apps where you want to use certain parts of the app to vue, certain parts of the app reactive
    - Good for app which are trying to migrate some parts of the app
    - An app where you dont want to do sinle page apps. For an highly accessible app. 
     - https://www.gatsbyjs.com/blog/2019-07-11-user-testing-accessible-client-routing/
     - https://dev.to/s_aitchison/page-titles-and-a11y-in-single-page-applications-esp-react-vue-4ok8

# Escaping

```html
<p>
{% raw %}
    {{ msg }}
{% endraw %}
</p>
```

or use other delimeters
// Delimiters changed to ES6 template string style

```
delimiters: ['${', '}']
```

```
${msg}
```
