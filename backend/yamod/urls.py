from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_jwt.views import obtain_jwt_token

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1'
    ),
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('artist/options', views.artist_option_list),
    path('album/options', views.album_option_list),
    path('song/list', views.songs_list),
    path('song/create', views.song_form_create),
    path('song/<int:pk>/get', views.song_form_get),
    path('song/<int:pk>/update', views.song_form_update),
    path('song/<int:pk>/delete', views.song_delete),
    path('concert/list', views.concerts_list),
    path('concert/create', views.concert_form_create),
    path('concert/<int:pk>/get', views.concert_form_get),
    path('concert/<int:pk>/update', views.concert_form_update),
    path('concert/<int:pk>/delete', views.concert_delete),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api-token-auth/', obtain_jwt_token),
]
