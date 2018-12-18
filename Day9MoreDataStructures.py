us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'


def get_every_nth_state(n=10):
    """Return a list with every nth item (default 10th item)
       of states (takeaway: lists keep order)"""
    return (states[::n])                #syntax for nth item. n is argument
#print(get_every_nth_state())



def get_state_abbrev(abbrev):
    """Look up a state abbreviation by full name in
       us_state_abbrev, if not found return the string stored in the
       NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    try:
        return (us_state_abbrev[abbrev])
    except:
        return (NOT_FOUND)
#print(get_state_abbrev("Virginia"))
#print(get_state_abbrev("Nor Carolina"))

def get_longest_state_in_list(data):
    """Takes dict or list and determines the longest state name
       (takeaways: use a dict method to get all keys, use sorted)"""  
    return (max(states, key=len))           #does the same but in one line
#print(get_longest_state_in_list(states))
    
def longest_state(data):
    cur_longest = []
    cur_longest_num = 0
    for state in data:
        if len(state) == cur_longest_num:
            cur_longest.append(state)
        elif len(state) > cur_longest_num:
            cur_longest = [state]
            cur_longest_num = len(state)
    return cur_longest
print(longest_state(states))

def get_longest_state_in_dict(data):
    """Takes dict and determines the longest state name
    (takeaways: use a dict method to get all keys, use sorted)"""
    for keys in data.keys():
        return(max(states, key=len))
#print(get_longest_state_in_dict(us_state_abbrev))


def combine_state_names_and_abbreviations():
    """Return a new list with the first 10 abbreviations from the
       us_state_abbrev dict ordered values and the last 10 states from
       the states list (takeaways: use another dict method to get all
       values and use sorted, list slicing and list concatenation)"""
    state_abbrevs = []
    state_names = []
    for value in us_state_abbrev.values():
        state_abbrevs.append(value)
    for state in states:
        state_names.append(state)
    return(state_abbrevs[:10], state_names[-10:])
print(combine_state_names_and_abbreviations())