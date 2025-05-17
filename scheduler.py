import schedule
import time
from dumper import dump_sqlite_db

schedule.every().day.at("12:00").do(dump_sqlite_db)

print("[SCHEDULER] Очікуємо на щоденне створення дампу о 12:00...")

while True:
    schedule.run_pending()
    time.sleep(60)
