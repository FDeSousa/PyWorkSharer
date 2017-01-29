
def dequeue_worker(queue, worker, poison_token=None):
    is_joinable_queue = hasattr(queue, 'task_done')

    poisoned = False
    while not poisoned:
        try:
            item = queue.get()

            if item == poison_token:
                poisoned = True
            else:
                worker(item)
        except:
            pass
        finally:
            if is_joinable_queue:
                queue.task_done()
