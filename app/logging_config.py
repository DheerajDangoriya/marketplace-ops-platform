import logging
import os
from datetime import datetime

def setup_logging():
        # Create a 'logs' directory if it doesn't exist
            log_dir = "logs"
            if not os.path.exists(log_dir):
                            os.makedirs(log_dir)

                                # Generate filename based on current date (e.g., marketplace_2026-02-23.log)
                            log_filename = os.path.join(log_dir, f"marketplace_{datetime.now().strftime('%Y-%m-%d')}.log")

                                        # Define the logging format
                                            # [Timestamp] [Level] [Module]: Message
                            log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

                                                    # Configure the root logger
                            logging.basicConfig(
                                                                    level=logging.INFO,
                                                                            format=log_format,
                                                                                    handlers=[
                                                                                                    logging.FileHandler(log_filename),  # Save to file
                                                                                                                logging.StreamHandler()             # Also output to terminal
                                                                                    ]
                                                        )

                            return logging.getLogger("MarketplaceApp")

                                                            # Initialize logger
                            logger = setup_logging()                        
      