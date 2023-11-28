#!/usr/bin/env ruby

# Get the argument from the command line
input_string = ARGV[0]

# Define the regular expression to match a 10-digit phone number
regex = /^\d{10}$/

# Use the match method to check if the input matches the pattern
match_result = input_string.match(regex)

# Print the result
puts match_result ? match_result[0] : ''
