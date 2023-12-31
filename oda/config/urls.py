from django.contrib import admin
from django.urls import path, include
from config.views import IndexView, comingsoon
from django.conf import settings
from django.conf.urls.static import static

# from wagtail.admin import urls as wagtailadmin_urls
# from wagtail import urls as wagtail_urls
# from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('adventure/', include('adventure.urls')),

    path('comingsoon/', comingsoon),
    
    # path('cms/', include(wagtailadmin_urls)),
    # path('documents/', include(wagtaildocs_urls)),
    # path('pages/', include(wagtail_urls)),
]

urlpatterns += static(
	prefix = settings.MEDIA_URL,
	document_root=settings.MEDIA_ROOT,
)

handler404 = 'config.views.page_not_found'
handler500 = 'config.views.internal_server_error'
