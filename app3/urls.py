
from django.urls import path
from .views import *

urlpatterns = [
    # path('',view_,name = 'view'),
    path('view/',view_, name = 'view_'),
    path('create/', create_, name = 'create_'),
    path('delete/<int:id>/', dele , name = "delete1"),
    path('update/<int:id>/', update , name = "update1"),
]
    