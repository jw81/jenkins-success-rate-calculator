import os
import requests
from datetime import datetime

# Fetch Jenkins URL, cookie, start date, and end date from environment variables
jenkins_url = os.getenv("JENKINS_URL")
cookie = os.getenv("COOKIE")
start_date_str = os.getenv("START_DATE")
end_date_str = os.getenv("END_DATE")

# Validate required environment variables
if not all([jenkins_url, cookie, start_date_str, end_date_str]):
    raise ValueError("JENKINS_URL, COOKIE, START_DATE, and END_DATE environment variables are required.")

# Parse start and end dates
try:
    start_date = datetime.strptime(start_date_str, "%m-%d-%Y")
    end_date = datetime.strptime(end_date_str, "%m-%d-%Y")
except ValueError:
    raise ValueError("START_DATE and END_DATE must be in the format mm-dd-yyyy")

# Jenkins builds list API endpoint
builds_url = f"{jenkins_url}/api/json?tree=builds[number,url]"

# Set up headers to include the cookie
headers = {
    "Cookie": cookie
}

# Fetch build data with error handling
try:
    response = requests.get(builds_url, headers=headers)
    response.raise_for_status()  # Raise an error for non-200 responses
    builds_data = response.json().get("builds", [])
except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
    exit(1)
except ValueError:
    print("Failed to parse JSON response. Response content:")
    print(response.text)
    exit(1)

# Initialize counters for builds
total_builds = 0
successful_builds = 0

# Loop through each build to get detailed info
for build in builds_data:
    build_number = build["number"]
    build_url = f"{jenkins_url}/{build_number}/api/json"

    try:
        build_response = requests.get(build_url, headers=headers)
        build_response.raise_for_status()
        build_info = build_response.json()
        
        # Check timestamp and result fields
        build_time = datetime.fromtimestamp(build_info["timestamp"] / 1000)
        build_result = build_info.get("result")

        # Only count builds within the specified date range
        if start_date <= build_time <= end_date:
            total_builds += 1
            if build_result == "SUCCESS":
                successful_builds += 1

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data for build {build_number}: {e}")
    except KeyError:
        print(f"Missing expected data in build {build_number}")

# Calculate success rate
if total_builds > 0:
    success_rate = (successful_builds / total_builds) * 100
else:
    success_rate = 0

print(f"Success Rate from {start_date_str} to {end_date_str}: {success_rate:.2f}%")
