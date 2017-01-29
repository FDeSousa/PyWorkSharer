
try:
    import multiprocessing
except ImportError:
    import multiprocessing.dummy as multiprocessing


class Configuration:
    cpu_count = multiprocessing.cpu_count()
