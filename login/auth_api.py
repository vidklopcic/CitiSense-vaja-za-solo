import time
from models import ApiAuth

def auth_api(token):
    instance = ApiAuth.objects.get(token=token)
    if instance is not None:
        if time.time() - instance.time < 2*24*60*60:
            instance.delete()
            return False
        return True
    else:
        return False