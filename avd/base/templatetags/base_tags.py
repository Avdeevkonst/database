from django import template
from base.models import *

register = template.Library()


@register.inclusion_tag('base/paid_user.html')
def show_paid_users(sort=None, paid_selected=0):
    if not sort:
        paid_user = User.objects.all()
    else:
        paid_user = User.objects.order_by(sort)

    return {"paid_user": paid_user, "paid_selected": paid_selected}
