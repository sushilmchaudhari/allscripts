def time_calc(time_in_seconds):
    time_in_seconds = float(time_in_seconds)
    day = time_in_seconds // (24 * 3600)
    time_in_seconds = time_in_seconds % (24 * 3600)
    hour = time_in_seconds // 3600
    time_in_seconds %= 3600
    minutes = time_in_seconds // 60
    time_in_seconds %= 60
    seconds = time_in_seconds
    out = "%d:%d:%d:%d" % (day,hour,minutes,seconds)
    return out

