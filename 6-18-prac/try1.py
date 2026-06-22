# A single server config dictionary
config = {"name": "timeout", "value": "30"}

# Try each of these one at a time by changing the config dict above:
# Case 1: config = {"name": "timeout", "value": "30"}  -> should succeed
# Case 2: config = {"name": "retries", "value": "five"} -> bad value
# Case 3: config = {"name": "port"}                     -> missing key
# Case 4: config = {"value": "50"}                      -> missing name key

# Write a try/except that:
# 1. Reads config["name"] and config["value"]
# 2. Converts value to int
# 3. Handles KeyError and ValueError separately
# 4. On success prints: "Config loaded: timeout = 30"

try:
    config_name = config["name"]
    config_value = config["value"]
    conv_value = int(config_value)
    print(f"Config loaded: {config_name} = {conv_value}")

except KeyError:
    print("Error: Missing configuration key.")
except ValueError:
    print("Error: Must be a valid integer.")