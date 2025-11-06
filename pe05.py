#1) Make_shirt 
def make_shirt(size, message):  #call with positional and keyword args
    print(f"Making a {size} shirt with the message: '{message}'")


make_shirt("M", "One Life") # positional call
make_shirt(size="L", message="Love Others") # keyword call

print("-" * 40) #Makes a ----- Keeping terminal clean and for testing code

#2) make_shirt w/ default large
def make_shirt_default(size="L", message="I love Python"): # large shirt default w/ default message 
    print(f"Making a {size} shirt with the message: '{message}'") # paste any size shirt w/ custom message 


make_shirt_default()# Large default shirt w/ default message 

make_shirt_default("M")# medium w/ default message

make_shirt_default(size="S", message="Be Nice")# any size w/ custom message

print("-" * 40) #Makes a ----- Keeping terminal clean and for testing code

#3) describe city 

def describe_city(city, country="Vietnam"): #describes the city and country which is vietnam default
    print(f"{city} is in {country}.") # makes a override w/ a city and a country you can paste

describe_city("Saigon")              # default country
describe_city("Seattle", "USA")      # override default
describe_city("Tokyo", "Japan")      # override default
describe_city("Toronto", "Canada")   # override default

print("-" * 40) #Makes a ----- Keeping terminal clean and for testing code

#4) show message

def show_messages(messages): # function that takes list as message
    for msg in messages: # Loop through list
        print(msg)  # Print the current message

msgs = ["Keep going, you're almost there"] # writing messages to print 
show_messages(msgs) # call function displaying message one by one 

print("-" * 40) #Makes a ----- Keeping terminal clean and for testing code

#5) String count

def count(string):  # function that takes a string as input
    upper_count = 0  # uppercase counter
    lower_count = 0  # lowercase counter

    for character in string:         # loop through each character 
        if character.isupper():      # check if uppercase
            upper_count += 1         # plus 1 uppercase
        elif character.islower():    # check if lowercase
            lower_count += 1         # plus 1 lowercase

    print("No. of Upper case characters:", upper_count)  # print total uppercase letters
    print("No. of Lower case characters:", lower_count)  # print total lowercase letters


sample = "The quick Brow Fox"  # sample string to test the function
count(sample)  # call the function with the sample string
