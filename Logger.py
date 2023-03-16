from datetime import datetime as dt

class Logger:
    @staticmethod
    def log_data(self, msg):
        time = dt.now().strftime('%D,%H,%M')
        with open('log.log', 'a') as file:
            file.write('{}, {}\n'.format(time, msg))


