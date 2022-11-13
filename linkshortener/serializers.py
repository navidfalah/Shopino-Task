from venv import create
from rest_framework import serializers

class LinkSerailizer(serializers.Serializer):
    old_link = serializers.CharField()

