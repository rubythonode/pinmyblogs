from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def emptyCheck(value):
    value = str(value).strip()

    if (len(value) <= 0):
        raise ValidationError("Length should be > 0")


###################################

def UniqueUsernameIgnoreCaseValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')
    else:
        return True


def nickNameValidator(value):
    value = str(value).strip()
    if len(value) < 6 and len(value) > 0:
        raise ValidationError("username length > 6")


####################



def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


def emailValidator(value):
    value = str(value).strip()

    print "Checking the errors in email"

    try:
        validate_email(value)
        return True
    except ValidationError   as e:
        raise ValidationError("Invalid Email!")


#######################

def passwordValidator(value):
    value = str(value).strip()

    if len(value) > 0 and len(value) < 6:
        raise ValidationError("Use at least 1 letter, 1 digit and 6 characters.")


        ################################


