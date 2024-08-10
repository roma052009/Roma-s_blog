import django_setup

from blog.models import Post

new_post = Post(
    title = "Just title",
    content = "Im hapy bc i can finaly read this"
).save()

# post = Post.objects.first()
# post.delete()