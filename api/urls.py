from django.urls import path

from api.views import GiftListView, GirlsListView, GiftDetailView, GirlsDetailView, PanjabiListView, PanjabiDetailView, \
    PantListView, PantDetailView, ShirtListView, ShirtDetailView, T_shirtListView, T_shirtDetailView

urlpatterns=[
    path('gift/',GiftListView.as_view()),
    path('gift/<pk>',GiftDetailView.as_view()),

    path('girls/',GirlsListView.as_view()),
    path('girls/<pk>',GirlsDetailView.as_view()),

    path('panjabi/',PanjabiListView.as_view()),
    path('panjabi/<pk>',PanjabiDetailView.as_view()),

    path('pant/',PantListView.as_view()),
    path('pant/<pk>',PantDetailView.as_view()),

    path('shirt/',ShirtListView.as_view()),
    path('shirt/<pk>',ShirtDetailView.as_view()),

    path('t_shirt',T_shirtListView.as_view()),
    path('t_shirt/<pk>',T_shirtDetailView.as_view())
]