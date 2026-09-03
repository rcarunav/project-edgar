import sys
from pathlib import Path
import time

# Automatically finds the project root (FabricDataEngineer) and adds it to Python's path
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

# Now this import will work anywhere!
from Publish.Code.Bronze_Layer.Api_Rate_Limiter import RateLimiter


def fake_api_call(cik):
    """Simulates an API call that returns some fake JSON data."""
    return {"cik": cik, "status": "200 OK"}


# 1. Initialize Rate Limiter at 5 requests/sec (0.20s interval)
limiter = RateLimiter(requests_per_second=5)

print("\n--- Starting 5 Fake API Calls ---")
start_time = time.monotonic()
last_time = start_time

for i in range(1, 6):
    limiter.wait()  # This throttles the call

    current_time = time.monotonic()
    gap_from_last = current_time - last_time
    total_elapsed = current_time - start_time
    last_time = current_time

    # Make the fake API call
    response = fake_api_call(f"CIK000000000{i}")

    print(
        f"Call {i} | Response: {response['status']} | "
        f"Time from start: {total_elapsed:.3f}s | "
        f"Gap since last call: {gap_from_last:.3f}s"
    )

print("--- Done! ---\n")