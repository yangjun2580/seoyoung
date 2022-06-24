
from django.urls import path
from .views import UploadFeed, Profile, UploadReply, ToggleLike,ToggleBookmark, gallery, main2



urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('like', ToggleLike.as_view()),
    path('reply', UploadReply.as_view()),
    path('bookmark', ToggleBookmark.as_view()),
    path('profile', Profile.as_view()),
    path('gallery', gallery.as_view()),
    path('main2', main2.as_view())
    ]




