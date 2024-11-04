from cloudflarest.cloudfluser import AdaptureUser
import httpx
import pprint


def get_machine_learning_status(zone_id, headers):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/bot_management"
    response = httpx.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data



def main():
    user = AdaptureUser('xx',token_name='token')
    headers = user.credentials.headers
    
    for zone in user.zones:
        ml_status = get_machine_learning_status(zone['id'],headers)
        print(zone['name'])
        pprint.pprint(ml_status)
        
    

if __name__ == "__main__":
    main()