import pytest
from app import fetch_weather_data
import streamlit as st

@pytest.fixture(autouse=True, scope="module")
def mock_streamlit():
    """
    Mock various streamlit methods that are called during testing.
    This avoids errors due to Streamlit's interactive nature, which doesn't play nice with testing.
    """
    

    st.write = lambda *args: None
    st.header = lambda *args: None
    # Add other Streamlit methods that you want to mock...
    yield

def test_fetch_weather_data():
    # Replace 'Paris' and 'YOUR_API_KEY' with appropriate values or mock the request
    result = fetch_weather_data("Paris", st.secrets["general"]["API_KEY"])
    assert result is not None  # or other assertions based on your needs