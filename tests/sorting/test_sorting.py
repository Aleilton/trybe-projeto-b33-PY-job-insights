import pytest
from src.sorting import sort_by


jobs = [
    {"max_salary": 100, "min_salary": 50, "date_posted": "2020-05-08"},
    {"max_salary": 1000, "min_salary": 100, "date_posted": "2020-04-25"},
    {"max_salary": 50000, "min_salary": 200, "date_posted": "2020-05-02"},
    {"max_salary": 15000, "min_salary": 300, "date_posted": "2020-05-09"},
    {"max_salary": 1500, "min_salary": 10, "date_posted": "2020-04-28"},
    {"max_salary": 200, "min_salary": 101, "date_posted": "2020-05-05"},
]
jobs_sorterd_by_min = [
    {"max_salary": 1500, "min_salary": 10, "date_posted": "2020-04-28"},
    {"max_salary": 100, "min_salary": 50, "date_posted": "2020-05-08"},
    {"max_salary": 1000, "min_salary": 100, "date_posted": "2020-04-25"},
    {"max_salary": 200, "min_salary": 101, "date_posted": "2020-05-05"},
    {"max_salary": 50000, "min_salary": 200, "date_posted": "2020-05-02"},
    {"max_salary": 15000, "min_salary": 300, "date_posted": "2020-05-09"},
]
jobs_sorterd_by_max = [
    {"max_salary": 50000, "min_salary": 200, "date_posted": "2020-05-02"},
    {"max_salary": 15000, "min_salary": 300, "date_posted": "2020-05-09"},
    {"max_salary": 1500, "min_salary": 10, "date_posted": "2020-04-28"},
    {"max_salary": 1000, "min_salary": 100, "date_posted": "2020-04-25"},
    {"max_salary": 200, "min_salary": 101, "date_posted": "2020-05-05"},
    {"max_salary": 100, "min_salary": 50, "date_posted": "2020-05-08"},
]
jobs_sorterd_by_date = [
    {"max_salary": 15000, "min_salary": 300, "date_posted": "2020-05-09"},
    {"max_salary": 100, "min_salary": 50, "date_posted": "2020-05-08"},
    {"max_salary": 200, "min_salary": 101, "date_posted": "2020-05-05"},
    {"max_salary": 50000, "min_salary": 200, "date_posted": "2020-05-02"},
    {"max_salary": 1500, "min_salary": 10, "date_posted": "2020-04-28"},
    {"max_salary": 1000, "min_salary": 100, "date_posted": "2020-04-25"},
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == jobs_sorterd_by_min

    sort_by(jobs, "max_salary")
    assert jobs == jobs_sorterd_by_max

    sort_by(jobs, "date_posted")
    assert jobs == jobs_sorterd_by_date

    with pytest.raises(ValueError, match='invalid sorting criteria: None'):
        sort_by(jobs, None)

    with pytest.raises(ValueError, match='invalid sorting criteria: xablau'):
        sort_by(jobs, "xablau")
