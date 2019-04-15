from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('home/', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('login/', views.login, name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    #url(r'^logout/$', views.logout, name='logout'),	
    path('auth/', include('social_django.urls', namespace='social')),  # <- Here
]