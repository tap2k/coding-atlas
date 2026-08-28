import os
import pytest


@pytest.fixture(autouse=True, scope="session")
def staging_db():
    # Shared staging database. See AGENTS.md: do not run locally.
    yield os.environ.get("STAGING_DSN", "postgres://staging.internal/slugs")
