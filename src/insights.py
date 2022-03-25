from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    unique_job_types = set()
    for row in data:
        unique_job_types.add(row["job_type"])
    return list(unique_job_types)

# Foi utilizado a seguinte fonte para compreender
# o fluxo de iteração do python
# https://www.youtube.com/watch?v=AnJPtKLtc7o&ab_channel=HashtagPrograma%C3%A7%C3%A3o


def filter_by_job_type(jobs, job_type):
    print(jobs)
    print(job_type)
    filtered_jobs = list()
    for row in jobs:
        if row["job_type"] == job_type:
            filtered_jobs.append(row)
    return filtered_jobs


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()
    for row in data:
        print(row["industry"])
        if row["industry"] != "":
            unique_industries.add(row["industry"])
    return list(unique_industries)


def filter_by_industry(jobs, industry):
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
    return []


def get_max_salary(path):
    data = read(path)
    max_salary = set()
    for row in data:
        print(row["max_salary"])
        if row["max_salary"] != "" and row["min_salary"] != "invalid":
            max_salary.add(int(row["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    data = read(path)
    min_salary = list()
    for row in data:
        print(row["min_salary"])
        if row["min_salary"] != "" and row["min_salary"] != "invalid":
            min_salary.append(int(row["min_salary"]))
    return min(min_salary)

    # pass


def matches_salary_range(job, salary):
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
    pass


def filter_by_salary_range(jobs, salary):
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
    return []
