from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-03-27"},
        {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-03-27"},
        {"min_salary": 9000, "max_salary": 11000, "date_posted": "2022-03-27"},
    ]

    result_min_salary = [jobs[0], jobs[1], jobs[2]]
    result_max_salary = [jobs[2], jobs[1], jobs[0]]

    sort_by(jobs, "min_salary")
    assert jobs == result_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == result_max_salary
