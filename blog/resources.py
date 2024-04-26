from import_export import resources
from blog.models import Comment


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
        # fields = ('blog', 'broadcast')
