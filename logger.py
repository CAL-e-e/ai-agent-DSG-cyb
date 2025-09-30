import logging

# Configure logging
def setup_logger():
    # Create logger
    logger = logging.getLogger('food_desert_analyzer')
    logger.setLevel(logging.INFO)

    # Create file handler with fixed filename
    log_filename = 'food_desert_analysis.log'
    file_handler = logging.FileHandler(log_filename, mode='a')  # 'a' for append mode
    file_handler.setLevel(logging.INFO)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Create logger instance
logger = setup_logger()

# Example logging functions
def log_data_loading(source):
    logger.info(f"Loading data from {source}")

def log_model_training(model_type, features):
    logger.info(f"Training {model_type} model with features: {features}")

def log_prediction(county, prediction, poverty_rate):
    logger.info(f"Prediction for {county}: Food Desert={prediction}, Poverty Rate={poverty_rate:.2f}%")

def log_error(error_message):
    logger.error(f"Error occurred: {error_message}")

def log_save_results(filename):
    logger.info(f"Saving results to {filename}")