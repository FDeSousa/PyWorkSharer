
try:
    import multiprocessing
except ImportError:
    import multiprocessing.dummy as multiprocessing

from . import configuration


def run_worker_pool(work_queue, configuration):
    with multiprocessing.Pool(max_workers=configuration.cpu_count) as pool:
        pass
