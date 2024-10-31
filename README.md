# Cloudflare Page Rules Exporter

This Python script retrieves page rules from multiple Cloudflare zones and exports the data to an Excel file using the Cloudflare API.

## Dependencies

- `cloudflarest`: A library for interacting with the Cloudflare API.
- `httpx`: A library for making HTTP requests.
- `pandas`: A data manipulation and analysis library, used here to create and export a DataFrame.

## Code Explanation

### Imports

```python
from cloudflarest.cloudfluser import AdaptureUser
import httpx
import pandas as pd

## Code Explanation: Zone Retrieval Loop

This section of the code is responsible for retrieving page rules for specified Cloudflare zones. It checks for the existence of the zones by their names and prepares to gather data for further processing.

### Code Breakdown

```python
# List of zone names to retrieve page rules for
zone_names = ['zone_name_1', 'zone_name_2']
all_rows = []  # To store data for all zones
