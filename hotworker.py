from simplesignals.process import WorkerProcessBase
from hotqueue import HotQueue


class HotWorkerBase(WorkerProcessBase):

    """
    Base class for worker processes that handle items
    from HotQueue Redis queues.
    """

    queue_name = 'queue'

    def __init__(self):
        self.queue = self.get_queue()
        super(HotWorkerBase, self).__init__()

    def get_queue(self):
        return HotQueue(self.queue_name)

    @property
    def process_title(self):
        return "hotworker-%s" % self.queue_name

    def do_work(self):
        item = self.queue.get(block=True, timeout=1)
        if item:
            self.process_item(item)

    def process_item(self, item):
        raise NotImplementedError()

    def __call__(self):
        self.run()


def worker(*args, **kwargs):

    """
    Shortcut decorator for creating HotQueue worker processes

        @worker
        def printer(item):
            print item
        printer()

    The decorator also accepts arguments: queue_name specifies the
    name of the queue the worker will listen on. All other kwargs
    are passed into the HotQueue constructor.
    """

    def decorator(func):

        queue_name = kwargs.pop('queue_name', func.__name__)

        class Worker(HotWorkerBase):

            @property
            def queue_name(self):
                return queue_name

            def get_queue(self):
                return HotQueue(queue_name, **kwargs)

            def process_item(self, item):
                func(item)

        w = Worker()
        return w

    # Make sure the decorator works with or without arguments
    if len(args) == 1 and callable(args[0]):
        return decorator(args[0])
    return decorator
