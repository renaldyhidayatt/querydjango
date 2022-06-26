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

- Raw Query
```python
    query = Post.objects.raw("Select posts_post.id, posts_post.title from posts_post")
    for i in range:
        print(i.title)
```    
- Order_by
urutan asc dan desc
```python
    Post.objects.all().order_by("id") asc
    Post.objects.all().order_by("-id") desc
```

- Values
Returns a QuerySet that returns dictionaries, rather than model instances
```python
    Post.objects.values("id", "title")
```

- Only
Similar to values but returns model instance
```python
    Post.objects.only("id", "title")

```

- Defer
Exclude a particular column in the query
```python
    Category.objects.defer("description")
```

- Union
Uses SQL’s operator to combine the results of two or more s.UNIONQuerySet
```python
    q1 = Post.objects.filter(status="P").only("id", "title")
    q2 = Post.objects.filter(status="R").only("id", "title")
    q3 = Post.objects.filter(status="A").only("id", "title")

    q1.union(query2, query3)
```

- Intersection
Uses SQL’s operator to return the shared elements of two or more s.
```python
query1 = Category.objects.filter(name="Educational").only("name","description")
query2 = Category.objects.filter(status='P').only("name", "description")
query1.intersection(query2)

```

- Difference
Uses SQL’s EXCEPT operator to keep only elements present in the QuerySet but not in some other QuerySets.

```python
query1 = Category.objects.all().only("name")
query2 = Category.objects.filter(status='P').only("name")

query1.difference(query2)

```

- Exact
An exact match
```python
Comment.objects.filter(body__exact="nice post").only("id","post", "body")
```

- Contains
Case-sensitive containment test.

```python
Comment.objects.filter(body__contains="nice").only("id","post", "body")
```

- In
Matches one of the values

```python
list = [i for i in range(1,100) if i%2==0]
Post.objects.filter(id__in = list).only("id", "title")
```

- gt, gte, lt, lte
```python
Post.objects.filter(id__gt = 3)

Post.objects.filter(id__lt = 100)
```

- And, Or
A Q() object represents an SQL condition that can be used in database-related 
operations. 
Q Objects makes it possible to define and reuse conditions, and combine them using 
operators such as | (OR) and & (AND).

```python
from django.db.models import Q

Comment.objects.filter(Q(post = p1.id) | Q(post = p2.id)).only("id","body")

Comment.objects.filter(Q(body__contains = "nice") & Q(body__contains="post")).only("id","body")

Comment.objects.filter(~Q(commented_by="admin")).only("id", "body")


```

- Select Related
Returns a QuerySet that will “follow” foreign-key relationships, selecting additional related-object data when it executes its query.

```python
Category.objects.select_related(“created_by”).get(id=1)

```

- Prefetch_related
prefetch_related does a separate lookup for each relationship, and does the ‘joining’ in Python. This allows it to prefetch many-to-many and many-to-one objects, which cannot be done using select_related, in addition to the foreign key and one-to-one relationships that are supported by select_related

```python
Post.objects.prefetch_related("category").get(id=1)
```

- F
F( ) expressions makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.


```python
from django.db.models import F
from datetime import timedelta
Post.objects.filter(last_updated__gt = F("published_on") + timedelta(seconds=1))

```