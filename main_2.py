from zeep import Client

wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = """
ujdfsghrtghrthgiortgh;rth;dhbk;sdjfgh;sdfhgrtghuo;tgh;hgsd;hsdjfghsdkfjgh

"""

client = Client(wsdl=wsdl)


def test_step2():
    assert client.service.VerifySignature('CMS', sign)['Result']
