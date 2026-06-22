# You have a list of deployment logs from a CI/CD pipeline
# Each entry is "pipeline: result: duration_seconds"
# Results are: SUCCESS, FAILED, TIMEOUT

deploy_logs = [
    "frontend: SUCCESS: 42",
    "backend: FAILED: 18",
    "frontend: SUCCESS: 38",
    "database: TIMEOUT: 120",
    "backend: SUCCESS: 55",
    "frontend: FAILED: 12",
    "database: SUCCESS: 98",
    "backend: FAILED: 22",
    "frontend: SUCCESS: 47",
    "database: FAILED: 30",
    "backend: TIMEOUT: 120",
    "frontend: SUCCESS: 51",
]

count_logs = {}
duration_times = {}

for line in deploy_logs:
    parts = line.split(":")
    
    pipeline_type = parts[0].strip()
    status = parts[1].strip()
    duration = int(parts[2].strip())
    
    count_logs[status] = count_logs.get(status, 0) + 1
    duration_times[duration] = count_logs.get(status, 0) + 1
    duration_times[pipeline_type] = duration_times.get(pipeline_type, 0) + duration
    


# 2. Track total deployment time per pipeline (sum of all durations)
# 3. Find the pipeline with the highest total deployment time
# 4. Print a report like:

# Pipeline Runtimes:
# frontend: 190s
# backend: 215s
# database: 248s
#
# Most time spent: database (248s)

print("Deployment Summary:")
for status, logs in count_logs.items():
    print(f"{status}: {logs}")

print()

print("Pipeline Runtimes:")
for pipeline, total_time in duration_times.items():
    print(f"{pipeline}: {total_time}s")

most_time_pipeline = max(duration_times, key=duration_times.get)
highest_duration = duration_times[most_time_pipeline]

print(f"Most time spent: {most_time_pipeline} ({highest_duration}s)")