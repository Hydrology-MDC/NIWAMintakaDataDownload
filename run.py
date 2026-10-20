from src.config_loader import load_config
from src.logger_setup import get_logger
from src.orchestration_layer import run


def main():

    config = load_config()

    logger = get_logger(
        config["logging"]["file"]
    )

    logger.info(
        "========== START =========="
    )

    run(
        config,
        logger
    )

    logger.info(
        "========== END =========="
    )


if __name__ == "__main__":

    main()