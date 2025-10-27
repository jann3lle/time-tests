import pytest
from datetime import datetime
# Import functions from times.py
from times import time_range, compute_overlap_time


def test_time_range_single_interval():
    result = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    assert result == [("2010-01-12 10:00:00", "2010-01-12 11:00:00")]