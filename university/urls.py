
from django.contrib import admin
from django.urls import path
from courses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fanlar/', All_Fan),
    path('yonalishlar/', All_Yonalish),
    path('ustozlar/', All_Ustoz),
    path('ustoz/<int:u>/', ustoz_ochir),
    path('yonalish/<int:y_o>/', yonalish_ochir),
    path('fan/<int:fan>/', fan_ochir),
    path('yonalish/<int:pk>/edit/', yonalish_edit),
    path('ustoz/<int:pk>/edit/', ustoz_edit),
]
