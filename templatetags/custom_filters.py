from django import template

register = template.Library()

@register.filter(name='truncate_long_text')
def truncate_long_text(value, max_length=30):
    if len(value) > max_length:
        return f"{value[:max_length]}..."
    return value
