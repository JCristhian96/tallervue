from django.utils.text import slugify


def set_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.description)
    return instance