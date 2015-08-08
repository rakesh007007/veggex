from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from veggex import views
from django.contrib.staticfiles.urls import *
from startup.settings import *
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^try', views.tryy),
    url(r'^login', views.login),
    url(r'^logPost', views.logPost),
    url(r'^logout', views.logout),
    url(r'^main', views.main),
    url(r'^categoryView', views.categoryView),
    url(r'^addtocart', views.addtocart),
    url(r'^cart', views.cart),
    url(r'^removeItemPost', views.removeItemPost),
    url(r'^orderStep1', views.orderStep1),
    url(r'^makeOrder', views.makeOrder),
    url(r'^seeOrder', views.seeOrder),
    url(r'^account', views.account),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)