"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from students.views import get_students, index, create_student, update_student
from groups.views import get_group, create_groups, update_groups
from teachers.views import get_teachers, create_teacher, update_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('students/', get_students, name='get_students'),
    path('groups/', get_group, name='get_group'),
    path('teachers/', get_teachers, name='get_teachers'),
    path('students/create/', create_student, name='create_student'),
    path('teachers/create/', create_teacher, name='create_teacher'),
    path('groups/create/', create_groups, name='create_group'),
    path('students/update/<int:pk>/', update_student, name='update_student'),
    path('groups/update/<int:pk>/', update_groups, name='update_group'),
    path('teachers/update/<int:pk>/', update_teacher, name='update_teacher'),

]
