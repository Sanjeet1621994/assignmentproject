
# second step import settings and static as imported
#  below and add the media code as show below

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views
# add the media to the url pattern as done below
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='main project'),
                  path('shop/', include('shop.urls')),
                  path('blog/', include('blog.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
