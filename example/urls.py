from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	path(r'example_get/<str:var_a>/<int:var_b>',  views.example_get),
	path(r'example_post/', views.example_post),
    path(r'example_post1/', views.example_post1),
    path(r'fib/', views.fib),
    path(r'get/<str:city>/',views.get),
    path(r'addSine/',views.addSine),
    path(r'curve/',views.curve),
    path(r'pointlist/',views.pointlist),
    path(r'number/',views.number)
]