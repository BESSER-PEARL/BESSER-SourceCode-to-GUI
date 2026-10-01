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
Header = Class(name="Header")
MainContent = Class(name="MainContent")

# FinancialServicesPage class attributes and methods

# Header class attributes and methods

# MainContent class attributes and methods

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="FinancialServicesPage", type=FinancialServicesPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
mainContent: BinaryAssociation = BinaryAssociation(
    name="mainContent",
    ends={
        Property(name="FinancialServicesPage", type=FinancialServicesPage, multiplicity=Multiplicity(1, 1)),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={FinancialServicesPage, Header, MainContent},
    associations={header, mainContent},
    generalizations={}
)
