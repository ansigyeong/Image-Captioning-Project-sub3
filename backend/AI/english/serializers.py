from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Vocabulary, Speaking, Userwordbook

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'

class SpeakingSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Speaking
        fields = ('cap_text', 'image')

class UserwordbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userwordbook
        fields = '__all__'