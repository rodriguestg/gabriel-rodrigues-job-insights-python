from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r", encoding="utf-8") as file:
        jobs_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        dict_jobs = [jobs for jobs in jobs_csv]
    return dict_jobs
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    dict_jobs = read(path)
    group_by_job_type = {}
    for row in dict_jobs:
        job_type = row["job_type"]
        if job_type not in group_by_job_type:
            group_by_job_type[job_type] = 0
        group_by_job_type[job_type] += 1
    return group_by_job_type
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    group_by_job_type = []
    for row in jobs:
        job_type_row = row["job_type"]
        if job_type_row == job_type:
            group_by_job_type.append(row)
    return group_by_job_type
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
