from cloudflarest.cloudfluser import AdaptureUser
import httpx
import pandas as pd
import pprint
from datetime import datetime, timezone

# This function is being used to get the Machine Learning Status 
def get_machine_learning_status(zone_id, headers):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/bot_management"
    response = httpx.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data


def main():
    user = AdaptureUser('xx', token_name='token')
    client_name = user.client_name
    headers = user.credentials.headers
    results = []

    for idx,zone in enumerate(user.zones, start=1):
        ml_status = get_machine_learning_status(zone['id'], headers)
        print(f"zone: {zone['name']} zones left: {idx} of {len(user.zones)}")
        # print(zone['name'])
        # pprint.pprint(ml_status)

        # Map the fields from the response
        if ml_status and ml_status['success']:
            result = ml_status['result']
            results.append({
                'Account Name':zone['account']['name'],
                'Zone Name': zone['name'],
                'AI Bots Protection': zone['ai_bots_protection'],#result.get('ai_bots_protection', 'N/A'),
                'Auto Update Model': zone['auto_update_model'],#result.get('auto_update_model', 'N/A'),
                'Enable JS': zone['enable_js'],#result.get('enable_js', 'N/A'),
                'Suppress Session Score': zone['suppress_session_score'],#result.get('suppress_session_score', 'N/A'),
                'Using Latest Model': zone['using_latest_model']#result.get('using_latest_model', 'N/A'),
            })

    # Create a DataFrame
    df = pd.DataFrame(results)

    # Export to Excel and format output file
    today = datetime.now()
    formatted_date = today.strftime('%b%d')
    df.to_excel(f'{client_name}machine_learning_status{formatted_date}.xlsx', index=False)


if __name__ == "__main__":
    main()
