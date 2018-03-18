# webinspect 
Simple web server for inspecting (echo) incoming HTTP requests

## Run server
```sh
docker run -p 8080:8080 cxmcc/webinspect
```

## Example Output

* Visit from browser
```
=== path ===
/
=== remote_address ===
127.0.0.1
=== headers ===
Cookie: cookiename=cookievalue
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36
Connection: keep-alive
Dnt: 1
Host: www.example.com
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
=== cookies ===
cookiename: cookievalue
=== data ===

```

* curl
```
$ curl localhost:8080
=== path ===
/
=== remote_address ===
127.0.0.1
=== headers ===
User-Agent: curl/7.47.0
Host: localhost:8080
Accept: */*
=== cookies ===
=== data ===

```
