import random
import string


def genetate_new(length=6, chars=string.letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


def send_hash(instance, length=6):
    new_code=genetate_new(length=length)
    K=instance
    # print (new_code)

    hash_exists_user=K.objects.filter(user_hash=new_code).exists()

    if (hash_exists_user):
        return send_hash(instance, length=length)
    return new_code
