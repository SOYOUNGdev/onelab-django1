from django.db import models


class CommunityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(community_post_status=True)
