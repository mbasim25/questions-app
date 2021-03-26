from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from users.models import CustomUser
from questions.models import Question, Answer


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username"]
