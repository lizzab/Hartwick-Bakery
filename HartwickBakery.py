# Temur Khabibullaev
Cookies = []
Candy = []
# Function that gets an input from user in a loop
def cookie_input():
    for i in range(0,6):
        getting_values = int(input("Give a value of COOKIES for each month starting from first:\n> "))
        Cookies.append(getting_values)
        print(Cookies)

# Function that gets an input from user in a loop
def candy_input():
    for i in range(0,6):
        getting_values = int(input("Give a value of CANDIES for each month starting from first:\n> "))
        Candy.append(getting_values)
        print(Candy)

# Function that calculates average(I could have done better, but nah it's ok)
def average_sales_cookies():
    av = (Cookies[0] + Cookies[1] + Cookies[2] + Cookies[3] + Cookies[4] + Cookies[5]) / 6
    return av

# Function that calculates average(I could have done better, but nah it's ok)
def average_sales_candy():
    av = (Candy[0] + Candy[1] + Candy[2] + Candy[3] + Candy[4] + Candy[5]) / 6
    return av

# Function that defines max and min
def max_min_cookies():
    print("Here is the maximum number of cookies:\n",max(Cookies))
    print("Here is the minimum number of cookies:\n",min(Cookies))

# Function that defines max and min
def max_min_candy():
    print("Here is the maximum number of candies:\n",max(Candy))
    print("Here is the minimum number of candies:\n",min(Candy))

# Function that defines popularity of cookies or candies
def which_more_popular():
    if average_sales_cookies() > average_sales_candy():
        print("Cookies are more popular these days.")
    elif average_sales_cookies() < average_sales_candy():
        print("Candies are more popular these days.")
    else:
        print("...")

# Function that start a program
def start():
    cookie_input()
    candy_input()
    print("Average sales for cookies:\n",average_sales_cookies())
    print("Average sales for candies:\n",average_sales_candy())
    max_min_cookies()
    max_min_candy()
    which_more_popular()

start()

# Table
print(f"""          Months        Cookies      Candy
        ------------------------------------
        |Month 1|        |{Cookies[0]}|        |{Candy[0]}|
        |Month 2|        |{Cookies[2]}|        |{Candy[2]}|
        |Month 4|        |{Cookies[3]}|        |{Candy[3]}|
        |Month 5|        |{Cookies[4]}|        |{Candy[4]}|
        |Month 6|        |{Cookies[5]}|        |{Candy[5]}|
        ------------------------------------
""")
