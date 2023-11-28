#!/usr/bin/env ruby

# Get the log entry from the command line
log_entry = ARGV[0]

# Define the regular expression to extract information from the log entry
regex = /\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/

# Use the match method to check if the input matches the pattern
match_result = log_entry.match(regex)

# Print the result in the specified format
puts "#{match_result[1]},#{match_result[2]},#{match_result[3]}"
