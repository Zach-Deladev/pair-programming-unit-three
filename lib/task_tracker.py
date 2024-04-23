def task_tracker(str):
    if len(str) == 0:
        raise Exception("No text given.")
    return "#TODO" in str
