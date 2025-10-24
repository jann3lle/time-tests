import pytest
from datetime import datetime
from times import time_range, compute_overlap_time

def test_time_range_single_interval():
    result = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    assert result == [("2010-01-12 10:00:00", "2010-01-12 11:00:00")]

def test_time_range_two_intervals_with_gap():
    result = time_range("2010-01-12 10:00:00", "2010-01-12 10:20:00", 2, 60)
    start1, end1 = result[0]
    start2, end2 = result[1]

    assert len(result) == 2

    t1_end = datetime.strptime(end1, "%Y-%m-%d %H:%M:%S")
    t2_start = datetime.strptime(start2, "%Y-%m-%d %H:%M:%S")
    gap = (t2_start - t1_end).total_seconds()
    assert gap == pytest.approx(60)

def test_compute_overlap_time():
    range1 = [("2010-01-12 10:00:00", "2010-01-12 12:00:00")]
    range2 = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]
    result = compute_overlap_time(range1, range2)
    assert result == [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]

def test_compute_overlap_time_no_overlap():
    range1 = [("2010-01-12 09:00:00", "2010-01-12 09:30:00")]
    range2 = [("2010-01-12 10:00:00", "2010-01-12 10:30:00")]
    result = compute_overlap_time(range1, range2)
    low, high = result[0]
    assert low >= high

