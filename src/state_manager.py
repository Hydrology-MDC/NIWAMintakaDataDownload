import json
import os

from datetime import datetime, timedelta


def load_state():

    state_file = "state/state.json"

    if not os.path.exists(state_file):
        return {}

    with open(state_file, "r") as f:
        return json.load(f)


def save_state(state):

    with open("state/state.json", "w") as f:
        json.dump(state, f, indent=4)


def get_start_date(
    state,
    product
):
    """
    Returns the start date for a product.

    Priority:
    1. Last successful timestamp from state.json
    2. initial_start_date from config.yaml
    """

    product_id = str(product["product_id"])

    if product_id in state:
        return state[product_id]

    return product["initial_start_date"]