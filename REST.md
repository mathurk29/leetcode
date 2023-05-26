https://restfulapi.net/

https://support.smartbear.com/swaggerhub/docs/tutorials/index.html

https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html

https://support.smartbear.com/swaggerhub/docs/tutorials/writing-asyncapi-tutorial.html



What is REST API - A web svc that conform REST 

REST (REpresentational State Transfer) is an  architectural design for distributed hypermedia systems.

REST has six guiding principles (constraints):

1.  **Uniform Interface**:
    1. a resource in a system shoudl have a unique URI
    1. that URI should provide way to fetch additional/related data.
    1. all resources should be accessible through a common approach ex: HTTP GET
    1. 
1.  **Client- Server**: decoupled i.e. evolved separately as long as interface is not changed.
1.  **Stateless**: No session. No histroy. If the client application needs to be a stateful application for the end-user, where the user logs in once and does other authorized operations after that, then each request from the client should contain all the information necessary to service the request – including authentication and authorization details.

 
1.  **Cacheable**: cacheable resources MUST declare themselves so. caching can be done on both server or client side. ex Header having following attributes: Expires/Cache-Control/Etag/Last-Modified. 

        If a resource is available in cache - this is how client decides to go with cache or fresh request:

        While requesting a resource, client sends the ETag in If-None-Match header field to the server. The server matches the Etag of the requested resource and the value sent in If-None-Match header. If both values match the server sends back a 304 Not Modified status, without a body, which tells the client that the cached version of the response is still good to use (fresh).
Ref: https://learning.mlytics.com/the-internet/http-request-methods/ 



When both, the method of the request and the status of the response, 




1.  **Layered System**: Client do not know the backend layers. He only needs to know the facing server / gateway.
1.  **Code on Demand**: 



<BR>
<BR>
<BR>
<BR>

# HTTP 

https://learning.mlytics.com/origin-server/what-are-http-headers/



HTTP defines request methods to indicate the desired action to be performed for a given resource

## Safe Methods  

An HTTP method is safe if a request using this method doesn’t alter the state of the server. In other words, it leads to a read-only operation.

- safe methods: GET, HEAD, OPTIONS, TRACE
- unsafe methods: POST, PUT, DELETE, CONNECT, PATCH

Safe methods are also cacheable.


## Idempotent

An HTTP method is idempotent if multiple identical requests using this method will have the same effect on the server as that of a single request of that same method. In other words, an idempotent method should not have any side-effects, except for keeping logs and statistics. 

    All safe methods are also idempotent, but not all idempotent methods are safe


are cacheable, the response to the request can be cached.


### POST

The POST method requests to submit and process the representation enclosed in the request to a target resource

A POST request is typically sent via an HTML form and results in a change on the server.

The POST method is unsafe, non-idempotent, and cacheable only if freshness information is included.

201 Created
200 OK
204 No Content

### PUT

The PUT method requests to create a new resource or replaces a representation of the target resource with the state defined by the representation enclosed in the request (or request payload).

The PUT method is unsafe, idempotent, and non-cacheable.

201 Created if new resource
200 OK / 204 No content - if existing resource modified

### DELETED

200 OK - If a resource has been successfully deleted together with an **entity** describing what has been deleted,
204 No content - response does not include **entity**
202 Accepted - if queued
404 Not found

### OPTIONS
The supported HTTP methods are returned on the Allow header. 
