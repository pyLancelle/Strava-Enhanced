"""
This file contains the ETL workflow.

"""
import yaml
from dotenv import dotenv_values

from tasks.etl.api_loader import API_Loader

def etl_flow():
    FILEPATHS = {
        'DOT_ENV': '../.env',
        'CONFIG_YAML': '../configuration/configuration.yaml'
    }

    secrets = dotenv_values(FILEPATHS.get('DOT_ENV'))

    with open(FILEPATHS.get('CONFIG_YAML'), 'r') as f:
        config = yaml.safe_load(f)

    strava = API_Loader(
        access_token=secrets.get('STRAVA_ACCESS_TOKEN'),
        client_secret=secrets.get('STRAVA_SECRET'),
        client_id=secrets.get('STRAVA_CLIENT_ID'),
        refresh_token=secrets.get('STRAVA_REFRESH_TOKEN')
    )
    strava.run()



if __name__ == '__main__':
    etl_flow()
