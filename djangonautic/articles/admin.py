from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
# Now django knows that in the admin section, we want to see the articles.