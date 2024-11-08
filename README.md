# Jenkins Build Success Rate Calculator

This Dockerized Python script calculates the success rate of builds for a specified Jenkins job within a given date range. By using this setup, you can retrieve success rates without needing to install Python on your local machine.

## Prerequisites

- **Docker**: Make sure Docker is installed and running on your machine.
- **Jenkins Access**: You need access to the Jenkins job URL and a valid authentication cookie.

## Environment Variables

The script requires the following environment variables:

- `JENKINS_URL`: The URL of the Jenkins job.
- `COOKIE`: The authentication cookie required to access Jenkins. This can be obtained by inspecting the request headers in your browser's developer tools.
- `START_DATE`: The start date for the date range, in `mm-dd-yyyy` format.
- `END_DATE`: The end date for the date range, in `mm-dd-yyyy` format.

## Building the Docker Image

Clone this repository or save the `Dockerfile` and `get_success_rate.py` script in the same directory, then run:

```bash
docker build -t jenkins-success-rate .
```

## Running the Docker Container

Use the following command to run the Docker container, passing in the required environment variables:
```bash
docker run -e JENKINS_URL="https://your-jenkins-url.com/job-name" \
           -e COOKIE="your-cookie-value" \
           -e START_DATE="mm-dd-yyyy" \
           -e END_DATE="mm-dd-yyyy" \
           jenkins-success-rate
```

## Output

The script will output the success rate for the specified date range:

```bash
Success Rate from 10-01-2023 to 10-15-2023: 85.71%
```

## Troubleshooting

- **Authentication Issues:** If you encounter a `403 Forbidden` error, ensure that your `COOKIE` value is correct. You can obtain this by checking your browser's developer tools for the Cookie header when logged into Jenkins.
- **Invalid Date Format:** Ensure that `START_DATE` and `END_DATE` are in `mm-dd-yyyy` format. Any other format will result in a parsing error.