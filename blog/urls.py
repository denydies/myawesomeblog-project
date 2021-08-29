from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_blog, name='posts'),
    path('<int:post_id>', views.show_post, name='show_post'),
]