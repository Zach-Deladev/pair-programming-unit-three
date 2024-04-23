from lib.task_tracker import *
import pytest

def test_task_tracker_does_contain_string():
    result = task_tracker("#TODO buy an apple")
    assert result == True

def test_task_tracker_does_not_contain_string():
    result = task_tracker("buy an apple")
    assert result == False

def test_task_tracker_given_empty_string():
    with pytest.raises(Exception, match=r"No text given."):
        task_tracker("")