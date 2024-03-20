from django.urls import path
from .views import comments_list


app_name = 'comments'

urlpatterns = [
    path('<int:id>/', comments_list, name='comments')
]