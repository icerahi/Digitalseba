from rest_framework import serializers

from gift.models import Gift
from girls.models import Girls
from panjabi.models import Panjabi
from pant.models import Pant
from shirt.models import Shirt
from t_shirt.models import T_shirt


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gift
        fields=('title','product_code','price','picture','description','date','band','active')



class GirlsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Girls
        fields=('title','product_code','price','picture','description','date','band','active')

class PanjabiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Panjabi
        fields = ('title', 'product_code', 'price', 'picture', 'description', 'date', 'band', 'active')

class PantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pant
        fields = ('title', 'product_code', 'price', 'picture', 'description', 'date', 'band', 'active')

class ShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shirt
        fields = ('title', 'product_code', 'price', 'picture', 'description', 'date', 'band', 'active')

class T_shirtSerializer(serializers.ModelSerializer):
    class Meta:
        model=T_shirt
        fields = ('title', 'product_code', 'price', 'picture', 'description', 'date', 'band', 'active')
