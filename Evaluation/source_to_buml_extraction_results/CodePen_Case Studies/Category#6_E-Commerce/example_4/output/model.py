####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
ECommerceCustomerEnquiryForm = Class(name="ECommerceCustomerEnquiryForm")

# ECommerceCustomerEnquiryForm class attributes and methods
ECommerceCustomerEnquiryForm_firstName: Property = Property(name="firstName", type=StringType)
ECommerceCustomerEnquiryForm_lastName: Property = Property(name="lastName", type=StringType)
ECommerceCustomerEnquiryForm_storeName: Property = Property(name="storeName", type=StringType)
ECommerceCustomerEnquiryForm_storeNumber: Property = Property(name="storeNumber", type=StringType)
ECommerceCustomerEnquiryForm_memberNumber: Property = Property(name="memberNumber", type=StringType)
ECommerceCustomerEnquiryForm_email: Property = Property(name="email", type=StringType)
ECommerceCustomerEnquiryForm_confirmEmail: Property = Property(name="confirmEmail", type=StringType)
ECommerceCustomerEnquiryForm_antiSpam: Property = Property(name="antiSpam", type=StringType)
ECommerceCustomerEnquiryForm.attributes={ECommerceCustomerEnquiryForm_confirmEmail, ECommerceCustomerEnquiryForm_antiSpam, ECommerceCustomerEnquiryForm_firstName, ECommerceCustomerEnquiryForm_lastName, ECommerceCustomerEnquiryForm_storeNumber, ECommerceCustomerEnquiryForm_storeName, ECommerceCustomerEnquiryForm_memberNumber, ECommerceCustomerEnquiryForm_email}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ECommerceCustomerEnquiryForm},
    associations={},
    generalizations={}
)
