from suds.client import Client
calcservice = Client('http://localhost:8000/?wsdl')
print "Adding 10 and 20 from Webservice"
print calcservice.service.add(10,20)
print "Multiplying 10 and 20 from Webservice"
print calcservice.service.multiply(10,20)
print "Dividing 30 and 20 from Webservice"
print calcservice.service.divide(30,20)
