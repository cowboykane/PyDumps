import json

raw_api_response = """
{
    "metadata": {
        "datacenter": "us-east-1",
        "generated_at": "2026-06-23"
    },
    "infrastructure": [
        {"server_id": "vm-01", "role": "web-ui", "environment": "production", "status": "online"},
        {"server_id": "vm-02", "role": "api-gateway", "environment": "staging", "status": "offline"},
        {"server_id": "vm-03", "role": "auth-service", "environment": "production", "status": "online"},
        {"server_id": "vm-04", "role": "db-primary", "environment": "production", "status": "offline"},
        {"server_id": "vm-05", "role": "cache-redis", "environment": "dev", "status": "offline"}
    ]
}
"""

offline_servers = []

data = json.loads(raw_api_response)
print(data)

for server in data["infrastructure"]:
    if server["status"] == "offline":
        offline_servers.append(server)

with open("6-23-prac/incident_report.json", "w") as file:
    json.dump(offline_servers, file, indent=4)
    print("Json Loaded successfully!")