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
LawFirmPage = Class(name="LawFirmPage")
Header = Class(name="Header")
Navigation = Class(name="Navigation")
Aside = Class(name="Aside")
Main = Class(name="Main")

# LawFirmPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header.attributes={Header_title}

# Navigation class attributes and methods
Navigation_links: Property = Property(name="links", type=StringType)
Navigation.attributes={Navigation_links}

# Aside class attributes and methods
Aside_contactInformation: Property = Property(name="contactInformation", type=StringType)
Aside_services: Property = Property(name="services", type=StringType)
Aside.attributes={Aside_services, Aside_contactInformation}

# Main class attributes and methods
Main_aboutUs: Property = Property(name="aboutUs", type=StringType)
Main.attributes={Main_aboutUs}

# Relationships
navigation: BinaryAssociation = BinaryAssociation(
    name="navigation",
    ends={
        Property(name="LawFirmPage", type=LawFirmPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="LawFirmPage", type=LawFirmPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
aside: BinaryAssociation = BinaryAssociation(
    name="aside",
    ends={
        Property(name="LawFirmPage", type=LawFirmPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Aside", type=Aside, multiplicity=Multiplicity(1, 1))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="LawFirmPage", type=LawFirmPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={LawFirmPage, Header, Navigation, Aside, Main},
    associations={navigation, header, aside, main},
    generalizations={}
)
