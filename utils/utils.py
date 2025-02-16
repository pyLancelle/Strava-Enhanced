from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # Remplace pytz pour gérer les fuseaux horaires

def days_to_timestamp(chosen_date: str, nb_days: int) -> int:
    """
    The purpose of this function is to transform a number of days into a timestamp, that we will use in the ETL process.

    :param chosen_date: the date from whom we decide to calculate the number of days.
    :param nb_days: the number of days needed.
    :return: a timestamp that corresponds to the right calculation.
    """
    if nb_days < 0:
        raise ValueError("nb_days must be greater than or equal to zero.")

    try:
        date_reference = datetime.strptime(chosen_date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError("The date provided doesn't match the expected pattern (YYYY-MM-DD).") from e

    date_calcul = date_reference - timedelta(days=nb_days)
    date_minuit = datetime(
        date_calcul.year,
        date_calcul.month,
        date_calcul.day,
        tzinfo=ZoneInfo("Europe/Paris")
    )

    return int(date_minuit.timestamp())