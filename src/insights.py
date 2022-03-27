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
    print(jobs)
    print(industry)
    filtered_industries = list()
    for row in jobs:
        if row["industry"] == industry:
            filtered_industries.append(row)
    return filtered_industries


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


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
    elif type(salary) != int:
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError
    else:
        return job["min_salary"] <= salary <= job["max_salary"]

# lançar exceção no python (raise) - equivalente ao throw do js.
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python


def filter_by_salary_range(jobs, salary):
    job_list = list()
    try:
        for job in jobs:
            if job["min_salary"] <= salary <= job["max_salary"]:
                job_list.append(job)
    except (TypeError):
        print(TypeError)
    return job_list

# TypeError: "<=" not supported between instances of "int" and "NoneType"
