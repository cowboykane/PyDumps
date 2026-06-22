import os, shutil

log_count = {}

logs = os.listdir("logs")

for log in logs:
    file_path = os.path.join("logs", log)
    line_count = 0

    with open(file_path, "r") as file:
        for line in file:
            line_count += 1

    log_count[log] = line_count

print("\n--- LOG REPORT ---")

for log_name, count in log_count.items():
    print(f"{log_name}: {count} lines")

shutil.copytree("logs", "logs_backup")

print("\nBackup created: logs_backup")