from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def valid_email_domains(value):
    valid_domains = ['@gmail.com', '@yahoo.com']
    for i in valid_domains:
        if str(value).endswith(i):
            break
    else:
        raise ValidationError('Invalid email address')


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        domains = list(domains)
        self.domains = domains

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f' {args[0].split("a")} is not valid.')


