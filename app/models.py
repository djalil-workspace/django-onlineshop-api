from django.db.models import Model, CharField, TextField, ImageField, IntegerField, DateTimeField


class Item(Model):
    title = CharField(verbose_name="Title", max_length=128)
    description = TextField(verbose_name="Description")
    image = ImageField(verbose_name="Image", upload_to="items/")
    amount = IntegerField(verbose_name="Amount", default=0)
    price = IntegerField(verbose_name="Price-$", default=0)
    added_time = DateTimeField(verbose_name="Date&Time", auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"