#!/usr/bin/env ruby

#get the argument from commandline

input_string = ARGV[0]

# Define the regular expression to match join the results

regex = /hbt{2,5}n/

# Use the scan method to find matches and join 

matches = input_string.scan(regex).join

#Print the result

puts matches
