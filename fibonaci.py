import logging

def fibonaci(input_list):
    next_entry = input_list[-2] + input_list[-1]
    input_list.append(next_entry)
    if next_entry <= 100:
        logging.warning("this iteration is {}".format(next_entry))
        fibonaci(input_list)
    else:
        logging.warning("this is the last iteration {}".format(next_entry))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_list = [0, 1]
    fibonaci(start_list)