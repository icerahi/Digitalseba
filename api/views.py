from rest_framework.generics import ListAPIView,RetrieveAPIView

from api.serializer import GiftSerializer, T_shirtSerializer, ShirtSerializer, PantSerializer, PanjabiSerializer, \
    GirlsSerializer
from gift.models import Gift
from girls.models import Girls
from panjabi.models import Panjabi
from pant.models import Pant
from shirt.models import Shirt
from t_shirt.models import T_shirt


class GiftListView(ListAPIView):
    queryset=Gift.objects.all()
    serializer_class=GiftSerializer
class GiftDetailView(RetrieveAPIView):
    queryset=Gift.objects.all()
    serializer_class=GiftSerializer



class GirlsListView(ListAPIView):
    queryset = Girls.objects.all()
    serializer_class = GirlsSerializer
class GirlsDetailView(RetrieveAPIView):
    queryset = Girls.objects.all()
    serializer_class = GirlsSerializer


class PanjabiListView(ListAPIView):
    queryset = Panjabi.objects.all()
    serializer_class = PanjabiSerializer
class PanjabiDetailView(RetrieveAPIView):
    queryset = Panjabi.objects.all()
    serializer_class = PanjabiSerializer

class PantListView(ListAPIView):
    queryset = Pant.objects.all()
    serializer_class = PantSerializer
class PantDetailView(RetrieveAPIView):
    queryset = Pant.objects.all()
    serializer_class = PantSerializer

class ShirtListView(ListAPIView):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer
class ShirtDetailView(RetrieveAPIView):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer


class T_shirtListView(ListAPIView):
    queryset = T_shirt.objects.all()
    serializer_class = T_shirtSerializer
class T_shirtDetailView(RetrieveAPIView):
    queryset = T_shirt.objects.all()
    serializer_class = T_shirtSerializer
