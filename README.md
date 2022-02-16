# PublicDiscussion

____
clone docker_compose branch

```
docker-compose up --build 
```

```
docker-compose up -d
```

```
docker-compose exec web python manage.py collectstatic 
```

```
docker-compose exec web python manage.py migrate --noinput 
```

```
docker-compose exec web python manage.py createsuperuser 
```
