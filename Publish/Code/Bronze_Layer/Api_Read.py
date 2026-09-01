# The API read rate limit should not exceed 10 req/sec
#We will test with APPLE CIK first 0000320193  
rate_limit = 10  # requests per second
CIK = "0000320193"  # CIK for Apple Inc.
#https://data.sec.gov/submissions/CIK0000320193.json
#https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json
import time
import requests




