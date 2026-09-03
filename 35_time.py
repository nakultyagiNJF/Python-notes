#! Python Dates:------->
#* A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

# file import only one time on the head section.
import datetime
 
today = datetime.datetime.now()
print(today) # 2025-09-12 10:36:54.935880

print("Year :", today.year) # Year : 2025
print("Month :", today.month) # Month : 9
print("Day :", today.day) # Day : 12
print("Hour :", today.hour) # Hour : 10
print("Minute :", today.minute) # Minute : 36
print("Second :", today.second) # Second : 54


print(today.strftime("%a")) # Fri

#? create date objects:--------->
#* To create a date object, use the datetime() class.

# example:
myDate = datetime.datetime(2005, 9, 6)
print(myDate)

#? A reference to the legal format codes:--------->>

"""
    Directive	Description	                                                            Example	
        %a	        Weekday, short version	                                              Wed	
        %A	        Weekday, full version	                                            Wednesday	
        %w	        Weekday as a number 0-6, 0 is Sunday	                                3	
        %d	        Day of month 01-31	                                                    31	
        %b	        Month name, short version	                                           Dec	
        %B	        Month name, full version	                                         December	
        %m	        Month as a number 01-12	                                                12	
        %y	        Year, short version, without century	                                18	
        %Y	        Year, full version                                                     2018	
        %H	        Hour 00-23	                                                            17	
        %I	        Hour 00-12	                                                            05	
        %p	        AM/PM	                                                                PM	
        %M	        Minute 00-59	                                                        41	
        %S	        Second 00-59	                                                        08	
        %f	        Microsecond 000000-999999                                         	548513	
        %z	        UTC offset	                                                          +0100	
        %Z	        Timezone	                                                           CST	
        %j	        Day number of year 001-366	                                           365	
        %U	        Week number of year, Sunday as the first day of week, 00-53	            52	
        %W	        Week number of year, Monday as the first day of week, 00-53	            52	
        %c	        Local version of date and time	                                Mon Dec 31 17:41:00 2018	
        %C	        Century	                                                                20	
        %x	        Local version of date	                                              12/31/18	
        %X	        Local version of time	                                              17:41:00	
        %%	        A % character	                                                          %	
        %G	        ISO 8601 year	                                                         2018	
        %u	        ISO 8601 weekday (1-7)	                                                  1	
        %V	        ISO 8601 weeknumber (01-53)	                                             01
"""

# some examples:----->>
today = datetime.datetime.now()

# using methods:--->>
print(today.strftime("%a"))
print(today.strftime("%A"))
print(today.strftime("%b"))
print(today.strftime("%B"))
print(today.strftime("%p"))
print(today.strftime("%c"))
print(today.strftime("%x"))
print(today.strftime("%X"))
print(today.strftime("%G"))
print(today.strftime("%V"))
print(today.strftime("%j"))