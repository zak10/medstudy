from collections import namedtuple

Choice = namedtuple("Choice", "value label")


class Choices:
    """
    Usage: Base class to define choices and helper functions for a CharField on a model.
    Each 'choice' should be encapsulated in the Choice namedtuple object defined below.

    Example:

    class CopyType(Choices):
        PROXY = Choice(value='proxy', label='Proxy')
        NOTICE = Choice(value='notice', label='Notice')
        FIRST_TIME_RECIPIENT = Choice(value='first_time_recipient', label='First Time Recipient')
        LEGAL = Choice(value='legal', label='Legal')

    On the model, use the choices() method:
        type = models.CharField(choices=CopyType.choices(), max_length=50)

    To access the choice value: CopyType.PROXY.value
    """

    order = None

    @classmethod
    def choice_attributes(cls):
        return [
            attr
            for attr, obj in cls.__dict__.items()
            if attr.isupper() and isinstance(obj, Choice)
        ]

    @classmethod
    def choices(cls):
        if cls.order:
            return cls.order
        return sorted(
            [cls.__dict__[choice] for choice in cls.choice_attributes()],
            key=lambda attr: attr[0],
        )

    @classmethod
    def get_label(cls, value):
        for choice in cls.choices():
            if choice.value == value:
                return choice.label

    @classmethod
    def get_value(cls, label):
        for choice in cls.choices():
            if choice.label == label:
                return choice.value

    @classmethod
    def pairs(cls):
        return [(attr, cls.__dict__[attr].value) for attr in cls.choice_attributes()]

    @classmethod
    def values(cls):
        return [choice.value for choice in cls.choices()]

    @classmethod
    def max_length(cls):
        return max([len(v) for v in cls.values()])

    @classmethod
    def static_mapping(cls):
        return {choice.value: choice.label for choice in cls.choices()}

    @classmethod
    def labels(cls):
        return [choice.label for choice in cls.choices()]

    @classmethod
    def build_constraint_string(cls, column_name: str) -> str:
        choices_string = ", ".join(f"'{choice.value}'" for choice in cls.choices())
        return f"CHECK ({column_name} IN ({choices_string}))"
