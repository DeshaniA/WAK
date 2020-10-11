 #***(1)Returns all customers from customer table
from accounts.models import Customer, Contract, Service

customers = Customer.objects.all()

#(2)Returns first customer in table
firstCustomer = Customer.objects.first()

#(3)Returns last customer in table
lastCustomer = Customer.objects.last()

#(4)Returns single customer by name
customerByName = Customer.objects.get(name='peter fernando')

#***(5)Returns single customer by name
customerById = Customer.objects.get(id=1)

#***(6)Returns all contracts related to customer (firstCustomer variable set above)
firstCustomer.contract_set.all()

#(7)***Returns contracts customer name: (Query parent model values)
contract = Contract.objects.first()
parentName = contract.customer.name

#(8)***Returns services from services table with value of "Industrial" in category attribute
services = Service.objects.filter(category="Industrial")

#(9)***Contract/Sort Objects by id
leastToGreatest = Service.objects.all().order_by('id')
greatestToLeast = Service.objects.all().order_by('-id')


#(10) Returns all services with tag of "Electrical": (Query Many to Many Fields)
servicesFiltered = Service.objects.filter(tags__name="Electrical")