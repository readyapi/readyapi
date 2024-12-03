import pytest
from readyapi.concurrency import contextmanager_in_threadpool
from readyapi.testclient import TestClient
from contextlib import contextmanager
import time

@contextmanager
def sample_context_manager():
    print("Entering context")
    yield "context value"
    print("Exiting context")

def test_contextmanager_in_threadpool():
    with contextmanager_in_threadpool(sample_context_manager()) as value:
        assert value == "context value"

def test_contextmanager_in_threadpool_exception():
    @contextmanager
    def faulty_context_manager():
        print("Entering context")
        raise ValueError("An error occurred")
        yield "context value"
        print("Exiting context")

    with pytest.raises(ValueError, match="An error occurred"):
        with contextmanager_in_threadpool(faulty_context_manager()) as value:
            pass

def test_contextmanager_in_threadpool_cleanup():
    cleanup_called = False

    @contextmanager
    def context_manager_with_cleanup():
        nonlocal cleanup_called
        try:
            yield "context value"
        finally:
            cleanup_called = True

    with contextmanager_in_threadpool(context_manager_with_cleanup()) as value:
        assert value == "context value"

    assert cleanup_called
