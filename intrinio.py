from log3 import log
import cPickle as pickle
import requests
import os

class Intrinio(object):
    def __init__(self, username, password):
        self.username = os.environ.get('INTRINIO_USERNAME')
        self.password = os.environ.get('INTRINIO_PASSWORD')
        self.url =  'https://api.intrinio.com/securities/search?conditions=marketcap~lt~200000000&page_size=500'

    def save(self, stocks, pickle_name):
        """ pickles the result for later use"""

        # pickle stocks object for later reuse
        log.info("Pickling object stocks as {pickle_name}".format(pickle_name=pickle_name))
        pickle.dump(stocks, open(pickle_name, "wb"))

    def get_stocks(self):

        retries = 4
        stocks = []

        try:
            log.info("Getting request for stock screener")
            resp = requests.get(self.url, auth=(self.username, self.password), timeout=10)
            resp.raise_for_status()

        except requests.HTTPError as http_error:
            log.error("Server returned the following HTTP Error: {http_error}".format(http_error=http_error))

        except requests.exceptions.Timeout:
            log.error('Timeout')

        else:
            log.info('SUCCESS')
            try:
                log.info( "Trying to read json file . . .")
                data1 = resp.json()
            except Exception as ex:
                print ex
            else:
                if 'errors' in data1:
                    print  data1['errors'][0]['human']
                    raise ValueError(data1['errors'][0]['human'])

                else:
                    log.info('SUCCESS')
                    total_pages = data1['total_pages']
                    result_count = data1['result_count']
                    log.info("Total pages: {total_pages} \tresult_count: {result_count}"
                             .format(total_pages=total_pages,result_count=result_count))

                    stocks = []

                    for p in range(1, total_pages+1):

                        url_new = self.url + "&page_number=" + str(p)

                        for r in range(retries):
                            try:
                                log.debug(" Going to page number {p}".format(p=p))
                                resp = requests.get(url_new, auth=(self.username, self.password), timeout=10)

                                if resp.status_code == 503:
                                    log.error("503 Error: Server is too busy. Retrying again")
                                    resp.raise_for_status()

                            except Exception as ex:
                                print ex
                                continue
                            else:
                                log.info("SUCCESS")
                                data = resp.json()
                                for stock in data['data']:
                                    stocks.append(str(stock['ticker']))
                                break
                return stocks


if __name__ == '__main__':

    intrinio = Intrinio(username, password)

    symbols = intrinio.get_stocks()
    intrinio.save(symbols, "less_than_200m.pickle")