from django.template.loader_tags import register


def key(d, key_name):
    value = d[key_name]
    return value

key = register.filter('key', key)