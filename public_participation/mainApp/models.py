from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Discussion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    documents = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.title


class UserView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='views')
    view = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'discussion')

    def __str__(self):
        return f"{self.user.username}'s view on {self.discussion.title}"


class Vote(models.Model):
    VOTE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey('Discussion', on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=3, choices=VOTE_CHOICES)  # Yes or No vote
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'discussion')

    def __str__(self):
        return f"{self.user.username} voted {self.get_vote_type_display()} on {self.discussion.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_view = models.ForeignKey(UserView, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s comment on {self.user_view.user.username}'s view"
