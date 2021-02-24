New book query
```python
newbook = Book.objects.create(title = '', desc = '')

newbook1 = Book.objects.create(title = 'C Sharp', desc = '')
newbook2 = Book.objects.create(title = 'Java', desc = '')
newbook3 = Book.objects.create(title = 'Python', desc = '')
newbook4 = Book.objects.create(title = 'PHP', desc = '')
newbook5 = Book.objects.create(title = 'Ruby', desc = '')
```

New author query
```python
newauthor = Author.objects.create(first_name = '', last_name = '')

newauthor = Author.objects.create(first_name = 'Jane', last_name = 'Austen')
newauthor = Author.objects.create(first_name = 'Emily', last_name = 'Dickinson')
newauthor = Author.objects.create(first_name = 'Fyodor', last_name = 'Dostoevsky')
newauthor = Author.objects.create(first_name = 'Wiliam', last_name = 'Shakespeare')
newauthor = Author.objects.create(first_name = 'Lau', last_name = 'Tzu')
```

After adding a new text field "notes" ran these commands
```python
books_authors_proj> python manage.py makemigrations
books_authors_proj> python manage.py migrate
>>> from books_authors_app.models import *  
```

Query: Change the name of the C Sharp book to C#
```python
newbook1 = Book.objects.get(id=1)
newbook1.title = "C#"
print(newbook1.title)
newbook1.save()
```

Query: Change the first name of the 4th author to Bill
```python
newauthor = Author.objects.get(id=4)
newauthor.first_name = "Bill"
print(newauthor.first_name)
newauthor.save()
```

Query: Assign the first author to the first 2 books
```python
linkauthor = Author.objects.get(id=1)
linkbook = Book.objects.get(id=1)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=1)
linkbook = Book.objects.get(id=2)
linkauthor.books.add(linkbook)
linkauthor.books.all()
```

Query: Assign the second author to the first 3 books
```python
linkauthor = Author.objects.get(id=2)
linkbook = Book.objects.get(id=1)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=2)
linkbook = Book.objects.get(id=2)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=2)
linkbook = Book.objects.get(id=3)
linkauthor.books.add(linkbook)
linkauthor.books.all()
```

Query: Assign the third author to the first 4 books
```python
linkauthor = Author.objects.get(id=3)
linkbook = Book.objects.get(id=1)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=3)
linkbook = Book.objects.get(id=2)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=3)
linkbook = Book.objects.get(id=3)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=3)
linkbook = Book.objects.get(id=4)
linkauthor.books.add(linkbook)
linkauthor.books.all()
```

Query: Assign the fourth author to the first 5 books (or in other words, all the books)
```python
linkauthor = Author.objects.get(id=4)
linkbook = Book.objects.get(id=1)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=4)
linkbook = Book.objects.get(id=2)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=4)
linkbook = Book.objects.get(id=3)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=4)
linkbook = Book.objects.get(id=4)
linkauthor.books.add(linkbook)
linkauthor.books.all()
linkauthor = Author.objects.get(id=4)
linkbook = Book.objects.get(id=5)
linkauthor.books.add(linkbook)
linkauthor.books.all()
```

Query: Retrieve all the authors for the 3rd book
```python
linkbook = Book.objects.get(id=3)
>>> linkbook.link.all()  
<QuerySet [<Author: <Author object: Emily Dickinson(2)>>, <Author: <Author object: Fyodor Dostoevsky(3)>>, <Author: <Author object: Bill Shakespeare(4)>>]>
```

Query: Remove the first author of the 3rd book
```python
linkauthor = Author.objects.get(id=3)
linkbook = Book.objects.get(id=3)
linkauthor.books.remove(linkbook)
```

Query: Add the 5th author as one of the authors of the 2nd book
```python
linkauthor = Author.objects.get(id=5)
linkbook = Book.objects.get(id=2)
linkauthor.books.add(linkbook)
linkauthor.books.all()
```

Query: Find all the books that the 3rd author is part of
```python
linkauthor = Author.objects.get(id=3)
linkauthor.books.all()
```

Query: Find all the authors that contributed to the 5th book
```python
linkbook = Book.objects.get(id=5)

```