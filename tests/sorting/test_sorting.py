import pytest
from src.sorting import sort_by

jobs_mock = [
    {
        'title': 'Front end developer',
        'min_salary': '2000',
        'max_salary': '5000',
        'date_posted': '2020-02-02',
    },
    {
        'title': 'Back end developer',
        'min_salary': '3000',
        'max_salary': '4000',
        'date_posted': '2020-07-02',
    },
    {
        'title': 'Full stack developer',
        'min_salary': '3500',
        'max_salary': '6000',
        'date_posted': '2020-03-02',
    },
]


def test_sort_by_criteria():
    with pytest.raises(ValueError, match='invalid sorting criteria: xablau'):
        sort_by(jobs_mock, 'xablau')

    assert sort_by(jobs_mock, 'date_posted') == [
        jobs_mock[1],
        jobs_mock[2],
        jobs_mock[0]
    ]

    assert sort_by(jobs_mock, 'max_salary') == [
        jobs_mock[2],
        jobs_mock[0],
        jobs_mock[1]
    ]

    assert sort_by(jobs_mock, 'min_salary') == [
        jobs_mock[0],
        jobs_mock[1],
        jobs_mock[2]
    ]

    pass
