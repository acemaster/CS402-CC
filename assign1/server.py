from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode,srpc

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class CalculateService(ServiceBase):
    @srpc(Integer, Integer, _returns=Iterable(Unicode))
    def add(num1, num2):
        final_num = num1 + num2
        yield u'Sum is, %d' % final_num

    @srpc(Integer, Integer, _returns=Iterable(Unicode))
    def multiply(num1, num2):
        final_num = num1 * num2
        yield u'Product is, %d' % final_num

    @srpc(Integer, Integer, _returns=Iterable(Unicode))
    def divide(num1, num2):
        final_num = num1/num2
        yield u'Quotient is, %d' % final_num





application = Application([CalculateService], 'CS402.CC.assign1.calc',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    # logging.basicConfig(level=logging.DEBUG)
    # logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()