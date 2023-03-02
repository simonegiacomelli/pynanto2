import os
from typing import List

from server.database import execute_sql


async def server_list_dir(path: str) -> List[str]:
    return os.listdir(path)


async def server_execute_sql(sql: str):
    return execute_sql(sql)
