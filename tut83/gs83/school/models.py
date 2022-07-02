from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# When you delete the User so page also delete, but its not vice versa.
# but ham kuch code likhkar aesa kar sakte h.
class Page(models.Model):
    # 👀👀👀👀👀👀👀
    # When you delete the User so page also delete, but its not vice versa.
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # 👀👀👀👀👀👀👀
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    # but ab kuch delete nahi hoga.

    # 👀👀👀👀👀👀👀👀👀👀👀👀👀
    # I want to add only specific user to create a page.

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})
    

    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
    