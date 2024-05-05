
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),

#edit-roshan path added 
    path('', include('webapp.urls')),
]
