from django.urls import path 
from . import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    #Register a new user url
    path('register/', views.RegisterView.as_view()),

    #Profile view url 
    path('Profile/<doc>', views.MyProfileView.as_view()),
    path('Profile/update/<Documento>', views.UpdateProfileView.as_view()),

    # Login url -> function for logging in
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

