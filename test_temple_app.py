
import pytest
from temple_data import temples
import os

def test_temple_data_integrity():
    """Verify that the temple data is loaded correctly and has required fields."""
    assert len(temples) > 0
    for name, data in temples.items():
        assert "location" in data
        assert "description" in data
        assert "history" in data
        assert "architecture" in data
        assert "image_url" in data

def test_temple_data_content():
    """Verify specific content in temple data."""
    assert "Brihadeeswarar Temple" in temples
    assert "Thanjavur" in temples["Brihadeeswarar Temple"]["location"]

def test_environment_setup():
    """Test that environment variables can be set (mocking API key setup)."""
    os.environ["GOOGLE_API_KEY"] = "test_key"
    assert os.environ.get("GOOGLE_API_KEY") == "test_key"
