import pytest
import os
from datetime import datetime
from lib.generate_log import generate_log

def test_generate_log_creates_file():
    # Test valid list input creates the file correctly
    test_data = ["Action 1", "Action 2"]
    generate_log(test_data)
    
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"log_{current_date}.txt"
    
    assert os.path.exists(filename)
    
    # Clean up the test file after verifying
    if os.path.exists(filename):
        os.remove(filename)

def test_generate_log_value_error():
    # Test that a ValueError is thrown if input is not a list
    with pytest.raises(ValueError):
        generate_log("Not a list string")
