# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%

tax = .05   # default state tax amount


def tax_calculator(tax, state, item_cost):
    """Calculates total cost including tax.

    Takes tax, mulitiplies times the item cost to find out the specific
    tax amount for the item, then adds the tax amount to the item_cost to
    evaluate the cost of the item with tax.

    State input is primarily to check if state is California (CA). If so,
    tax is .07 and will do same calculation with adjusted tax rate.

    Changes case of state input to uppercase for simplified check if state is
    CA or not."""

    state = state.upper()      # capitalize input, for ease w/ if conditional

    if state != 'CA':
        total = item_cost + (float(item_cost) * tax)

    else:
        tax = .07      # You get what you pay for & CA is better
        total = item_cost + (float(item_cost) * tax)

    print total
    return total


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def is_berry(fruit):
    """Checks if input string is a berry fruit.

    Sets case of input fruit to lower case for easier comparison. If
    the fruit given is 'strawberry', 'cherry', or 'blackberry', will return
    True. Otherwise, will return False."""

    
    fruit = fruit.lower()  # makes all lower case for ease in comparison

    if fruit == 'strawberry' or fruit == 'cherry' or fruit == 'blackberry':
        return True
    else:
        return False

# is_berry('CHERRY')


def shipping_cost(fruit):
    """Returns shipping cost based on whether fruit is a berry or not.

    Calls the is_berry function to evaluate if the input string in
    shipping_cost is a berry. If is_berry returns True, shipping cost will be
    zero. For all other inputs for fruit, shipping cost will be 5."""


    fruit_shipping = is_berry(fruit)

    if fruit_shipping is True:
        return 0
    else:
        return 5

#  shipping_cost('BLACKBERRY')

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#

my_hometown = 'tracy'

def is_hometown(town):
    """Checks if town is also Jennifer D's hometown.

    Takes input string town and changes to all lowercase for easier
    evaluation. If input is 'tracy' (for Tracy, CA), will return True.
    Otherwise will return False."""
    

    town = town.lower()
    if town == my_hometown:
        return True
    else:
        return False


#  is_hometown('Tracie')


#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#

def full_name(first, last):
    """

    """

    print '{} {}'.format(first, last)


#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(hometown, first, last):
    """

    """

    hometown = hometown.lower()
    same_city = is_hometown(hometown)

    if same_city is True:
        print 'Hi, {} {}, we\'re from the same place!'.format(first, last)
    else:
        print 'Hi {} {}, where are you from?'.format(first, last)

# hometown_greeting('Fresno', 'MC', 'Hammer')

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################