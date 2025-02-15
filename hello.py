from dotenv import dotenv_values
import yaml

from tasks.etl.api_loader import API_Loader

def main():
    # Import config
    with open('configuration/configuration.yaml', 'r') as f:
        config = yaml.safe_load(f)

    secrets = dotenv_values('.env')

    # Fetch from Strava
    strava = API_Loader(
        access_token=secrets.get('STRAVA_ACCESS_TOKEN'),
        client_secret=secrets.get('STRAVA_SECRET'),
        client_id=secrets.get('STRAVA_CLIENT_ID'),
        refresh_token=secrets.get('STRAVA_REFRESH_TOKEN')
    )



    # Insert into Bronze
    athlete = strava.get_athlete_data()
    #
    print(athlete)



if __name__ == "__main__":
    main()