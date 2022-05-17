from django.contrib import admin
from django.urls import path, include
from plants import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('plants.urls')),
  path('accounts/', include('django.contrib.auth.urls')),
  path('plants/<str:_search>/', views.detail, name='detail')
]
