import os
import shutil
from datetime import datetime


def dump_sqlite_db():
    source_db = "identifier.sqlite"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    dump_file = os.path.join("dumps", f"dump_{timestamp}.sqlite")

    if os.path.exists(source_db):
        shutil.copy(source_db, dump_file)
        print(f"[DUMP] Створено дамп: {dump_file}")
    else:
        print("[ERROR] Файл бази даних не знайдено.")
