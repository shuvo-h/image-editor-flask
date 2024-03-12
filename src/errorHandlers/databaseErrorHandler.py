import re

# Function to format error message
def format_error_message(error):
    # Extract error message from the exception
    error_message = str(error)

    # Parse database error message for readability
    parsed_message = parse_db_error_message(error_message)
    if parsed_message:
        return parsed_message
    
    # Check for duplicate entry error
    duplicate_entry_message = parse_duplicate_entry_error(error_message)
    if duplicate_entry_message:
        return duplicate_entry_message
    
    # If unable to parse, return the original error message
    return error_message

# Function to parse duplicate entry error message
def parse_duplicate_entry_error(error_message):
    # Define regular expression pattern to detect duplicate entry error
    duplicate_entry_pattern = r"Duplicate entry '(.*?)' for key '(.*?)'"
    
    # Search for duplicate entry error message
    duplicate_entry_match = re.search(duplicate_entry_pattern, error_message)
    
    if duplicate_entry_match:
        duplicate_value = duplicate_entry_match.group(1)
        duplicate_key = duplicate_entry_match.group(2)
        keyName = duplicate_key.split('.')[1] if len(duplicate_key.split('.')) > 1 else duplicate_key
        return f"{keyName} already exists"
    else:
        return None



# Function to parse database error message for readability
def parse_db_error_message(error_message):
    # Define regular expression pattern to extract the error message
    error_msg_pattern = r"\d+, \"Column '(.*?)' (cannot be null)\""

    # Search for the error message in the error message
    error_msg_match = re.search(error_msg_pattern, error_message)

    if error_msg_match:
        error_msg = error_msg_match.group(1)
        return error_msg + " " + error_msg_match.group(2)
    else:
        return None
    
