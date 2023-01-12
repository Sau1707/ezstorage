class PrimaryKey:
    class int: pass
    class str: pass

DEAFAULT_VALUES = {int: 0, float: 0.0, str: "", bool: False, list: [], dict: {}, tuple: (), PrimaryKey.int: 0, PrimaryKey.str: ""}
DEAFAULT_SCHEMA = {int: "INTEGER", float: "REAL", str: "TEXT", bool: "INTEGER", list: "TEXT", dict: "TEXT", tuple: "TEXT", PrimaryKey.int: "INTEGER PRIMARY KEY", PrimaryKey.str: "TEXT PRIMARY KEY"}
