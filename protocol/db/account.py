from ...models import User

def getUser(user_id):
	try:
		return User.objects.get(userID = user_id)
	except User.DoesNotExist:
		return None

def makeUser(user_id, user_type, str_nickName):
	# FIXME: Check duplicated user.
	user = User(userID = user_id, userType = user_type, nickName = str_nickName)
	user.save()
