import logging
import json
import os
from config.global_config import config

logging_config = config["logging_config"]


class JsonFormatter(logging.Formatter):
    def format(self, record):
        message = record.getMessage()  # Retrieve the message
        payload = getattr(record, 'payload', None)  # Get extra payload, if any
        prompt = getattr(record, 'prompt', None)  # Get extra output, if any
        output = getattr(record, 'output', None)  # Get extra output, if any

        obj = {
            'level': record.levelname,
            'time': self.formatTime(record, self.datefmt),
            'message': message,
            'payload': payload,  # Include the payload in log
            'output': output,  # Include the output in log
            'prompt': prompt,  # Include the output in log
            'name': record.name,
            'filename': record.filename,
        }
        return json.dumps(obj)

class JsonFileHandler(logging.FileHandler):
    def emit(self, record):
        log_entry = self.format(record)
        try:
            with open(self.baseFilename, 'r+') as f:
                f.seek(0)
                content = f.read()
                # Check if the file is empty
                if content:
                    logs = json.loads(content)
                else:
                    logs = []
                logs.append(json.loads(log_entry))
                f.seek(0)
                f.truncate()
                json.dump(logs, f, indent=4)  # Indent the JSON objects by 4 spaces
        except json.JSONDecodeError:
            with open(self.baseFilename, 'w') as f:
                json.dump([json.loads(log_entry)], f, indent=4)  # Indent the JSON objects by 4 spaces

# Always Initialize the logger
logger = logging.getLogger(logging_config["logger_name"])

if os.environ.get('ENVIRONMENT') != 'production':
    # Initialize the log file if it doesn't exist or is empty
    if not os.path.exists(logging_config["log_filename"]) or os.path.getsize(logging_config["log_filename"]) == 0:
        with open(logging_config["log_filename"], 'w') as f:
            json.dump([], f)

    # Set the log level
    logger.setLevel(logging.DEBUG)

    # Create a custom file handler
    file_handler = JsonFileHandler(logging_config["log_filename"])

    # Create an instance of the custom formatter
    json_formatter = JsonFormatter()

    # Set the formatter for the file handler
    file_handler.setFormatter(json_formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)
else:
    # In production, you could either set up a different logging mechanism here
    # or use a "null handler" to discard logs.
    logger.addHandler(logging.NullHandler())
