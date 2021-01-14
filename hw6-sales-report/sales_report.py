"""Generate sales report showing total melons each salesperson sold."""

def get_melons_sold_by_salesperson(file_path):

    """Return a dictionary of saleperson name and melons sold
    
    Arguments: 
        file_path (str) - the path to sales report log file

    Return:
        mels_by_sales (dict)
    
    """

mels_by_sales = {}

    with open(log_file_path) as f:
        for line in f:
            line = line.rstrip()

            # Create a list of data and unpack its values
            salesperson_name, total_dollars, melons_sold = line.split('|')

            # Set or increment the salesperson's total melons sold
            if salesperson_name in mels_by_sales:
                mels_by_sales[salesperson_name] += int(melons_sold)
            else:
                mels_by_sales[salesperson_name] = int(melons_sold)

    return mels_by_sales


def print_sales_report(melons_sold_by_salesperson):
    """Print a report of salespeople and the total no. of melons they've sold.

    Arguments:
        melons_sold_by_salesperson (dict) - {salesperson_name: melons_sold}
    """

    for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
        print(f'{salesperson_name} sold {melons_sold} melons')


print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))
