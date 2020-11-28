# A test implementation/blueprint for celery workers

The python code is not very interessting. The main purpose of the project was to test a configuration to easily build up a test setup with docker-compose

## Dependencies 🛠
Since all code is executed in containers the only dependency is Docker and docker-compose.

## How to use 🚀
### 1. Clone the Repos
````
git clone https://github.com/Newmi1988/fastapi-celery
````

### 2. Simply run 
```
docker-compose build 
```
followed by 
```
docker-compose up
```

### 3. FastAPI (open localhost:8080/docs)
Use the FastAPI Docs page to run the example on the workers

## TODO
- Add pydantic models for savety.
- Add helm charts and automate build for testing in k8s

## NOTE
The underlying modules using poetry to keep track of all the dependencies.

