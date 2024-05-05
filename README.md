## JIRA Issue Archiver

This project automates fetching issues from JIRA and storing them in an AWS S3 bucket.

### Project Structure

* **issues.py**: Handles fetching issues, storing data in S3, and tracking progress.
* **jira.py**: Responsible for making authenticated API calls to JIRA.
* **main.py**: The entry point, triggering issue loading and printing confirmation.

### Dependencies

This project requires the following Python libraries:

* `jira`
* `boto3`
* `datetime`
* `os`
* `json`
* `dotenv`

**Installation**

1. Install the dependencies using `pip`:

   ```bash
   pip install jira boto3 dotenv
   ```

2. Create a file named `.env` in your project directory. Add the following environment variables with your specific details:

   ```
   JIRA_API_URL=your_jira_api_url
   EMAIL=your_jira_email
   API_TOKEN=your_jira_api_token
   BUCKET=your_s3_bucket_name
   ```

### Usage

1. Run the script:

   ```bash
   python main.py
   ```

This will fetch a maximum of 50 issues at a time from JIRA based on the provided JQL query (defined in the `.env` file) and store them as JSON files in your S3 bucket, organized by date.

**Explanation**

* **issues.py**:
    * Uses `fetch_data` (from `jira.py`) to retrieve issues from JIRA in batches.
    * Stores issue keys and prints confirmation messages.
    * Saves each issue's JSON data to S3 using its key as the filename, organized by date for better manageability.

* **jira.py**:
    * Builds the JIRA API URL and query parameters based on environment variables.
    * Performs authenticated API calls using your Jira email and API token.
    * Returns the JSON response from JIRA.

* **main.py**:
    * Imports `load_issue` from `issues.py`.
    * Calls `load_issue` to initiate the fetching and S3 storage process.
    * Prints the total number of issues stored.

**Customization**

* You can modify the `JQL` environment variable to define the specific JIRA issues you want to fetch.
* Adjust the `maxResults` value in `issues.py` to retrieve a different number of issues per batch.
