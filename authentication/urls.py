from django.urls import path 
from . import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [


    path('register/', views.RegisterView.as_view()),
    path('Profile/<doc>', views.MyProfileView.as_view()),

    # Login url
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

