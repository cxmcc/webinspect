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
=== method===
GET
=== remote_address ===
127.0.0.1
=== headers ===
Cookie: cookiename=cookievalue
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Connection: keep-alive
Dnt: 1
Host: localhost:8080
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
=== cookies ===
cookiename: cookievalue
=== data ===

=== curl ===
curl http://localhost:8080/ --header "Cookie: cookiename=cookievalue" --header "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36" --header "Connection: keep-alive" --header "Dnt: 1" --header "Host: localhost:8080" --header "Upgrade-Insecure-Requests: 1" --header "Cache-Control: max-age=0" --header "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" --header "Accept-Language: en-US,en;q=0.9" --header "Accept-Encoding: gzip, deflate, br"
```

* curl
```
$ curl localhost:8080
$ curl localhost:8080
=== path ===
/
=== method===
GET
=== remote_address ===
127.0.0.1
=== headers ===
User-Agent: curl/7.47.0
Host: localhost:8080
Accept: */*
=== cookies ===
=== data ===

=== curl ===
curl http://localhost:8080/ --header "User-Agent: curl/7.47.0" --header "Host: localhost:8080" --header "Accept: */*"
```
