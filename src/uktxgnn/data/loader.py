#!/usr/bin/env python3
"""UK MHRA drug data loader.

This module loads drug data from the UK Medicines and Healthcare products
Regulatory Agency (MHRA) PARD database.

Data must be obtained from:
- https://products.mhra.gov.uk/ (search interface)
- MHRA FOI request for bulk data
"""

from pathlib import Path
from typing import Optional

import pandas as pd


def load_mhra_data(filepath: Path) -> pd.DataFrame:
    """Load MHRA export file (CSV or Excel).

    Args:
        filepath: Path to MHRA data file

    Returns:
        DataFrame with MHRA data
    """
    if filepath.suffix.lower() == '.xlsx':
        df = pd.read_excel(filepath)
    else:
        df = pd.read_csv(filepath, encoding='utf-8')

    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names for consistency.

    MHRA exports may have varying column names. This function
    normalizes common variations.
    """
    column_map = {
        'Product Licence Number': 'PL_Number',
        'Product License Number': 'PL_Number',
        'PL Number': 'PL_Number',
        'Product Name': 'Product_Name',
        'Product name': 'Product_Name',
        'Active Substance': 'Active_Substances',
        'Active Substances': 'Active_Substances',
        'Active substance': 'Active_Substances',
        'Therapeutic Indications': 'Indications',
        'Therapeutic indications': 'Indications',
        'Pharmaceutical Form': 'Dosage_Form',
        'Marketing Authorisation Status': 'Status',
        'MA Status': 'Status',
    }

    df = df.rename(columns=column_map)
    return df


def load_bnf_data(filepath: Path) -> pd.DataFrame:
    """Load UK BNF data from Open Formulary format.

    Args:
        filepath: Path to drug_names.csv file

    Returns:
        DataFrame with standardized columns
    """
    import re

    print(f"Loading BNF data from: {filepath}")
    df = pd.read_csv(filepath, header=None, names=['bnf_code', 'drug_name'])

    # Extract drug names - parse format like "Omeprazole_Cap E/C 10mg"
    # The part before underscore is usually the active ingredient
    def extract_ingredient(name):
        if pd.isna(name):
            return ""
        # Split by underscore and take first part
        parts = str(name).split('_')
        ingredient = parts[0].strip()
        # Remove brand/manufacturer info in parentheses
        ingredient = re.sub(r'\([^)]*\)', '', ingredient).strip()
        return ingredient

    df['Active_Substances'] = df['drug_name'].apply(extract_ingredient)

    # Standardize to expected format
    result = pd.DataFrame({
        'PL_Number': df['bnf_code'],
        'Product_Name': df['drug_name'],
        'Active_Substances': df['Active_Substances'],
        'ingredients': df['Active_Substances'],
        'brand_name': df['drug_name'],
    })

    # Remove duplicates by Active_Substances and filter non-empty
    result = result[result['Active_Substances'].notna() & (result['Active_Substances'] != '')]
    result = result.drop_duplicates(subset=['Active_Substances']).reset_index(drop=True)

    print(f"  Total BNF items: {len(result)}")
    print(f"  Unique ingredients: {result['Active_Substances'].nunique()}")

    return result


def filter_active_medicines(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to only include active marketing authorisations.

    Excludes revoked, withdrawn, or suspended products.
    """
    if 'Status' in df.columns:
        excluded = ['Revoked', 'Withdrawn', 'Suspended', 'Not renewed']
        df = df[~df['Status'].str.contains('|'.join(excluded), case=False, na=False)]

    return df


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load and process MHRA drug data.

    This is the main entry point, compatible with the standard TxGNN interface.

    Args:
        filepath: Optional path to MHRA data file. If not provided,
                  looks for data in standard locations.

    Returns:
        DataFrame with columns:
            - PL_Number: Product Licence number
            - Product_Name: Drug product name
            - Active_Substances: Active substances (semicolon separated)
    """
    base_dir = Path(__file__).parent.parent.parent.parent
    data_dir = base_dir / "data"
    raw_dir = data_dir / "raw"

    # Try to find MHRA or BNF data file
    if filepath is None:
        possible_files = [
            raw_dir / "drug_names.csv",  # Open Formulary BNF data
            raw_dir / "mhra_products.csv",
            raw_dir / "mhra_export.csv",
            raw_dir / "mhra_products.xlsx",
            raw_dir / "uk_medicines.csv",
            data_dir / "mhra_products.csv",
        ]

        for f in possible_files:
            if f.exists():
                filepath = f
                break

    if filepath is None or not filepath.exists():
        print("Warning: No MHRA/BNF data found.")
        print("Please download BNF data or MHRA data")
        print("Expected file: data/raw/drug_names.csv")
        return pd.DataFrame(columns=['PL_Number', 'Product_Name', 'Active_Substances'])

    # Check if this is BNF format (drug_names.csv)
    if "drug_names.csv" in str(filepath):
        return load_bnf_data(filepath)

    print(f"Loading MHRA data from: {filepath}")

    # Load and process
    df = load_mhra_data(filepath)
    df = normalize_columns(df)
    df = filter_active_medicines(df)

    # Ensure required columns exist
    required_cols = ['PL_Number', 'Product_Name', 'Active_Substances']
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    print(f"  Total medicines: {len(df)}")
    print(f"  With ingredients: {df['Active_Substances'].notna().sum()}")

    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """Filter active drugs with valid ingredients.

    Args:
        df: Drug DataFrame

    Returns:
        Filtered DataFrame
    """
    col = 'Active_Substances' if 'Active_Substances' in df.columns else 'ingredients'
    active = df[df[col].notna() & (df[col] != '')].copy()
    active = active.reset_index(drop=True)
    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """Get drug data summary statistics.

    Args:
        df: Drug DataFrame

    Returns:
        Summary statistics dictionary
    """
    all_ingredients = set()
    ing_col = 'Active_Substances' if 'Active_Substances' in df.columns else 'ingredients'
    name_col = 'Product_Name' if 'Product_Name' in df.columns else 'brand_name'

    for ing_str in df[ing_col].dropna():
        # MHRA uses comma or semicolon separation
        for sep in [';', ',']:
            if sep in str(ing_str):
                ingredients = [i.strip() for i in str(ing_str).split(sep)]
                all_ingredients.update(ingredients)
                break
        else:
            all_ingredients.add(str(ing_str).strip())

    return {
        "total_count": len(df),
        "with_ingredient": df[ing_col].notna().sum(),
        "unique_products": df[name_col].nunique() if name_col in df.columns else 0,
        "unique_ingredients": len(all_ingredients),
    }


def get_unique_ingredients(df: pd.DataFrame) -> list[str]:
    """Extract unique ingredients from loaded data."""
    all_ingredients = []

    col = 'Active_Substances' if 'Active_Substances' in df.columns else 'ingredients'
    for ing_str in df[col].dropna():
        for sep in [';', ',']:
            if sep in str(ing_str):
                ingredients = [i.strip() for i in str(ing_str).split(sep)]
                all_ingredients.extend(ingredients)
                break
        else:
            all_ingredients.append(str(ing_str).strip())

    return sorted(set(all_ingredients))


if __name__ == "__main__":
    # Test loading
    df = load_fda_drugs()
    print(f"\nLoaded {len(df)} drugs")

    if len(df) > 0:
        ingredients = get_unique_ingredients(df)
        print(f"Unique ingredients: {len(ingredients)}")
        print(f"\nSample ingredients: {ingredients[:10]}")
