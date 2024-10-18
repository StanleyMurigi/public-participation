from rest_framework import viewsets
from .models import Profile, Discussion, UserView, Vote, Comment
from .serializers import ProfileSerializer, DiscussionSerializer, UserViewSerializer, VoteSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
class UserViewViewSet(viewsets.ModelViewSet):
    queryset = UserView.objects.all()
    serializer_class = UserViewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Check if the user has already submitted a view for this discussion
        user = self.request.user
        discussion = self.request.data.get('discussion')

        if UserView.objects.filter(user=user, discussion=discussion).exists():
            raise ValidationError("You have already submitted a view for this discussion.")

        serializer.save(user=user)
    
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the user has not already voted for this discussion
        user = self.request.user
        discussion = self.request.data.get('discussion')

        if Vote.objects.filter(user=user, discussion=discussion).exists():
            raise ValidationError("You have already voted for this discussion.")

        serializer.save(user=user)

        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the user is commenting on an existing UserView
        serializer.save(user=self.request.user)
