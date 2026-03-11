import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    quasi_identifiers = ["age", "zip3", "gender"]

    
    merged = anon_df.merge(aux_df, on=quasi_identifiers, how="inner")

    
    match_counts = merged.groupby("anon_id")["name"].transform("count")
    unique_matches = merged[match_counts == 1][["anon_id", "name"]].copy()
    unique_matches = unique_matches.rename(columns={"name": "matched_name"})

    return unique_matches.reset_index(drop=True)


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    n_identified = len(matches_df)
    n_total = len(anon_df)
    return n_identified / n_total