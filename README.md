# Welcome to drf_test_task!

# Quick start with Docker 

1) Open `docker-compose.yml`

2) Update `DJANGO_SECRET_KEY` here:
```
	environment:
      - DEBUG=1
      - DJANGO_SECRET_KEY=""
```

3) `docker compose up --build` in your terminal

4) `localhost:8000` in your browser

Once set up, an admin user with `username=admin` and `password=12345` is automatically created.

# API Routes 

Once your project is set up, your are allowed to use `api/v1/` Routes. These include:

1) GET `api/v1/items/` - List of all items 
2) GET `api/v1/items/{id}` - Detail view of item 

# API Filters 

When requesting to `LIST Routes`, you can put `_filter` object in the body of your request and write `Django ORM` filter queries as values. This is an example of body:

```
GET {{host}}/api/v1/items/

BODY:
{
    "_filter": {
        "title__startswith": "Test"
    }
}
```




