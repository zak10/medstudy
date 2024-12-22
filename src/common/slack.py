import dataclasses
import json
from enum import StrEnum

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from common.domains import BaseDomain
from common.json_extra import UUIDEncoder
from nwo import settings
from collections.abc import MutableMapping


def flatten(dictionary, parent_key='', separator='_'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)


class NotificationType(StrEnum):
    NEW_USER_LOGIN = "new_user_magic_link"
    EXISTING_USER_LOGIN = "existing_user_magic_link"
    PROPOSAL_SUBMITTED = "proposal_submitted"
    REQUEST_SUBMITTED = "request_submitted"
    REQUEST_CREATED = "request_created"
    SHARING_TOKEN_REDEEMED = "sharing_token_redeemed"


class SlackChannel(StrEnum):
    MVP = "C07TXV4S0AH"
    WEBHOOKS = "C085EEJRS1E"

    @classmethod
    def get_for_notification_type(
        cls, notification_type: NotificationType
    ) -> "SlackChannel":
        # if we ever want to do intelligent routing
        return SlackChannel.WEBHOOKS


@dataclasses.dataclass(slots=True)
class Notification(BaseDomain):
    email_address: str
    notification_type: NotificationType
    additional_context: dict


slack_client = WebClient(token=settings.SLACK_BOT_TOKEN)


class NotificationClient:
    def __init__(self, slack: WebClient | None = None):
        self._slack = slack or slack_client

    def send_notification(self, notification: Notification) -> bool:
        channel = SlackChannel.get_for_notification_type(notification.notification_type)

        try:
            payload = notification.to_dict()
            payload["env"] = settings.ENV
            flattened = flatten(payload)
            response = slack_client.chat_postMessage(
                channel=channel,
                text="\n".join(f"{key}: {val}" for key, val in flattened.items()),
            )
        except SlackApiError:
            return False

        return response.status_code == 200
