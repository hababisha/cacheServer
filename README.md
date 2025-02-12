# cacheServer
A simple cache server in python.

The goal for this project is to be able to implement a very simple cache server inorder to learn&&understand how caching works.

Here’s a pseudo-code for a very basic HTTP server that can respond to GET requests:
- Wait for a request
  - When a request comes in, check what file it's looking for.
  - If we have it:
    - Great! Send it.
  - If we don't have it:
    - Send back a 404.


And Here’s the pseudocode for a very basic cache server:
- Wait for a request
  - When a request comes in, check what file it's looking for.
  - If we have it stored in the cache:
    - Send it.
  - If we don't have it in the cache:
    - Request it from the main server
    - If the main server has it:
      - Store a copy in the cache
      - Send the file to the client
    - If the main server does not have it:
      - Send a 404 to the client

# RESOURCES

https://alexanderell.is/posts/simple-cache-server-in-python/

https://joaoventura.net/blog/2017/python-webserver/

