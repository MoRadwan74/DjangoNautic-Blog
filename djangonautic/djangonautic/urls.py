from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns     # This helps Django serve static files.
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # if we try to runserver then at the end of the address type /admin we can see the admin-login panel with username and password but actually we don't have those yet so let's create them.
    # In Terminal: python manage.py createsupreruser and add your credentials. Then runserver again and access using the credentials you have entered.
    # We can see that our articles are not showing up as we didn't told django-admin to make them appear in the admin-area. So we need to do this in the directory articles/admin.py
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about),     # $ means that this must be the end of the string. Ended with /about/.
    path('', views.homepage),   # This is for the Home page.
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)