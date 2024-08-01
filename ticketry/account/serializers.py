from djoser.serializers import UserSerializer as BaseUserSerializer

class Userserializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email']
