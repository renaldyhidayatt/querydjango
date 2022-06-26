## Query Django

### Migration
- Makemigrations
    which is responsible for creating new migrations based on the changes you have made to your models #(#https://docs.djangoproject.com/en/4.0/topics/migrations/)

    ```python
        python manage.py makemigrations
    ```
- migrate
    which is responsible for applying and unapplying migrations

    ```python
        python manage.py migrate
    ```
- sqlmigrate
    which displays the SQL statements for a migration
    ```python
        python manage.py sqlmigrate [Models] [migrations]
    ```
- showmigrations
    which lists a project’s migrations and their status
    ```python
        python manage.py showmigrations
    ```

### Create SuperUser
```python
    python manage.py createsuperuser
```

### Models
- create

  ```python
  c1 = Category.objects.create(name="Educational", description="Category descritption", created_by=u,status="P")

  c1.save()
  
  ```

- update
  ```python
    c1 = Category.objects.get(name="Educational")
    c1.name = "Educational"
    c1.description="Category"
    c1.status="R"
    c1.created_by=u
    c1.save()
  ```

- filter
  ```python
    Category.objects.get(name="Educational")
  ```

- getall by models Many to many
  ```python
    p1 = Post.objects.get(title="golang")
    p1.category.all()
  ```

- filter by models many to many
  ```python
    Post.objects.get(category__name="Educational")
  ```

- Following Relationship Backward
  ```python
    p1.comment_set.all()
  
  ```