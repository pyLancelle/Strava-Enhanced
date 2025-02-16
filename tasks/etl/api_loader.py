import requests

class API_Loader:
    def __init__(self, access_token, client_secret, client_id, refresh_token):
        self.access_token = access_token
        self.client_secret = client_secret
        self.client_id = client_id
        self.refresh_token = refresh_token

    def run(self):
        self.refresh_access_token()

        pass

    def _get_headers(self):
        """

        :return:
        """
        return {'Authorization': f'Bearer {self.access_token}'}

    def refresh_access_token(self):
        """
        Rafraîchit le token d'accès à chaque appel.
        """
        url = "https://www.strava.com/api/v3/oauth/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data.get("access_token")
            print("Jeton rafraîchi avec succès.")
            return True
        else:
            print("Erreur lors du rafraîchissement du token :", response.status_code, response.text)
            return False

    def get_athlete_data(self):
        """
        Récupère les informations de l'athlète connecté.
        Rafraîchit le token à chaque appel.
        """
        if not self.refresh_access_token():
            print("Impossible de rafraîchir le token.")
            return None

        url = "https://www.strava.com/api/v3/athlete"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            print("Erreur lors de la requête :", response.status_code, response.text)
            return None

    def get_recent_activities(self, after=1735691212):
        """
        Récupère la liste des activités récentes de l'athlète connecté.

        Args:
            page (int): Le numéro de page à récupérer (utile pour la pagination).
            per_page (int): Le nombre d'activités par page.

        Returns:
            list: Une liste de dicts contenant les informations de chaque activité.
        """
        # Rafraîchit le token à chaque appel
        if not self.refresh_access_token():
            print("Impossible de rafraîchir le token.")
            return None

        url = "https://www.strava.com/api/v3/athlete/activities"
        params = {
            'after': after
        }
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Erreur lors de la récupération des activités :", response.status_code, response.text)
            return None



