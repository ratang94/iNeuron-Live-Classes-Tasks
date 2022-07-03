import logging

logging.basicConfig(filename="Dict_s.log", level=logging.DEBUG, format="%(levelname)s  %(asctime)s %(message)s")


class Dict_s:
    logging.info("Accessing Dict_s class")

    def __init__(self, d):
        self.d = d

    def lvl2nesting(self):
        """ Function taking input as dictionary with 2nd level nesting and returning list"""
        logging.info("Inside lvl2nesting function")
        try:
            self.d = d
            self.l = []
            if type(self.d) != dict:
                raise ValueError("Only dictionary input is allowed")
            else:
                logging.info("input provided is dictionary")
                for i in list(self.d.keys()):
                    if type(i) not in (set, tuple):
                        self.l.append(i)
                        logging.info(self.l)
                    else:
                        self.l.extend(i)
                        logging.info(self.l)
                for j in list(self.d.values()):
                    if type(j) not in (list, dict, set, tuple):
                        self.l.append(j)
                        logging.info(self.l)
                    elif type(j) in (list, tuple, set):
                        self.l.extend(j)
                        logging.info(self.l)
                    elif type(j) == dict:
                        for k in list(j.keys()):
                            if type(k) not in (set, tuple):
                                self.l.append(k)
                                logging.info(self.l)
                            else:
                                self.l.extend(k)
                                logging.info(self.l)
                        for m in list(j.values()):
                            if type(m) not in (list, dict, set, tuple):
                                self.l.append(m)
                                logging.info(self.l)
                            elif type(m) in (list, tuple, set):
                                self.l.extend(m)
                                logging.info(self.l)
            logging.info("output %s", self.l)
            return self.l
        except ValueError as v:
            logging.error(v)
            return v
        except Exception as e:
            logging.error(e)
            return e

    dict_sq = lambda x: {'square': [i ** 2 for i in x], 'cube': [i ** 3 for i in x]}

    def sq_dict(self, *x):
        """ returns a dictionary with square and cubes inside it"""
        logging.info("Inside sq_dict function")
        try:
            self.x = x
            logging.info("input %s", self.x)
            return Dict_s.dict_sq(self.x)
        except Exception as e:
            logging.exception(e)
            return e


d = {'1': [1, 2, 3], '2': {'3': [1, 2, 3], 'a': ['an', 'ku', 'r']}}

dict_var = Dict_s(d)

print(dict_var.lvl2nesting())
