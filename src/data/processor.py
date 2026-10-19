
import pandas as pd


def clean_flight_data(flights: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw BTS flight data for the initial flight-duration model.

    Returns a new DataFrame without modifying the original.
    """
    cleaned = flights.copy()

    # Normalize column names.
    cleaned.columns = cleaned.columns.str.strip().str.upper()

    # Convert flight dates to pandas datetime.
    cleaned["FL_DATE"] = pd.to_datetime(
        cleaned["FL_DATE"], errors="coerce"
    )

    # Convert numeric columns, allowing invalid values to become missing.
    numeric_columns = [
        "CRS_DEP_TIME",
        "DEP_TIME",
        "DEP_DELAY",
        "CRS_ARR_TIME",
        "ARR_TIME",
        "ARR_DELAY",
        "CANCELLED",
        "DIVERTED",
        "CRS_ELAPSED_TIME",
        "ACTUAL_ELAPSED_TIME",
    ]

    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(
            cleaned[column], errors="coerce"
        )

    # Remove records without a valid date.
    cleaned = cleaned.dropna(subset=["FL_DATE"])

    # Exclude cancelled and diverted flights.
    cleaned = cleaned[
        (cleaned["CANCELLED"] == 0)
        & (cleaned["DIVERTED"] == 0)
    ]

    # Require a valid, positive actual flight duration.
    cleaned = cleaned[
        cleaned["ACTUAL_ELAPSED_TIME"].notna()
        & (cleaned["ACTUAL_ELAPSED_TIME"] > 0)
    ]

    # Remove exact duplicate records.
    cleaned = cleaned.drop_duplicates()

    return cleaned.reset_index(drop=True)


def save_clean_flight_data(
    flights: pd.DataFrame,
    output_path: str,
) -> None:
    """Save cleaned flight records to a CSV file."""
    flights.to_csv(output_path, index=False)
