# HotWorker

**Unix-friendly HotQueue worker processes.**

**Author:** Jamie Matthews. [Follow me on Twitter](http://twitter.com/j4mie).

## Documentation

This module allows you to create worker processes that listen on [HotQueue](http://richardhenry.github.com/hotqueue/)
queues. Your workers will gracefully shut down when they receive a Unix signal telling them to exit, finishing with
the item currently being processing first. Uses [simplesignals](https://github.com/j4mie/simplesignals/) for signal
handling.

    from hotworker import worker

    @worker
    def printer(item):
        print item

    if __name__ == "__main__":
        printer()

Run this worker at the command line or with a process monitor such as [Circus](http://circus.io). Then, in your main program:

    from hotqueue import HotQueue

    queue = HotQueue('printer')
    queue.put("Hello from HotWorker")

#### 0.2.0

* Add a `startup` function to wait for a Redis connection

#### 0.1.0

* Initial release.

## Installation

You can install hotworker from PyPI:

    pip install hotworker

## Development

To contribute: fork the repository, make your changes, add some tests, commit,
push to a feature branch, and open a pull request.

## (Un)license

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this
software, either in source code form or as a compiled binary, for any purpose,
commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
