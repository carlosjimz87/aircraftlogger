from django.db.models.fields import related
import pandas as pd
from pandas.io.parsers import read_csv
from app.models import Airport
from os.path import exists
from django.conf import settings

SOURCE_FILE = "airports.csv"
SOURCE_URL = "https://ourairports.com/data/" + SOURCE_FILE
SOURCE_PATH = settings.MEDIA_ROOT / SOURCE_FILE


def filter_data(df):
    df = df[["ident", "type", "name", "municipality"]]
    df = df.dropna()
    df = df[(df.type == "large_airport")]
    df = df[(df.ident.str.len() == 4)]
    df = df[["ident", "name", "municipality"]]
    return df


def get_airports(columns, reload):
    if reload or not exists(SOURCE_PATH):
        df = pd.read_csv(SOURCE_URL)
        df.to_csv(SOURCE_PATH)
    else:
        df = pd.read_csv(SOURCE_PATH)

    df = filter_data(df)
    df.columns = columns
    return df.to_dict('records')


def populate_airports(limit=None, reload=False):
    Airport.objects.all().delete()
    cols = [field.name for field in Airport._meta.fields]
    airports_data = get_airports(cols, reload)[:limit]
    aiports_instances = [Airport(**airport) for airport in airports_data]
    try:
        return Airport.objects.bulk_create(aiports_instances)
    except Exception as err:
        raise err
