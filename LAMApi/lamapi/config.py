class LAMConfiguration(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://lamapi:ajZ88Xi2ojnxq9baEUhZDEqhaEPDxpJvkXcest6bkvEiH8fLnI@localhost/louvoragapemontese'

    @property
    def SECRET_KEY(self):
        return 'kjqOQXTvEgd1Aj2JyZ5x7SRgS49J60n0qF0w3uEG0nyCa5KqmCt19CZIGzbp'