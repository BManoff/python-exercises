# %%
#1.) Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    return x == 2 or x == "2"

is_two(2)

# %%
#2.) Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(vowel):
   if vowel in "aeiou":
       return True
   else:
        return False


is_vowel("a")

# %%
#3.)Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(consonant):
   if consonant not in "aeiou":
       return True
   else:
        return False

is_consonant("b")

# %%
#4.)Define a function that accepts a string that is a word.
#  The function should capitalize the first letter of the word if the word starts with a consonant

def is_a_word(word):
    if type(word) != str:
        return False
    if word[0] not in "aeiou":
       return word.capitalize()
    else:
        return word

is_a_word("all")


# %%
#5.) Define a function named calculate_tip.
#  It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(bill):
    return bill * 0.25

calculate_tip(50)

# %%
#6.) Define a function named apply_discount.
#  It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original, discount):
    return original - (original * discount)

apply_discount(5, 0.25)



# %%
#7.) Define a function named handle_commas.
#  It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(comma_string):
    comma_string = comma_string.replace(",", "")
    return comma_string
    

handle_commas("Hi, how are you?")

# %%
#8.) Define a function named get_letter_grade.
#  It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(number):
    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70: 
        return "C"
    elif number >= 60: 
        return "D"
    else:
        return "F"

get_letter_grade(82)

# %%
#9.) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed

def is_vowel(vowel):
  vowel = vowel.lower()
  return vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u"


def remove_vowels(astring):
  for character in astring:
    if is_vowel(character):
       astring = astring.replace(character, "")

  return astring

remove_vowels("Hi how are you doing?")

# %%
#10.) Define a function named normalize_name. It should accept a string and return a valid python identifier

def remove_special_char(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])

def normalize_name(name):
    special_char_removed = remove_special_char(name)
    return special_char_removed.lower().strip().replace(" ", "_")
    

normalize_name(" % Hot sauce")


# %%
#11.) Write a function named cumulative_sum that accepts a list of numbers
#     and returns a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(nums):
    output = []
    total = 0
    for num in nums:
        total += num 
        output.append(total)
    return output

cumulative_sum([1, 1, 1])


