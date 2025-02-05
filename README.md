# JobFinder Data Pipeline

## Overview

JobFinder is a **job recommendation system** that extracts job listings from multiple websites, processes them using **Scala**, and stores structured data in **MongoDB** for efficient querying. The pipeline ensures that only **new job listings** are processed and updates the database accordingly.

## Features

- **Automated Web Scraping**: Extracts job offers from two different websites.
- **Scala Data Processing**: Cleans, normalizes, and structures scraped data.
- **MongoDB Integration**: Stores raw and processed data in separate collections.
- **Change Streams for Real-time Processing**: Triggers Scala processing upon new data insertion.
- **Automated Execution**: Uses **Windows Task Scheduler** for scheduled execution.

## Technologies Used

- **Python** (for web scraping)
- **Scala** (for data processing)
- **MongoDB** (for database storage)
- **Bash/PowerShell** (for automation)
- **Cronjobs** (for periodic execution)



## Setup Instructions

### Prerequisites

1. Install **MongoDB** and ensure the service is running.
2. Install **Scala & sbt** for executing the Scala script.
3. Install required Python dependencies:
   ```bash
   pip install requests beautifulsoup4 pymongo
   ```
4. Ensure **Windows Task Scheduler** (or cron jobs for Linux) is set up for automation.

### Running the Pipeline Manually

1. **Run the web scrapers**:
   ```bash
   python scripts/main_site1.py
   python scripts/main_site2.py
   ```
2. **Run the Scala processing script**:
   ```bash
   sbt run
   ```
3. **Orchestrate everything with the pipeline script**:
   ```bash
   ./scripts/pipeline.sh
   ```

### Automating the Process

- **Windows Task Scheduler**:
  - Create a new task.
  - Set the trigger (e.g., every 24 hours).
  - Set the action to run `pipeline.sh`.
- **Linux (cron job example)**:
  ```bash
  0 */12 * * * /path/to/scripts/pipeline.sh
  ```

## MongoDB Collections

- **jobs\_scrape** (Raw scraped data)
- **processed\_jobs** (Processed & cleaned data)

## Future Improvements

- **Improve data matching** with advanced NLP techniques.
- **Enhance logging & monitoring**.
- **Optimize scraping & processing performance**.


