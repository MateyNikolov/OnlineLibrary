from django.urls import path, include

from onlineLibrary.web.views import show_home_page, add_book, edit_book, details_book, show_profile, edit_profile, \
    delete_profile

urlpatterns = [
    path('', show_home_page, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', details_book, name='details book'),
    path('profile/', include([
        path('', show_profile, name='profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]