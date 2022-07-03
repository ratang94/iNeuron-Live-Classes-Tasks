import logging

logging.basicConfig(filename="tuples.log", level=logging.DEBUG, format="%(levelname)s %(asctime)s %(message)s")


class Tuple_s:
    logging.info("accessing Tuple_s class")

    def __init__(self, l):
        self.l = l

    def extract_tuple(self):
        """To extract tuples from a collection"""
        logging.info("Inside extract_tuple class")
        try:
            for i in self.l:
                if type(i) == tuple:
                    logging.info(i)
                    print(i)
        except Exception as e:
            logging.error(e)

l = [[1,2,3,4], (2,3,4,5,6),(3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),
     {'k1':"sudh", 'k2':"ineuron", 'k3':"kumar", 3:6,7:8}, ["ineuron", "data science"]]
tup_var = Tuple_s(l)

tup_var.extract_tuple()