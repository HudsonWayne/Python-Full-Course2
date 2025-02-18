#dictionary = A changeable, unordered collection 
#                   of  unique key:value pairs

# Fast because they use hashing, allowing us to access a values quickly


capitals = {'USA': 'Washington DC',
            'UK': 'London',
            'Germany': 'Berlin',
            'France': 'Paris',
            'Japan': 'Tokyo'
            
            }

for key, value in capitals.items():
    print(key, value)