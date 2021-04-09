from rest_framework.throttling import UserRateThrottle

class DhoniRateThrottel(UserRateThrottle):
    scope = 'dhoni'