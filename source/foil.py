# storing the data from the 6_25_18 mpfd irradiation


class Foil(object):
    def __init__(self, peak_area, peak_error, activity, activity_error,
                 counting_time):
        self.peak_area = peak_area
        self.peak_error = peak_error
        self.activity = activity
        self.t_c = counting_time
        self.activity_error = activity_error
