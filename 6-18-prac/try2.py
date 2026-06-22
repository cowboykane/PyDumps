

config = {"name": "timeout", "value": "30"}

try:
    config_name = config["name"]
    config_value = config["value"]
    
    parsed_value = int(config_value)
    
    print(f"Config loaded: {config_name} = {parsed_value}")

except KeyError:
    print("Error: Missing a required configuration key.")

except ValueError:
    print("Error: The configuration value must be a valid integer.")
