from warnings import warn


class ReadabilityException(Exception):
    pass

def minimum_words_warning():
    warn('100 words required for optimal accuracy.')