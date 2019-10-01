"""""
            <<< Here, we talk about Models >>>
    - A Model is a class which represent a table in a database.
    - Each type of data we have (e.g. Articles, Users, Books...) is represented by it's own model.
    - Each model maps to a single table in a database.

For example:
------------
In the code:
    >> class Articles():
        title = models.CharField()  # CharField: small amount of text
        body = models.TextField()   # TextField: you guess !
In the Database:
    id    title    body
    ----------------------
    1     blah     blah blah blah blah
    2     blah2    blah blah blah blah
    3     blah3    blah blah blah blah 
    
So here we will create our models here.
The steps:
==========
1- Import the models from djanbo database.
>> from django.db import models

2- Create a class with the name of the model and pass "models.Modal" as an argument.
>> class modelName(models.Model):
    some code

2- Add the attributes you want using the models.xField() like below.
>> title = models.CharField()
Check the documentation of all fields: https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

3- If you run the following command in the terminal,
>> python manage.py runserver
You can see that we have a message that there're some built-in models which is created when the app is created so we need to migrate them before migrating our model.
>> In the Terminal: python manage.py migrate

4- Now we can migrate the created model to the database as well. But before running the migrate process, we need to make a migration file then migrate the changes. This file will track any changes we made to the model.
>> In the Terminal: python manage.py makemigrations
You will see inside your app, a folder which is called "migrations" which contains a file called "0001_initial.py". This file will have the changes we already made like adding the atrributes plus adding the Id of each added record.

5- Safely, we can now migrate these data (our model) like so,
>> In the Terminal: python manage.py migrate

<<< NOTE >>> Each time we change the model we need to issue the commands "makemigrations" and "migrate".
"""""

from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # When an article is created, auto_now_add will automatically add the time then to the date field.
    # add in Thumbnail, author
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):  # self is like this
        return self.title

    def snippet(self):
        return self.body[:50]   # This means just take the first characters from 0 to 50

"""""
$ ORM Section:
--------------
- Django ORM is basiclly the bridge between the code and the database. So we can use it to interact between the database and the model like (Save an instance) or (Retreive instance from the database...).

- Instead of do that in the code here, we will use Python Shell and make the commands there,
>> In the Terminal: python manage.py shell

- We can now import our model (AKA "Article" class) from articles folder >>> models.py
>> from articles.models import Article

- If we type >> "Article" we get, articles.models.Article which represents the class.

- Let's say we want to retreive all of the objects inside the table,
>> Article.objects.all()

- This will output something like this "<QuerySet []>" which indicates there's no objects.

- So let's create a new object of Article
>> article = Article()

- Now if we call >> "article" we get "<Article: Article object (None)>" indicating an existing object but without initializing its attributes.

- We can set title to it,
>> article.title = "Hello World"

- If we try to output it like that >> "article.title" we get "Hello World".

- Then we need to save this to the database so easily we type,
>> articles.save()

- Now if we try to retrieve all the objects of Article class again by typing,
>> Article.objects.all()

- We get "<QuerySet [<Article: Article object (1)>]>"

- We can retrieve the title like so,
>> Article.objects.all()[0].title

- Which will print, "Hello World"

- When we retrieve the query set using this "Article.objects.all()" and we have for example, five objects we may see something like that "<QuerySet [<Article: Article object (1) Article object (2)...>]>" and it will be a nightmare.

- So it will be nice if the query result is the title of the object. Exit from the shell for now.

- Let's try to add a function that will make the look of the object (in both, admin section and shell) as the title instead of "Article object (id)". There's a built-in function for that called "__str__"
>> def __str__(self):
    return self.title

- Now if we query the objects, it will show the title of each instance object.

- If we try to go to the shell again and query the objects, we can see that each instance is labelled by its own title. Of course you can try to add another article object for example "article2" and try to output all of them.
"""""

"""""
Model Methods:
==============
- So far we are outputting the whole article in articles much might seem not quite right. Usually, the we see just a snippet of the article not the whole of it.

- So we need a method that cut part of the article and show the rest only.
"""""