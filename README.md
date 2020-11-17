# server

## Server setup
### Create venv
```
server > python -m venv venv
```
### Activate venv
```
server > .\venv\Scripts\activate
```
### Install dependencies
With `venv` acttive
```
server > pip install -r requirements.txt
```

## Run the server
With `venv` acttive
```
server > py .\server.py
```

## Run the unit tests
With `venv` acttive
```
server > py .\test.py -v
```

# client

## Client setup
### Install dependencies
```
client > npm install
```

## Run the client
### Compiles and hot-reloads for development
```
client > npm run serve
```

### Compiles and minifies for production
```
client > npm run build
```

## Run the unit tests
```
client > npm run test:unit
```
