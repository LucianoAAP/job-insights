from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []
    with open(path) as file:
        jobs = csv.DictReader(file)
        for job in jobs:
            jobs_list.append(job)

    return jobs_list
