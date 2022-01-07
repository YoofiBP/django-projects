from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.show, name='show'),
    path('<int:post_id>/share', views.post_share, name='post_share'),
]
