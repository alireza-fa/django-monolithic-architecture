from django.utils.translation import gettext_lazy as _

OK = 2000
NOT_ACCEPTABLE = 4060
BAD_REQUEST = 4010
TOO_MANY_REQUEST = 4290

INVALID_OTP = 4061

ERROR_TRANSLATION = {
    INVALID_OTP: _("Invalid code"),
    TOO_MANY_REQUEST: _("Please try again later"),
}
