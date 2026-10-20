import os
import json

from datetime import datetime

from src.state_manager import (
    load_state,
    save_state,
    get_start_date
)

from src.json_response_processor import (
    json_to_dataframe
)

from src.niwa_mintaka_client import (
    MintakaClient
)

def run(
    config,
    logger
):

    os.makedirs(
        config["folders"]["raw"],
        exist_ok=True
    )

    os.makedirs(
        config["folders"]["csv"],
        exist_ok=True
    )

    state = load_state()

    client = MintakaClient(
        config["api"]["base_url"],
        config["api"]["username"],
        config["api"]["password"]
    )

    for product in config["products"]:

        if not product["enabled"]:
            continue

        product_id = product["product_id"]

        try:
            start_date = get_start_date(
                state,
                product
            )

            end_date = datetime.utcnow().strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
            logger.info(
                "ProductID=%s | StartDate=%s | EndDate=%s",
                product_id,
                start_date,
                end_date
            )

            logger.info(
                f"Fetching Product {product_id}"
            )

            payload = client.fetch_product_data(
                product_id,
                start_date,
                end_date
            )

            raw_file = os.path.join(
                config["folders"]["raw"],
                f"{product_id}.json"
            )

            with open(
                raw_file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    payload,
                    f,
                    indent=2
                )

            df = json_to_dataframe(
                payload
            )

            if len(df) == 0:

                logger.warning(
                    f"No data returned for {product_id}"
                )

                continue

            latest_time = (
                df["DateTimeUTC"]
                .max()
            )

            site_name = (
                df["SiteName"]
                .iloc[0]
                .replace(" ", "_")
            )

            measurement = (
                df["Measurement"]
                .iloc[0]
                .replace(" ", "_")
            )

            run_date = datetime.now().strftime(
                "%Y%m%d"
            )

            csv_file = os.path.join(
                config["folders"]["csv"],
                f"{site_name}_"
                f"{measurement}_"
                f"{product_id}_"
                f"{run_date}.csv"
            )

            df.to_csv(
                csv_file,
                index=False
            )

            logger.info(
                f"Exported {len(df)} rows"
            )


            logger.info(
                f"Saved {csv_file}"
            )

            state[
                str(product_id)
            ] = latest_time

            save_state(
                state
            )

        except Exception as ex:

            logger.exception(
                f"Product Failed: {product_id}"
            )