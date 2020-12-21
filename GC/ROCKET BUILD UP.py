
current = int(input('What is the current time in 24 hours? '))

endtime = (51 + current)%24
days = (51-51%24)/24

print("Charge up complete in " + str(days) + " days at " + str(endtime) + ":00")

