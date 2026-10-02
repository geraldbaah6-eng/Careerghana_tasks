import re
from pathlib import Path

import pandas as pd


def cjlistings(inputcsv, outputcsv):
    df = pd.read_csv(inputcsv)

    requiredcolumns = {
        "Job Title",
        "Company Name",
        "Experience Level",
        "Location",
        "Salary Range",
        "Post Date",
    }

    missingcolumns = requiredcolumns - set(df.columns)
    if missingcolumns:
        raise ValueError(f"Missing columns: {', '.join(sorted(missingcolumns))}")

    textcolumns = df.select_dtypes(include=["object", "str"]).columns

    for column in textcolumns:
        df[column] = df[column].str.strip()

    for column in ["Job Title", "Company Name", "Experience Level"]:
        df[column] = df[column].str.strip().str.title()

    def formatlocation(location):
        if pd.isna(location) or not str(location).strip():
            return "Not Specified"

        location = re.sub(r"\s+", " ", str(location).strip())
        lower_location = location.lower()

        if lower_location == "remote":
            return "Remote"

        if "," in location:
            parts = [part.strip() for part in location.split(",")]
            city = parts[0].title()
            region = parts[1].strip()
            if region:
                region = region.upper() if len(region) <= 3 else region.title()
            return f"{city}, {region}" if region else city

        parts = location.split()
        if len(parts) >= 2 and len(parts[-1]) <= 3 and parts[-1].isalpha():
            city = " ".join(parts[:-1]).title()
            region = parts[-1].upper()
            return f"{city}, {region}"

        return location.title()

    df["Location"] = df["Location"].apply(formatlocation)

    companymap = {
        "it": "IT",
        "google": "Google",
        "amazon": "Amazon",
        "ipmc": "IPMC",
        "mtn": "MTN",
        "carerghana": "CareerGhana",
        "careerghana": "CareerGhana",
    }

    def normalizecompany(name):
        if pd.isna(name):
            return "Not Specified"

        value = str(name).strip()
        if not value:
            return "Not Specified"

        key = re.sub(r"\s+", " ", value).lower()
        return companymap.get(key, value)

    df["Company Name"] = df["Company Name"].apply(normalizecompany)

    def formatsalary(salary):
        if pd.isna(salary):
            return "Not Specified"

        salary = str(salary).strip()

        if not salary or salary.lower() in {"nan", "none", "na", "not specified"}:
            return "Not Specified"

        salary_lower = salary.lower()
        if salary_lower == "unpaid":
            return "Unpaid"

        cleaned = salary.replace("₵", "").replace("$", "").replace(",", "").replace(" ", "")
        cleaned = cleaned.replace("–", "-").replace("—", "-")

        match = re.fullmatch(r"(\d+)-(\d+)", cleaned)
        if match:
            low, high = match.groups()
            return f"₵{int(low):,} - ₵{int(high):,}"

        if re.fullmatch(r"\d+", cleaned):
            return f"₵{int(cleaned):,}"

        return salary

    df["Salary Range"] = df["Salary Range"].apply(formatsalary)

    df["Experience Level"] = (
        df["Experience Level"]
        .fillna("Not Specified")
        .replace({"Nan": "Not Specified", "None": "Not Specified"})
        .str.strip()
        .str.title()
    )

    df["Post Date"] = pd.to_datetime(
        df["Post Date"],
        errors="coerce",
    ).dt.strftime("%Y-%m-%d")

    df = df.drop_duplicates()
    df.to_csv(outputcsv, index=False)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "mjlistings.csv"
    output_path = base_dir / "Cleaned list.csv"
    cjlistings(str(input_path), str(output_path))
