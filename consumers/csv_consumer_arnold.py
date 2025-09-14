"""
csv_consumer_arnold.py

Consume JSON messages from a Kafka topic and process them.
"""

#####################################
# Import Modules
#####################################

import os
import json
from collections import defaultdict

from dotenv import load_dotenv

from utils.utils_consumer import create_kafka_consumer
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

load_dotenv()

#####################################
# Getter Functions for .env Variables
#####################################


def get_kafka_topic() -> str:
    topic = os.getenv("SALES_TOPIC", "unknown_topic")
    logger.info(f"Kafka topic: {topic}")
    return topic


def get_kafka_consumer_group_id() -> str:
    group_id: str = os.getenv("SALES_CONSUMER_GROUP_ID", "default_group")
    logger.info(f"Kafka consumer group id: {group_id}")
    return group_id


#####################################
# Function to process a single message
#####################################

current_revenue: defaultdict[str, float] = defaultdict(float)
latte_alert_triggered = False  # Ensure alert fires only once


def process_message(message: str) -> None:
    global latte_alert_triggered
    try:
        logger.debug(f"Raw message: {message}")

        data: dict = json.loads(message)
        money = data.get("money")
        coffee_name = data.get("coffee_name")  # fixed typo

        logger.info(f"Processed JSON message: {data}")

        if money is None or coffee_name is None:
            logger.error(f"Invalid message format: {message}")
            return

        current_revenue[coffee_name] += float(money)
        logger.info(f"Updated revenue: {dict(current_revenue)}")

        # ALERT if latte revenue exceeds 200 (fires only once)
        if coffee_name.lower() == "latte" and current_revenue[coffee_name] > 200 and not latte_alert_triggered:
            logger.alert(f"⚠️ Latte revenue exceeded 200! Current: {current_revenue[coffee_name]}")
            latte_alert_triggered = True

    except json.JSONDecodeError as e:
        logger.error(f"JSON decoding error for message '{message}': {e}")
    except Exception as e:
        logger.error(f"Error processing message '{message}': {e}")


#####################################
# Define main function for this module
#####################################


def main() -> None:
    logger.info("START consumer.")

    topic = get_kafka_topic()
    group_id = get_kafka_consumer_group_id()

    consumer = create_kafka_consumer(topic, group_id)

    logger.info(f"Polling messages from topic '{topic}'...")
    try:
        for message in consumer:
            message_str = message.value
            logger.debug(f"Received message at offset {message.offset}: {message_str}")

            process_message(message_str)

    except KeyboardInterrupt:
        logger.warning("Consumer interrupted by user.")
    except Exception as e:
        logger.error(f"Error while consuming messages: {e}")
    finally:
        consumer.close()
        logger.info(f"Kafka consumer for topic '{topic}' closed.")


#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
