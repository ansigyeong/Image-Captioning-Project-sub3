from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Vocabulary, Speaking

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'

class SpeakingSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Speaking
        fields = ('cap_text', 'image')