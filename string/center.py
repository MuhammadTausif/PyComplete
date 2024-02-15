# Example No 3:
event = "Python Developers Meetup"
date = "April 30th"
time = "6:00 PM"
location = "Tech Hub Downtown"

invitation = f"""
{'*' * 40}
{event.center(40)}
{date.center(40)}
{time.center(40)}
{location.center(40)}
{'*' * 40}
"""

print(invitation)