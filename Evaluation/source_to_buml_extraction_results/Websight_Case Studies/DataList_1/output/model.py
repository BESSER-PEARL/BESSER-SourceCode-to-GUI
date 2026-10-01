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
BankingInstitution = Class(name="BankingInstitution")
Header = Class(name="Header")
Main = Class(name="Main")
Footer = Class(name="Footer")
Service = Class(name="Service")

# BankingInstitution class attributes and methods

# Header class attributes and methods

# Main class attributes and methods

# Footer class attributes and methods

# Service class attributes and methods
Service_serviceName: Property = Property(name="serviceName", type=StringType)
Service_fee: Property = Property(name="fee", type=FloatType)
Service.attributes={Service_fee, Service_serviceName}

# Relationships
containsHeader: BinaryAssociation = BinaryAssociation(
    name="containsHeader",
    ends={
        Property(name="BankingInstitution", type=BankingInstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
containsMain: BinaryAssociation = BinaryAssociation(
    name="containsMain",
    ends={
        Property(name="BankingInstitution", type=BankingInstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
containsFooter: BinaryAssociation = BinaryAssociation(
    name="containsFooter",
    ends={
        Property(name="BankingInstitution", type=BankingInstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
includesService: BinaryAssociation = BinaryAssociation(
    name="includesService",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Service", type=Service, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={BankingInstitution, Header, Main, Footer, Service},
    associations={containsHeader, containsMain, containsFooter, includesService},
    generalizations={}
)
