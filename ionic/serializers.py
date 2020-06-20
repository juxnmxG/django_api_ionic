from rest_framework import serializers
from . models import Ionic

class IonicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ionic
        #fields = ('id', 'nombre', 'apellido', 'documento', 'email', 'fecha', 'pub_date')
        fields = '__all__'
