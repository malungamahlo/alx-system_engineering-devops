#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API to get the subscriber count 
  for a given subreddit.

  Args:
      subreddit: The name of the subreddit (e.g., "learnpython").

  Returns:
      The number of subscribers for the subreddit or 0 if it's invalid.
  """

  # Define the Reddit API endpoint URL with format string
  url = f"https://reddit.com/r/{subreddit}/about.json?limit=0"

  # Set a custom User-Agent header to avoid throttling
  headers = {"User-Agent": "My Reddit Subscriber Counter v1.0"}

  # Send a GET request without following redirects
  response = requests.get(url, allow_redirects=False, headers=headers)

  # Check for successful response (status code 200)
  if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract the subscriber count from the data dictionary (key may vary)
    return data.get("data", {}).get("subscribers", 0)
  else:
    # Request failed or redirected, return 0 for invalid subreddit
    return 0

# Example usage
subreddit_name = "learnpython"
subscribers = number_of_subscribers(subreddit_name)

if subscribers > 0:
  print(f"The subreddit r/{subreddit_name} has {subscribers} subscribers.")
else:
  print(f"Subreddit '{subreddit_name}' may not exist or is invalid.")

