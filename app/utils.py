import pandas as pd
from django.utils.timezone import now
from app.models import Airport, Aircraft, Flight
from os.path import exists
from django.conf import settings
from datetime import timedelta

SOURCE_FILE = "airports.csv"
SOURCE_URL = "https://ourairports.com/data/" + SOURCE_FILE
SOURCE_PATH = settings.MEDIA_ROOT / SOURCE_FILE


def filter_data(df):
    """
    Filter data of :model:`app.Airport`s from CSV datasource using pandas.
    Only `large_airports` with `ident` (icao_code), `municipality` (city) and `name` are selected.
    """
    df = df[["ident", "type", "name", "municipality"]]
    df = df.dropna()
    df = df[(df.type == "large_airport")]
    df = df[(df.ident.str.len() == 4)]
    df = df[["ident", "municipality", "name"]]
    return df


def get_airports(columns, reload):
    """
    Retrieve data of :model:`app.Airport`s from CSV datasource using pandas.
    File is saved in :media: folder for cache.
    """
    if reload or not exists(SOURCE_PATH):
        df = pd.read_csv(SOURCE_URL)
        df.to_csv(SOURCE_PATH)
    else:
        df = pd.read_csv(SOURCE_PATH)

    df = filter_data(df)
    df.columns = columns
    return df.to_dict('records')


def populate_airports(limit=None, reload=False):
    """
    Populate :model:`app.Airport`s from the datasource into the database.
    """
    Airport.objects.all().delete()
    cols = [field.name for field in Airport._meta.fields]
    airports_data = get_airports(cols, reload)[:limit]
    aiports_instances = [Airport(**airport) for airport in airports_data]
    try:
        return Airport.objects.bulk_create(aiports_instances)
    except Exception as err:
        raise err


def populate_aircrafts():
    """
    Populate dummy :model:`app.Aircraft`s from the datasource into the database.
    """
    Aircraft.objects.all().delete()
    aircraft_defaults = [
        dict(serial_number="AA5435", manufacturer="Airbus"),
        dict(serial_number="BA2311", manufacturer="Boeing"),
        dict(serial_number="EM8799", manufacturer="Embraer"),
    ]
    return (aircraft_defaults, [Aircraft.objects.create(
        **aircraft) for aircraft in aircraft_defaults])


def populate_flights(airports, aircrafts):
    """
    Populate dummy :model:`app.Flight`s from the datasource into the database.
    """
    Flight.objects.all().delete()
    flight_defaults = [
        dict(departure=airports[0],
             arrival=airports[1],
             departure_time=now() + timedelta(hours=3),
             arrival_time=now() + timedelta(hours=9),   # inflight_time = 6h
             aircraft=aircrafts[0]
             ),
        dict(departure=airports[0],
             arrival=airports[6],
             departure_time=now() + timedelta(hours=9),
             arrival_time=now() + timedelta(hours=24),  # inflight_time = 13h
             aircraft=aircrafts[1]
             ),
        dict(departure=airports[0],
             arrival=airports[7],
             departure_time=now() + timedelta(hours=1),
             arrival_time=now() + timedelta(hours=7),  # inflight_time = 6h
             aircraft=aircrafts[2]
             ),
        dict(departure=airports[2],
             arrival=airports[3],
             departure_time=now(),
             arrival_time=now() + timedelta(hours=6),  # inflight_time = 6h
             aircraft=aircrafts[0]
             ),
        dict(departure=airports[4],
             arrival=airports[5],
             departure_time=now() + timedelta(hours=1),
             arrival_time=now() + timedelta(hours=8),  # inflight_time = 7h
             aircraft=aircrafts[2]
             ),
        dict(departure=airports[4],
             arrival=airports[6],
             departure_time=now()+ timedelta(hours=2),
             arrival_time=now() + timedelta(hours=4),  # inflight_time = 2h
             aircraft=aircrafts[2]
             ),
        dict(departure=airports[8],
             arrival=airports[3],
             departure_time=now() + timedelta(days=1),
             arrival_time=now() + timedelta(days=1, hours=5),  # inflight_time = 5h
             aircraft=aircrafts[0]
             ),
        dict(departure=airports[8],
             arrival=airports[3],
             departure_time=now() + timedelta(days=3),
             arrival_time=now() + timedelta(days=3, hours=10),  # inflight_time = 10h
             aircraft=aircrafts[1]
             ),
        dict(departure=airports[9],
             arrival=airports[10],
             departure_time=now() + timedelta(days=2),
             arrival_time=now() + timedelta(days=2, hours=8),  # inflight_time = 8h
             aircraft=aircrafts[2]
             ),
        dict(departure=airports[9],
             arrival=airports[6],
             departure_time=now() + timedelta(days=5),
             arrival_time=now() + timedelta(days=5, hours=12),  # inflight_time = 12h
             aircraft=aircrafts[0]
             ),
    ]

    return (flight_defaults, [Flight.objects.create(
        **flight) for flight in flight_defaults])
