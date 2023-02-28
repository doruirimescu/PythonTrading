#!/usr/bin/python3
from Trading.config.config import DB_USERNAME, DB_PASSWORD, DB_NAME, DATA_STORAGE_PATH
from Trading.utils.write_to_file import read_json_file
from Trading.database.add_hedge_into_database import add_hedge
import pymysql


def update_open_trades(symbol: str, instrument_type: str, gross_profit: float,
                    swap: float, cmd: int, open_price: float,
                    timestamp_open: str, position_id: int, order_id: int):
    # Open database connection
    db = pymysql.connect(host='localhost', database=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD)
    db.autocommit(True)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # First delete
    query = f"DELETE FROM trading.open_trades;"
    cursor.execute(query)

    query = (
        f"INSERT INTO trading.open_trades(symbol, instrument_type, gross_profit, swap, cmd, open_price, timestamp_open, position_id, order_id) VALUES"
        f" ('{symbol}', '{instrument_type}', {gross_profit}, {swap}, {cmd}, {open_price}, '{timestamp_open}', {position_id}, {order_id});"
        )
    print(query)
    cursor.execute(query)
    db.close()
