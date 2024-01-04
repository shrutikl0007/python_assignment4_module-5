
# Q-5 : What is a QuerySet? Write program to create a new Post object in database:

# ans:

# A QuerySet is a collection of data from a database.
# A QuerySet is built up as a list of objects.
# QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage.

# Create object:

# create a new Post object in database:
# Post.objects.create(author=User, title='Sample title', text='Test')

# import User model first:
# from django.contrib.auth.models import User

# User.objects.all()
# User = User.objects.get(username='username')
# Post.objects.filter(title__contains='title')
