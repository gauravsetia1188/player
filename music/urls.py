from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    url(r'^$',views.IndexView, name="index"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^thanks/$', views.thankyou, name="thanks"),
    url(r'^signin/$', views.Signin.as_view(), name="signin"),
    url(r'^login/$', views.login_user, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^addalbum/$', views.add_album.as_view(), name="addalbum"),
    url(r'^songs/$', views.songs, name="songs"),
    url(r'^addsong/$', views.addsong.as_view(), name="addsong"),
    url(r'^albums/$', views.albums, name="albums"),
    url(r'^albums/details/(?P<pk>[0-9]+)/$', views.details.as_view(),name="details"),
    url(r'^albums/delete/(?P<pk>[0-9]+)/$', views.songdelete, name="deletesong"),

]


