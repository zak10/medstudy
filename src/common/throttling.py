from ninja_extra.throttling import AnonRateThrottle


class AIOnePerMinueThrottle(AnonRateThrottle):
    rate = "1/min"
    scope = "minutes"


class AIFivePerHourThrottle(AnonRateThrottle):
    rate = "5/hour"
    scope = "hours"
