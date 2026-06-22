
health_checks = [
    "web-01: OK",
    "db-01: CRITICAL",
    "web-02: WARNING",
    "db-02: OK",
    "cache-01: WARNING",
    "web-01: CRITICAL",
    "db-01: CRITICAL",
    "web-02: OK",
    "cache-01: CRITICAL",
    "web-01: OK",
    "db-02: WARNING",
    "web-02: CRITICAL",
]

check_counter = {}
server_list = {}

for line in health_checks:
    parts = line.split(":")
    server = parts[0].strip()
    status = parts[1].strip()
    
    check_counter[status] = check_counter.get(status, 0) + 1
    server_list[server] = status # Last recorded status 


print("Status Summary:")
for status, count in check_counter.items():
    print(f"{status}: {count}")

print()

print("Current Server States:")
for server, final_status in server_list.items():
    print(f"{server}: {final_status}")
    
