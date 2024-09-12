def oxford_comma(items):
    
    if len(items) == 1:
        return items[0]
    
    if len(items) == 2:
        return ' and '.join(items)
    
    # For three or more items
    return ', '.join(items[:-1]) + ', and ' + items[-1]
print(oxford_comma(['']))
    
