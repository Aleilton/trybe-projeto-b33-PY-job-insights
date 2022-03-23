# from jobs import read
from src.jobs import read


def get_unique_job_types(path):
    file_content = read(path)
    job_types = set()
    for line in file_content:
        job_types.add(line["job_type"])
    # converter set para list => https://favtutor.com/blogs/set-to-list-python
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    file_content = read(path)
    industries = set()
    for line in file_content:
        if line["industry"] != "":
            industries.add(line["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    jobs_list = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_list.append(job)
    return jobs_list


def get_max_salary(path):
    file_content = read(path)
    salaries = set()
    for line in file_content:
        if line["max_salary"] != "":
            # uso do try: https://stackoverflow.com/questions/1841565
            # /valueerror-invalid-literal-for-int-with-base-10
            try:
                salaries.add(float(line["max_salary"]))
            except ValueError:
                pass
    return sorted(salaries)[-1]
    pass


def get_min_salary(path):
    file_content = read(path)
    salaries = set()
    for line in file_content:
        if line["min_salary"] != "":
            try:
                salaries.add(float(line["min_salary"]))
            except ValueError:
                pass
    return sorted(salaries)[0]
    pass


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
