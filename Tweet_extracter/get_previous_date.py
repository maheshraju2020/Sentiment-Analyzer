# This script gives the previous date of the the given date, for getting tweets from that day eventually
from calendar import monthrange


def getYear(orig_date_arr):
    """
    return an integer specifying the previous Year
    """
    if orig_date_arr[1] == orig_date_arr[2] == 1:
        return orig_date_arr[0] - 1
    else:
        return orig_date_arr[0]


def getMonth(orig_date_arr):
    """
    return an integer specifying the previous month
    """
    if orig_date_arr[2] == 1:
        if orig_date_arr[1] == 1:
            return 12
        return orig_date_arr[1] - 1
    else:
        return orig_date_arr[1]


def getDate(orig_date_arr):
    """
    return an integer specifying the previous date
    """
    if orig_date_arr[2] != 1:
        return orig_date_arr[2] - 1
    else:
        if orig_date_arr[1] == 1:
            return 31
        else:
            return monthrange(orig_date_arr[0], orig_date_arr[1]-1)[1]


def prev_date_getter(date):
    """
    call subroutines to calculate the previous date from the given date, and return the previous date
    """
    orig_date_arr = list(map(int, date.split("-")))
    prev_date_arr = orig_date_arr[:]
    prev_date_arr[0] = getYear(orig_date_arr)
    prev_date_arr[1] = getMonth(orig_date_arr)
    prev_date_arr[2] = getDate(orig_date_arr)
    return "-".join(map(str, prev_date_arr))
