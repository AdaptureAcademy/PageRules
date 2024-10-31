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
