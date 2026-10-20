import pandas as pd


def json_to_dataframe(payload):

    site_name = payload["location"]["name"]
    measurement = payload["range"]["physicalPropertyName"]
    tuples = payload["data"][0]["tuples"]

    rows = []

    for item in tuples:

        rows.append({

            "SiteName": site_name,
            "Measurement": measurement,
            "DateTimeUTC": item["validityTime"],
            "Value": item["value"]

        })

    df = pd.DataFrame(rows)

    return df