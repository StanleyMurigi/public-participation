from rest_framework import serializers
from .models import Profile, Discussion, UserView, Vote, Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'is_admin']

class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'documents']

class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserView
        fields = ['id', 'user', 'discussion', 'view', 'created_at']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'discussion', 'vote_type', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_view', 'comment', 'created_at']

