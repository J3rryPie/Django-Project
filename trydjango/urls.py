"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, about_view, ans_view, form_create_view, forum_view, register_view, logout_view, \
    login_request
# from products.views import product_view,product_create_view,dynamic_lookup_view,product_delete_view,all_product_details
from csi_student.views import all_students_details, chat_window_view, about_me,edit_profile
from projects.views import all_projects, one_project_view, create_project_view
from curri.views import curri_view, all_curri  # ,get_queryset
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    # path('create/',product_create_view),
 # path('product/',product_view),
 # path('about/',about_view),
    path('admin/', admin.site.urls),
 # path('products/<int:id>/',dynamic_lookup_view,name='product'),
 # path('products/<int:id>/delete',product_delete_view,name='product_delete'),
 # path('products/all_products',all_product_details,name='all_products'),
    path(r'students/chat/', all_students_details, name='all_students'),
    path(r'students/<int:id>/', about_me, name='about_me'),
    path(r'students/update/<int:id>/', edit_profile, name='edit_profile'),
    path(r'students/chat/<int:id>', chat_window_view, name='chat window'),
    path(r'forum/<int:id>/', ans_view, name='ans_view'),
    path(r'forum/', forum_view, name='forum_view'),
    path(r'forum/create/', form_create_view, name='form_create_view'),
 # path('projects/',all_projects,name='all projects'),
    path(r'projects/', all_projects, name='all_projects'),
    path(r'projects/create/', create_project_view, name='create_project'),
    path(r'projects/<int:id>/', one_project_view, name='one_project'),
    path(r'curriculum/', curri_view, name='curri_view'),
    path(r'search/', curri_view, name='get_queryset'),
    path(r'tinymce/', include('tinymce.urls')),
    path(r'register/', register_view, name='register_view'),
    path(r'logout/', logout_view, name='logout_view'),
    path(r'login/', login_request, name='login_view'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
