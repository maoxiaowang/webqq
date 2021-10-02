from django.urls import path
from zone.views import PostIndex, PostList, PostCreate, PostDelete

app_name = 'zone'

urlpatterns = [
    path('index/', PostIndex.as_view(), name='index'),
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/create/', PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='posts_delete')
]
