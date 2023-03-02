import configparser
import decimal
from pathlib import Path

from sqlalchemy import create_engine, text


def map_data(row):
    def convert_value(value):
        if isinstance(value, decimal.Decimal):
            value = float(value)
        return value

    return tuple(map(convert_value, row))


def execute_sql(sql: str = None):
    if sql is None:
        sql = 'select * from rp_clienti'
    ini = Path(__file__).parent.parent / 'server.ini'
    config = configparser.ConfigParser()
    config.read(ini)
    connection_string = config['database']['fatturazione']
    engine = create_engine(connection_string)
    with engine.connect() as connection:
        result = connection.execute(text(sql))
        fields = tuple(result.keys()._keys)
        tab = (fields,) + tuple(map_data(row._data) for row in result)
        for row in tab:
            print(row)
    return tab


if __name__ == '__main__':
    execute_sql()
