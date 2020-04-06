from django.db import models

# Create your models here.


class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10,unique=True)
    passwd = models.CharField(max_length=20)
    admin = models.IntegerField(default=0)
    create_at = models.DateField()


class blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(users, on_delete=models.CASCADE)
    summary = models.TextField(max_length=50,blank=True)
    content = models.TextField()
    created_at = models.DateField()


class comments(models.Model):
    com_id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(blogs, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(users, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)

