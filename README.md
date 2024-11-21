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
docker run -e JENKINS_URL=$JENKINS_URL \
           -e COOKIE=$COOKIE \
           -e START_DATE=$START_DATE \
           -e END_DATE=$END_DATE \
           jenkins-success-rate
```

## Output

The script will output the success rate for the specified date range:

```bash
Total Builds: 10
Successful Builds: 8
Success Rate from 11-08-2024 to 11-20-2024: 80.00%
```

## Troubleshooting

- **Authentication Issues:** If you encounter a `403 Forbidden` error, ensure that your `COOKIE` value is correct. You can obtain this by checking your browser's developer tools for the Cookie header when logged into Jenkins.
- **Invalid Date Format:** Ensure that `START_DATE` and `END_DATE` are in `mm-dd-yyyy` format. Any other format will result in a parsing error.