import datetime as dt

def getDate():
    """
    Return todays date
    """
    # datetime format => 2020-02-29 16:55:38.717109
    date = dt.datetime.today()
    date = str(date).split(" ")[0]
    return date
