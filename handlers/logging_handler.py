import logging
import sys

# Configure logging with additional parameters
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    stream=sys.stderr,  # Log messages will also be output to standard error
    filemode='a',       # Append mode for log file
    datefmt='%Y-%m-%d %H:%M:%S',  # Custom date format
    style='{',          # Brace-style formatting for the log message
    force=True          # Force configuration of the root logger
)