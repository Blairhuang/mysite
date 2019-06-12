from django.urls import path
from .import views
from .views import PostListView
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'),#as_view()作用是把postlistview 转化成实际视图
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'), 
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'), #post/<int:primarykey> 例如post/1
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('about/', views.about, name='blog-about')
]

# <app>/<model>_<viewtype>.html-------== blog/post_list.html  按照error 的显示 ，网页默认查找的途径为 blog/<model=post>_detail.html