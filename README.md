# URL Encoder

Used to encode all possible characters of a URL.

Example: 
```
Insert a URL: https://www.google.com/search?q=github
%77%77%77.%67%6F%6F%67%6C%65.%63%6F%6D/%73%65%61%72%63%68?%71=%67%69%74%68%75%62
```

When pasted into the browser URL field, it's automatically decoded back to the original URL.

It can be used in XSS or Open Redirect payloads, to hide the real content of the link.
