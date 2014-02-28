from django.contrib.auth.models import User
from users.models import *

def generate_password():
	from os import urandom
	from base64 import urlsafe_b64encode
	# Generate a password with length 12
	return urlsafe_b64encode(urandom(8))[:-1]

GROUP_PRIORITY = [3, 1, 6, 5, 8, 9, 2, 14, 11, 4, 7, 15, 13, 12, 10]	# Sort by team lead -> staff -> consultant
def get_user_sorting_key(user):
	groups = [g.id for g in user.groups.all()]
	identity = ''.join([str(1 - groups.count(i)) for i in GROUP_PRIORITY])	# Sort by identity first
	title = user.profile.title.ljust(5)
	name = user.profile.name()
	return ''.join((identity, title, name))

def sorted_users(group_id=None):
	users = User.objects.filter(is_active=True)
	if group_id:
		users = users.filter(groups__id=group_id) 
	return sorted(users, key=get_user_sorting_key)
