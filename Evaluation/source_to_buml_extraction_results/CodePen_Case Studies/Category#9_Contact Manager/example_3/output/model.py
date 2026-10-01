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
ContactManager = Class(name="ContactManager")
Header = Class(name="Header")
Tab = Class(name="Tab")
Main = Class(name="Main")
Form = Class(name="Form")
Contacts = Class(name="Contacts")
Table = Class(name="Table")
Footer = Class(name="Footer")

# ContactManager class attributes and methods

# Header class attributes and methods

# Tab class attributes and methods
Tab_tabForm: Property = Property(name="tabForm", type=StringType)
Tab_tabContacts: Property = Property(name="tabContacts", type=StringType)
Tab.attributes={Tab_tabForm, Tab_tabContacts}

# Main class attributes and methods

# Form class attributes and methods
Form_firstname: Property = Property(name="firstname", type=StringType)
Form_surname: Property = Property(name="surname", type=StringType)
Form_age: Property = Property(name="age", type=IntegerType)
Form_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
Form_email: Property = Property(name="email", type=StringType)
Form_address: Property = Property(name="address", type=StringType)
Form.attributes={Form_surname, Form_address, Form_age, Form_phoneNumber, Form_email, Form_firstname}

# Contacts class attributes and methods

# Table class attributes and methods

# Footer class attributes and methods
Footer_copyrightNotice: Property = Property(name="copyrightNotice", type=StringType)
Footer.attributes={Footer_copyrightNotice}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Tab", type=Tab, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Contacts", type=Contacts, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="Contacts", type=Contacts, multiplicity=Multiplicity(1, 1)),
        Property(name="Table", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ContactManager, Header, Tab, Main, Form, Contacts, Table, Footer},
    associations={association1, association2, association4, association5, association6, association7, association3},
    generalizations={}
)
