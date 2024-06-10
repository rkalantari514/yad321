from django.urls import path

from profile_page.views import profilepage

urlpatterns = [
    path('profile/<profileId>', profilepage, name="profile"),
    # path('profile/edit/<profileId>', EditProfile, name="editprofile"),


]