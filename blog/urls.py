from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<slug:tag_slug>', views.index, name='index_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.show, name='show'),
    path('<int:post_id>/share', views.post_share, name='post_share'),
]
