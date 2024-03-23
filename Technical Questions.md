Technical Questions
A user is attempting to access a resource at a specific api endpoint.
The server response has a status code of `403 Forbidden`.
The user is asking us what's wrong, what would your initial thoughts/response be?
1. The user have not the qualified role(role based)
2. No permissions
3. IP blacklist

First, I tell to the user if he provided a correct authentification credentials
to access this ressource like user/password combination, tokens or API keys. And if
he has a valid credentials, perhaps he hasn't permissions to access pyththis resource,
server may be configured to restrict access based on user roles, group, or other
authorization settings.

We have a Postgres table that is getting too big and queries are slowing down significantly.
What are some steps we could take to optimize this table?
1.Indexing
2.Partitiong
3.

Users are allowed to upload ads through our api. Ads require additional processing, such as compression, harvesting metadata, etc. 
How would you handle time consuming processing of large media files through a RESTful api?
