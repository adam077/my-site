import json
import logging
import datetime
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


class Query:
    def __init__(self, summary, method, url, params, headers=None, body=None, timeout=300):
        self.summary = summary
        self.method = method
        self.url = url
        self.params = params
        self.headers = headers
        self.body = body
        self.timeout = timeout

    def query(self):
        start = datetime.datetime.now()
        try:
            req = requests.request(self.method, self.url, params=self.params, headers=self.headers, json=self.body,
                                   timeout=self.timeout)
            if req.status_code == 200:
                end = datetime.datetime.now()
                result = json.dumps(req.json(), ensure_ascii=False)
                info = "{} succeed using time {}, {} \n{}". \
                    format(self.summary, (end - start).total_seconds(), req.elapsed.total_seconds(), result)
                logger.debug(info)
                return req.json()
            else:
                # err = "{} query error : {} {}".format(summary, req.status_code, req.content)
                err = "{} error after query: {} {}". \
                    format(self.summary, req.status_code, json.dumps(req.json(), ensure_ascii=False))
                logger.error(err)
                raise Exception(err)

        except Exception as e:
            err = "{} err when query: {}".format(self.summary, e)
            logger.error(err)
            raise Exception(err)
