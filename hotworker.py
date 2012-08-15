from simplesignals.process import WorkerProcessBase
from hotqueue import HotQueue
from redis.exceptions import ConnectionError
from time import sleep, time


class HotWorkerBase(WorkerProcessBase):

    """
    Base class for worker processes that handle items
    from HotQueue Redis queues.
    """

    queue_name = 'queue'

    STARTUP_TIMEOUT = 10  # seconds to wait for a Redis conn on startup

    def __init__(self):
        self.queue = self.get_queue()
        super(HotWorkerBase, self).__init__()

    def get_queue(self):
        return HotQueue(self.queue_name)

    @property
    def process_title(self):
        return "hotworker-%s" % self.queue_name

    def startup(self):
        """Wait for a Redis connection to be available. Under normal
        circumstances (if Redis is running) this code should ping Redis
        once and then return."""
        redis = self.queue._HotQueue__redis
        start_time = time()

        while time() - start_time <= self.STARTUP_TIMEOUT:
            try:
                redis.ping()
                return  # everything's fine!
            except ConnectionError:
                sleep(0.5)

        # If we got here, we failed to connect to Redis at all
        raise ConnectionError("Failed to connect to Redis after %s"
                              " seconds" % self.STARTUP_TIMEOUT)

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
