from django.urls import path

from api.views import GiftListView, NittoListView, GiftDetailView, NittoDetailView, PanjabiListView, PanjabiDetailView, \
    PantListView, PantDetailView, ShirtListView, ShirtDetailView, T_shirtListView, T_shirtDetailView

urlpatterns=[
    path('gift/',GiftListView.as_view()),
    path('gift/<pk>',GiftDetailView.as_view()),

    path('nitto/',NittoListView.as_view()),
    path('nitto/<pk>',NittoDetailView.as_view()),

    path('panjabi/',PanjabiListView.as_view()),
    path('panjabi/<pk>',PanjabiDetailView.as_view()),

    path('pant/',PantListView.as_view()),
    path('pant/<pk>',PantDetailView.as_view()),

    path('shirt/',ShirtListView.as_view()),
    path('shirt/<pk>',ShirtDetailView.as_view()),

    path('t_shirt',T_shirtListView.as_view()),
    path('t_shirt/<pk>',T_shirtDetailView.as_view())
]