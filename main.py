from datetime import datetime
from pathlib import Path

Path("reports").mkdir(exist_ok=True)

today = datetime.now().strftime("%d-%m-%Y")

with open("reports/jobs_report.md", "w", encoding="utf-8") as f:
    f.write("# Bangladesh HR Job Report\n\n")
    f.write(f"Date: {today}\n\n")
    f.write("System Working Successfully ✅\n")

print("Done")
