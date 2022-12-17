import sqlite3


def get_all(query: str):
    """
    Подключение к БД
    """
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        result = []
        # Цикл по всем строкам БД
        for i in conn.execute(query).fetchall():
            s = dict(i)
            result.append(s)
    return result


def get_one(query: str):
    """
    Подключение к БД, одна строка
    """
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        res = conn.execute(query).fetchone()

        if res is None:
            return None
        else:
            return dict(res)
