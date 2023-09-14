def hours_to_seconds(hours):
   
# Convert time from hours to seconds.
      
    seconds = hours * 3600
    return seconds

# Ask the user for input
hours = float(input("Enter time in hours: "))

# Perform the conversion
seconds = hours_to_seconds(hours)

# Display the result
print(f"{hours} hours is equal to {seconds} seconds")
