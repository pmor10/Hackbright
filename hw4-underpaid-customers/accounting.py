MELON_COST = 1.00

def payment_status(file_name):

    customer_data = open(file_name)

    for order in customer_data:

        order = order.strip().split('|')

        customer_name = order[1]
        melons_qty = float(order[2])
        amount_paid = float(order[3])

        expected_price = MELON_COST * melons_qty

        # general info payment
        print(f"{customer_name} paid ${amount_paid}, expected ${expected_price}.")

        # check if over paid or underpaid
        if amount_paid > expected_price:
            print(f"OVERPAID>> {customer_name} has overpaid for their order.")
        
        elif amount_paid < expected_price:
            print(f"UNDERPAID>> {customer_name} has underpaid for their order.")

    customer_data.close()

payment_status("customer-orders.txt")