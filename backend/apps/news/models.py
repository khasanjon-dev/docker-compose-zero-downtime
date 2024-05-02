from django.db.models import Model, CharField, TextField, DateTimeField, ImageField


class News(Model):
    title = CharField(max_length=500)
    body = TextField()
    image = ImageField(upload_to='news/images')
    # date
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
