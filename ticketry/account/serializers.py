from djoser.serializers import UserSerializer as Save

class Userserializer(Save):
    class Meta(Save.Meta):
        fields = ['id', 'firstname', 'lastname', 'email']