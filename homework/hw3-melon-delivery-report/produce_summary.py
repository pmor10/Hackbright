def produce_summery(day_num, day_file):

    """Given day num and files to get the produce report
    opens the delivery file and generates report.
    """

    print("Day", day_num)

    the_file = open(day_file)

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")

    the_file.close()

produce_summery(1, "um-deliveries-20140519.txt")
produce_summery(2, "um-deliveries-20140520.txt")
produce_summery(3, "um-deliveries-20140521.txt")

