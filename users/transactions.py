from django.db import transaction
from users.models import Profile


@transaction.atomic
def user_register(form) -> Profile:
    user = form.save()
    profile = Profile.objects.create(
        first_name=user.first_name,
        last_name=user.last_name,
        user=user
    )
    return profile
