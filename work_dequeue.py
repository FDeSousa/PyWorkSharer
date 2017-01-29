
import threading


def run_dequeue_thread(queue, worker, poison_token=None):
    dq_thread = threading.Thread(name="work_dq_thread",
                                 target=dequeue,
                                 args=(queue, worker, poison_token))
    dq_thread.start()

def dequeue(queue, worker, poison_token):
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
