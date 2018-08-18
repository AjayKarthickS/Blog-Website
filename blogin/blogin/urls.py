from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as articles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^about/$',views.about,name='about'),
    url(r'^$',articles_views.article_list,name='home'),
    url(r'^articles/',include('articles.urls')),
    url(r'^accounts/',include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
