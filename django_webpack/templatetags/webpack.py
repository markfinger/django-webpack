from django_webpack.compiler import webpack
from django_webpack import settings
from django import template
import os

register = template.Library()


@register.simple_tag
def webpack_bundle(config_path=settings.CONFIG_PATH):
    bundle = webpack(os.path.join(settings.BUNDLE_ROOT, config_path))
    return bundle.render()