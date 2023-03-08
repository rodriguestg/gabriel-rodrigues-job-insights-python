from typing import Union, List, Dict
import csv


def read(path: str) -> List[Dict]:
    with open(path, mode="r", encoding="utf-8") as file:
        salary_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        dict_salary = [job for job in salary_csv]
    return dict_salary


def get_max_salary(path: str) -> int:
    dict_salary = read(path)
    max_salary = 0
    for row in dict_salary:
        salary_row = row["max_salary"]
        if salary_row != '' and salary_row != 'invalid':
            if int(salary_row) > max_salary:
                max_salary = int(salary_row)
    return int(max_salary)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    dict_salary = read(path)
    min_salary = get_max_salary(path)
    for row in dict_salary:
        salary_row = row["min_salary"]
        if salary_row != '' and salary_row != 'invalid':
            if int(salary_row) < min_salary:
                min_salary = int(salary_row)
    return int(min_salary)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max_s = int(job["max_salary"])
        min_s = int(job["min_salary"])
        result = bool
        if max_s < min_s:
            raise ValueError
        if int(salary) >= min_s and int(salary) <= max_s:
            result = True
        else:
            result = False
    except (ValueError, TypeError, KeyError):
        raise ValueError("O valor digitado não é válido.")
    return result
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    job_list = []
    for row in jobs:
        max_s = int(row["max_salary"])
        min_s = int(row["min_salary"])
        print(type(salary))
        if isinstance(salary, (str, int)):
            if max_s > min_s and len(str(salary)) > 0:
                job = matches_salary_range(row, salary)
                if job is True:
                    print(job)
                    job_list.append(row)
    return job_list
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
