from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path, mode="r", encoding="utf-8") as file:
        industries_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        dict_industries = [industries for industries in industries_csv]
    group_by_industries = []
    for row in dict_industries:
        industries_row = row["industry"]
        if industries_row not in group_by_industries and industries_row != '':
            group_by_industries.append(industries_row)
    return group_by_industries
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    group_by_industry = []
    for row in jobs:
        industry_row = row["industry"]
        if industry_row == industry:
            group_by_industry.append(row)
    return group_by_industry
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
