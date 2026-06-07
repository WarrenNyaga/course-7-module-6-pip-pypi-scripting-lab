import argparse
from datetime import datetime
import os
import requests


def fetch_data():
    """Fetches data from the public API specified in the lab assignment."""
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1", timeout=5
        )
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        pass
    return None


# FIXED: Changed function name from generate_log_function to generate_log
def generate_log(log_data):
    """Creates a timestamped log file and populates it with data."""
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list of strings.")

    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"log_{timestamp}.txt"

    with open(filename, "w") as file:
        if log_data:
            for item in log_data:
                file.write(f"{item}\n")
        else:
            file.write("")

    print(f"Success: Log written to {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automating Python Projects CLI Tool"
    )
    parser.add_argument(
        "--run", action="store_true", help="Execute the automated log process"
    )
    args = parser.parse_args()

    api_result = fetch_data()

    if api_result:
        data_to_log = [
            "User logged in.",
            "User updated profile.",
            f"Fetched Title: {api_result.get('title')}",
        ]
    else:
        data_to_log = ["User logged in.", "API data unavailable."]

    # FIXED: Updated the function call here as well
    generate_log(data_to_log)