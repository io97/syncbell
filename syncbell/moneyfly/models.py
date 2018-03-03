from django.db import models


""" カテゴリ """
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


""" 金額 """
class Money(models.Model):
    money = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
    )
    note = models.TextField()
    use_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_id
