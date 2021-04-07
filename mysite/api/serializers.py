from rest_framework import routers, serializers, viewsets
from .models import *

class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class TractorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddTractor
        fields = '__all__'

class RiceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rice_type
        fields = '__all__'

class TractorStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tractor_status
        fields = '__all__'

class MoneyStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Money_status
        fields = '__all__'

class WorkStatusSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Work_status
        fields = '__all__'



class WorkSerializer(serializers.ModelSerializer):
    farmer_name = FarmerSerializer(many=False, read_only=True)
    rice_type = RiceTypeSerializer(many=False, read_only=True)
    tractor = TractorSerializer(many=False, read_only=True)
    tractor_status = TractorStatusSerializer(many=False, read_only=True)
    money_status = MoneyStatusSerializer(many=False, read_only=True)
    work_status = WorkStatusSerializer(many=False, read_only=True)  

    class Meta:
        model = Work
        fields = '__all__'



## Serializers define the API representation.
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url', 'username', 'email', 'is_staff']
#
## ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#
## Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

