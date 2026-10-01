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
WebPage = Class(name="WebPage")
Header = Class(name="Header")
Logo = Class(name="Logo")
Navigation = Class(name="Navigation")
SearchBar = Class(name="SearchBar")
MainContent = Class(name="MainContent")
TravelPackage = Class(name="TravelPackage")

# WebPage class attributes and methods

# Header class attributes and methods

# Logo class attributes and methods

# Navigation class attributes and methods

# SearchBar class attributes and methods

# MainContent class attributes and methods

# TravelPackage class attributes and methods
TravelPackage_title: Property = Property(name="title", type=StringType)
TravelPackage_description: Property = Property(name="description", type=StringType)
TravelPackage.attributes={TravelPackage_description, TravelPackage_title}

# Relationships
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1)),
        Property(name="TravelPackage", type=TravelPackage, multiplicity=Multiplicity(0, 9999))
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo", type=Logo, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Logo, Navigation, SearchBar, MainContent, TravelPackage},
    associations={association4, association5, association6, association1, association2, association3},
    generalizations={}
)
