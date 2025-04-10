from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('',views.ques_feed),
    path('admin/', admin.site.urls),
    path('quora/',include('myapp.urls'),name = 'quora'),
    path('',include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)