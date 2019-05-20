from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    # Examples:
    # url(r'^$', 'testapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'admin/', admin.site.urls),
]
