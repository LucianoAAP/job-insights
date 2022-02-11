import pytest
from src.sorting import sort_by

jobs_mock = [
    {
        'title': 'Front end developer',
        'min_salary': 2000,
        'max_salary': 5000,
        'date_posted': '2020-02-02',
    },
    {
        'title': 'Back end developer',
        'min_salary': 3000,
        'max_salary': 4000,
        'date_posted': '2020-07-02',
    },
    {
        'title': 'Full stack developer',
        'min_salary': 3500,
        'max_salary': 6000,
        'date_posted': '2020-03-02',
    },
]

jobs_sorted_by_date_posted = [
    {
        'title': 'Back end developer',
        'min_salary': 3000,
        'max_salary': 4000,
        'date_posted': '2020-07-02',
    },
    {
        'title': 'Full stack developer',
        'min_salary': 3500,
        'max_salary': 6000,
        'date_posted': '2020-03-02',
    },
    {
        'title': 'Front end developer',
        'min_salary': 2000,
        'max_salary': 5000,
        'date_posted': '2020-02-02',
    },
]

jobs_sorted_by_max_salary = [
    {
        'title': 'Full stack developer',
        'min_salary': 3500,
        'max_salary': 6000,
        'date_posted': '2020-03-02',
    },
    {
        'title': 'Front end developer',
        'min_salary': 2000,
        'max_salary': 5000,
        'date_posted': '2020-02-02',
    },
    {
        'title': 'Back end developer',
        'min_salary': 3000,
        'max_salary': 4000,
        'date_posted': '2020-07-02',
    },
]

jobs_sorted_by_min_salary = [
    {
        'title': 'Front end developer',
        'min_salary': 2000,
        'max_salary': 5000,
        'date_posted': '2020-02-02',
    },
    {
        'title': 'Back end developer',
        'min_salary': 3000,
        'max_salary': 4000,
        'date_posted': '2020-07-02',
    },
    {
        'title': 'Full stack developer',
        'min_salary': 3500,
        'max_salary': 6000,
        'date_posted': '2020-03-02',
    },
]


def test_sort_by_criteria():
    sort_by(jobs_mock, 'date_posted')
    assert jobs_mock == jobs_sorted_by_date_posted

    sort_by(jobs_mock, 'max_salary')
    assert jobs_mock == jobs_sorted_by_max_salary

    sort_by(jobs_mock, 'min_salary')
    assert jobs_mock == jobs_sorted_by_min_salary

    with pytest.raises(ValueError, match='invalid sorting criteria: xablau'):
        sort_by(jobs_mock, 'xablau')

    pass
