#!/usr/bin/env ruby

# Get the argument from the command line


input_string = ARGV[0]

# Define the regular expression to match "School"

regex = /School/

# Use the scan method to find matches an join the results


matches = input_string.scan(regex).join

# Print the result

puts matches
