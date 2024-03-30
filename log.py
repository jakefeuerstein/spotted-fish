class Log:
    def __init__(self, time, location, activity, observed, caught):

        def filter_format(log_input, value):
            match log_input:
                case 'time':
                    return value
                case 'location':
                    return value
                case 'activity':
                    return value
                case 'observed':
                    return value
                case 'caught':
                    return value

        self.time = filter_format('time', time)
        self.location = filter_format('location', location)
        self.activity = filter_format('activity', activity)
        self.observed = filter_format('observed', observed)
        self.caught = filter_format('caught', caught)

    def get_log(self):
        return {
            'time': self.time,
            'location': self.location,
            'activity': self.activity,
            'observed': self.observed,
            'caught': self.caught
        }