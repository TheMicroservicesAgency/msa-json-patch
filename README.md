
# msa-json-patch

Microservice to generate a diff ([RFC 6902](https://tools.ietf.org/html/rfc6902)) between two json documents A & B, that can be also used to transform/patch document A into document B.

If you have a given JSON document with a series of updates, this can be used to reduce the amount of data to send over the wire.

Built using [jsonpatch](https://pypi.python.org/pypi/jsonpatch).

## Quick start

Execute the microservice container with the following command :

    docker run -ti -p 9909:80 msagency/msa-json-patch

## Example(s)


    $ curl -X POST "http://localhost:9909/json/diff" -H "Content-Type: application/json" \
    -d '[{"name": "test","val": 10}, {"name": "test","val": 20}]'
    {
      "data": "[{\"op\": \"replace\", \"value\": 20, \"path\": \"/val\"}]"
    }

    $ curl -X POST "http://localhost:9909/json/patch" -H "Content-Type: application/json" \
    -d '[{"name": "test","val": 10}, [{ "op": "replace","path": "/val", "value": 20}]]'
    {
      "data": {
        "name": "test",
        "val": 20
      }
    }

## Endpoints

- POST [/json/diff]() : Returns a diff between two JSON documents A and B. Expected input is [A,B]
- POST [/json/patch]() : Returns the generated document B from patching the document A. Expected input is [A, patch]

## Standard endpoints

- GET [/ms/version](/ms/version) : returns the version number
- GET [/ms/name](/ms/name) : returns the name
- GET [/ms/readme.md](/ms/readme.md) : returns the readme (this file)
- GET [/ms/readme.html](/ms/readme.html) : returns the readme as html
- GET [/swagger/swagger.json](/swagger/swagger.json) : returns the swagger api documentation
- GET [/swagger/#/](/swagger/#/) : returns swagger-ui displaying the api documentation
- GET [/nginx/stats.json](/nginx/stats.json) : returns stats about Nginx
- GET [/nginx/stats.html](/nginx/stats.html) : returns a dashboard displaying the stats from Nginx

## About

A project by the [Microservices Agency](http://microservices.agency).
