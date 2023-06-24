from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns=[
    path('',views.f2,name="home"),
    path('analyze/<str:anatext>/',views.res,name="analyze"),
]