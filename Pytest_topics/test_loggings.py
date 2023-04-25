import logging
LOGGER = logging.getLogger(__name__)

def test_myloggings():
    LOGGER.info("Info Logs")
    LOGGER.warning("Warning Logs")
    LOGGER.error("Error Logs")
    LOGGER.critical("Critical Logs")
    assert True