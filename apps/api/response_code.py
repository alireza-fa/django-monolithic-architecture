# 2000
OK = 200_00
CREATED = 201_00
# 4000
NOT_ACCEPTABLE = 406_00
BAD_REQUEST = 401_00
USER_NOT_FOUND = 404_00
INVALID_TOKEN = 406_00
TOO_MANY_REQUEST = 429_00
# 5000
INTERNAL_SERVER_ERROR = 500_00

INVALID_OTP = 406_01

ERROR_TRANSLATION = {
    # 200_00
    OK: "Ok",
    CREATED: "Created a row",
    # 400_00
    INVALID_OTP: "Invalid code",
    TOO_MANY_REQUEST: "Please try again later",
    INVALID_TOKEN: "Invalid token",
    USER_NOT_FOUND: "User with this information not found",
    # 500_00
    INTERNAL_SERVER_ERROR: "Interval server error",
}
