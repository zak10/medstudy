from typing import Any
from django.conf import settings
import pytest
import boto3
from unittest import mock
from moto import mock_aws

from software_requests.ai.agents.vendor_scorer import VendorWithScoreSchema


@pytest.fixture(autouse=True, scope="session")
def mock_aws_resources():
    with mock_aws():
        conn = boto3.resource("s3", region_name="us-east-1")
        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        conn.create_bucket(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        yield


class MockOrchestrator:
    def determine_category(self, *args, **kwargs) -> str:
        return "Data Enrichment"

    def determine_requirements(self, *args, **kwargs) -> dict[str, Any]:
        return {"Compliance": "GDPR", "Price": "Affordable"}

    def best_matching_vendors(self, *args, **kwargs) -> list[VendorWithScoreSchema]:
        return [
            {
                "vendor_name": "Test Vendor 1",
                "reason": "This is a good vendor",
                "score": 93,
            },
            {
                "vendor_name": "Test Vendor 2",
                "reason": "This is also a good vendor",
                "score": 82,
            },
        ]


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(autouse=True)
def patch_orchestrator():
    with mock.patch("software_requests.ai.orchestrator.Orchestrator", MockOrchestrator):
        yield


@pytest.fixture(autouse=True)
def patch_slack_Client():
    with mock.patch("common.slack.slack_client") as mock_slack_client:
        mock_slack_client.chat_postMessage.return_value.status_code = 200
        yield mock_slack_client
