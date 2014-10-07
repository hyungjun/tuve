import ujson
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.web import RequestHandler
from tuve.core.spec.tokyo_metro.api import TokyoMetroAPI
from tuve.core.spec.tokyo_metro.namespace import TokyoMetro as TM

class APIHandler(RequestHandler):

    def initialize(self, opt):
        self.opt = opt
        self.api = TokyoMetroAPI(opt.API_KEY)

    @gen.coroutine
    def get(self, resource_query_params):
        """
        Simply ignore `resource_query_params` to get
        the general idea on handling an asynchronous HTTP request.
        """
        query = self.api.datapoints.TRAIN_INFORMATION(
            # TM.Ginza if it needs to be specified...
        )
        response = yield AsyncHTTPClient().fetch(query.str)

        # temporarily hard-coded lines, diced data for ember.js
        models = ujson.loads(response.body)
        slims = [dict({
            k.split(':')[1]: v
            for k, v in model.items()
            if not k.startswith('@')
        }, id=index) for index, model in enumerate(models)]
        self.finish(ujson.dumps({'trainInformation':slims}))
