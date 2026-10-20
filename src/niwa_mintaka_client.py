import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class MintakaClient:

    def __init__(
        self,
        base_url,
        username,
        password
    ):

        self.base_url = base_url
        self.session = requests.Session()

        retry = Retry(
            total=5,
            backoff_factor=2,
            status_forcelist=[
                500,
                502,
                503,
                504
            ]
        )

        self.session.mount(
            "https://",
            HTTPAdapter(max_retries=retry)
        )

        self.auth = (
            username,
            password
        )

    def fetch_product_data(
        self,
        product_id,
        start_date,
        end_date
    ):

        url = (
            f"{self.base_url}"
            f"/products/{product_id}/data"
        )

        params = {
            "startDate": start_date,
            "endDate": end_date
        }

        response = self.session.get(
            url,
            auth=self.auth,
            params=params,
            timeout=300
        )

        response.raise_for_status()

        return response.json()