from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .tasks import send_post_notification

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save()
        # Send async task
        send_post_notification.delay(post.title)
