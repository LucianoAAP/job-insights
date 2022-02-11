from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_job_types = []
    for job in jobs_list:
        if job['job_type'] not in unique_job_types and job['job_type'] != '':
            unique_job_types.append(job['job_type'])

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs
                     if job['job_type'] == job_type]
    return filtered_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = []
    for job in jobs_list:
        if job['industry'] not in unique_industries and job['industry'] != '':
            unique_industries.append(job['industry'])

    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_jobs = [job for job in jobs
                     if job['industry'] == industry]
    return filtered_jobs


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0
    for job in jobs_list:
        if (
            job['max_salary'].isdigit()
            and int(job['max_salary']) > max_salary
           ):
            max_salary = int(job['max_salary'])

    return max_salary

    pass


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = get_max_salary(path)
    for job in jobs_list:
        if (
            job['min_salary'].isdigit()
            and int(job['min_salary']) < min_salary
           ):
            min_salary = int(job['min_salary'])

    return min_salary

    pass


def validate_salary_range(job):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('Job must contain a "min_salary" and a "max_salary"')
    if (
        not str(job['min_salary']).isdigit()
        or not str(job['max_salary']).isdigit()
       ):
        raise ValueError('Min and max salaries must contain only digits')
    if int(job['min_salary']) > int(job['max_salary']):
        raise ValueError('"min_salary" is bigger than "max_salary"')


def validate_salary_value(salary):
    if type(salary) != int and type(salary) != str:
        raise ValueError('Salary must be valid')
    if not str(salary).isdigit() and int(salary) > 0:
        raise ValueError('Salary must contain only digits')


def matches_salary_range(job, salary):
    validate_salary_range(job)
    validate_salary_value(salary)

    if (
        int(salary) >= int(job['min_salary'])
        and int(salary) <= int(job['max_salary'])
       ):
        return True

    return False

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
