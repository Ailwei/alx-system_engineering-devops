#!/usr/bin/env ruby

# Get the argument from the command line
input_string = ARGV[0]

# Define the regular expression to match the specified cases without square brackets
regex = /hbt{1,}n/

# Use the scan method to find matches and join the results
matches = input_string.scan(regex).join

# Print the result
puts matches
