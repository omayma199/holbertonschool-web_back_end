def index_range(page, page_size):
    # Calculate the start index
    start_index = (page - 1) * page_size
    
    # Calculate the end index
    end_index = start_index + page_size
    
    return (start_index, end_index)

# Example usage:
page = 3
page_size = 10
start, end = index_range(page, page_size)
print(f"Start index: {start}, End index: {end}")
