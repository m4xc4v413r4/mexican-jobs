"""Required constants for the Reddit API."""

# The following constants are used by both bots.
REDDIT_USERNAME = ""
REDDIT_PASSWORD = ""
APP_ID = ""
APP_SECRET = ""
USER_AGENT = "EmpleosBot v0.2"

# 0 for local time, 5 for Mexico Central Time.
DELTA_HOURS = 0

# Seconds in a day multiplied for the number of days.
JOBS_MAX_AGE = 86400 * 3

# The threads that the post_bot will keep updating.
POST_IDS = ["93i25l", "93i25l"]

# The threads the comments_bot will keep checking for new comments.
SUBMISSION_IDS = ["938fpu", "93i25l", "93au4i", "952ifq"]
