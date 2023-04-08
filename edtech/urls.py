from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve

admin.site.site_header = "Edtech"
admin.site.site_title = "Edtech"
admin.site.index_title = "Edtech"


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/accounts/', include('api.v1.accounts.urls', namespace='api_v1_accounts')),
    path('api/v1/programs/', include('api.v1.programs.urls', namespace='api_v1_programs')),
    path('api/v1/discussions/', include('api.v1.discussions.urls', namespace='api_v1_discussions')),

    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_FILE_ROOT}),
]
