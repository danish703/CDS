from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),#homepage
    path('analysis/',views.analysis,name='analysis')
]
