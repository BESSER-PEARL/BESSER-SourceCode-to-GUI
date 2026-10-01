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
FinancialServicesPage = Class(name="FinancialServicesPage")
Menu = Class(name="Menu")
Contact = Class(name="Contact")

# FinancialServicesPage class attributes and methods

# Menu class attributes and methods

# Contact class attributes and methods
Contact_companyName: Property = Property(name="companyName", type=StringType)
Contact_address: Property = Property(name="address", type=StringType)
Contact_phone: Property = Property(name="phone", type=StringType)
Contact_email: Property = Property(name="email", type=StringType)
Contact.attributes={Contact_phone, Contact_address, Contact_companyName, Contact_email}

# Relationships
fs_menu: BinaryAssociation = BinaryAssociation(
    name="fs_menu",
    ends={
        Property(name="FinancialServicesPage", type=FinancialServicesPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
fs_contact: BinaryAssociation = BinaryAssociation(
    name="fs_contact",
    ends={
        Property(name="FinancialServicesPage", type=FinancialServicesPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Contact", type=Contact, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={FinancialServicesPage, Menu, Contact},
    associations={fs_menu, fs_contact},
    generalizations={}
)
