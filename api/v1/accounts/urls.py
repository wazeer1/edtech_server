from django.urls import path, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

app_name = "api_v1_accounts"


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', views.register_user, name='regiser_user'),
    path('login/', views.login_user, name='login_user'),
    path('minimal/', views.minimal, name='minimal'),
]
