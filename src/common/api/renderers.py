from zoneinfo import ZoneInfo

from ninja.renderers import JSONRenderer, NinjaJSONEncoder


class CustomJsonEncoder(NinjaJSONEncoder):
    def default(self, v):
        if isinstance(v, ZoneInfo):
            return str(v)
        return super().default(v)


class CustomJsonRenderer(JSONRenderer):
    encoder_class = CustomJsonEncoder
