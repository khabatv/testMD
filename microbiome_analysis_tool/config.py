
import os
import logging

# --- Basic Configuration ---

# Set the number of CPU cores to use for parallel processing.
# Leaves one core free for system processes.
CPU_CORES = max(1, os.cpu_count() - 1)

# --- AI Configuration ---

# IMPORTANT: Replace "YOUR_API_KEY_HERE" with your actual Google Gemini API Key.
# You can obtain a key from https://aistudio.google.com/
GEMINI_API_KEY = "AIzaSyDiuCPQ8vYm9XLxB4yTSh4H1fBXxVcRUhY" # Placeholder Key

# --- Logging Setup ---

# Configure a logger to provide informative output to the console.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("MicrobiomeTool")

def setup_file_logger(output_dir):
    """Adds a file handler to the root logger to capture all logs."""
    # Ensure the handler is not added multiple times in a notebook environment
    root_logger = logging.getLogger()
    if any(isinstance(h, logging.FileHandler) for h in root_logger.handlers):
        # Find and remove existing file handlers
        for handler in root_logger.handlers[:]:
            if isinstance(handler, logging.FileHandler):
                handler.close()
                root_logger.removeHandler(handler)

    log_file = os.path.join(output_dir, 'analysis_log.txt')
    file_handler = logging.FileHandler(log_file, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
    logger.info(f"File logger initiated. All output will be saved to {log_file}")
