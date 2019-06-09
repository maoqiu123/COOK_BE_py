from django.db import models
# Create your models here.


class Group(models.Model):
    group_id = models.IntegerField(verbose_name="GroupId", default=123456789)
    chat_id = models.CharField(verbose_name="ChatId", max_length=255, null=True, blank=True)
    group_name = models.CharField(verbose_name=u"聊天室名称", max_length=255, null=True, blank=True, default="聊天室")

    class Meta:
        verbose_name = u"群聊信息"
        verbose_name_plural = verbose_name
        db_table = "group"

    def __str__(self):
        return self.group_name
