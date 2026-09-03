import time

from Publish.Code.Bronze_Layer.Api_Rate_Limiter import RateLimiter


def test_rate_limiter_enforces_5_requests_per_second():
    limiter = RateLimiter(5)

    first_start = time.monotonic()
    limiter.wait()
    first_elapsed = time.monotonic() - first_start

    second_start = time.monotonic()
    limiter.wait()
    second_elapsed = time.monotonic() - second_start

    assert first_elapsed < 0.2
    assert second_elapsed >= 0.15
