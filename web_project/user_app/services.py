from .models import User
from django.core.exceptions import ObjectDoesNotExist

class UserService:
    def loginCheck(self, user_id, user_pw):
        try:
            user = User.objects.get(email = user_id)
            if user_pw == user.password:
                return True
            else:
                return False
        except ObjectDoesNotExist:
            return False
        except:
            return False