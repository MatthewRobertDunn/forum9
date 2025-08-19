# thread_scope.py
from contextlib import contextmanager
import contextvars

thread_id_var = contextvars.ContextVar("thread_id")


def set_thread_id(thread_id):
    thread_id_var.set(thread_id)


def current_thread_id():
    return thread_id_var.get(None)  # default to None if not set


@contextmanager
def thread_scope(thread_id):
    token = thread_id_var.set(thread_id)  # save previous value
    try:
        yield
    finally:
        thread_id_var.reset(token)  # restore previous value
