# Example data for a user, the time of their visit and the site they accessed.
# Print a log message with the username, url, and timestamp replaced with values from the appropriate variables

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

print(username + ' accessed the site ' + url + ' at ' + timestamp + '.')