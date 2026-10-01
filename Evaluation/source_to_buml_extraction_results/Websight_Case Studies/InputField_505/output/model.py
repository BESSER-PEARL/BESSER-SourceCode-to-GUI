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
Navigation = Class(name="Navigation")
Main = Class(name="Main")
SearchBar = Class(name="SearchBar")
Property_ = Class(name="Property")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# Header class attributes and methods

# Navigation class attributes and methods

# Main class attributes and methods

# SearchBar class attributes and methods

# Property class attributes and methods
Property__title: Property = Property(name="title", type=StringType)
Property__description: Property = Property(name="description", type=StringType)
Property_.attributes={Property__description, Property__title}

# Footer class attributes and methods

# Relationships
containsSearchBar: BinaryAssociation = BinaryAssociation(
    name="containsSearchBar",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
containsProperty: BinaryAssociation = BinaryAssociation(
    name="containsProperty",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Property", type=Property_, multiplicity=Multiplicity(3, 3))
    }
)
containsHeader: BinaryAssociation = BinaryAssociation(
    name="containsHeader",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
containsMain: BinaryAssociation = BinaryAssociation(
    name="containsMain",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
containsFooter: BinaryAssociation = BinaryAssociation(
    name="containsFooter",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
containsNavigation: BinaryAssociation = BinaryAssociation(
    name="containsNavigation",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, Main, SearchBar, Property_, Footer},
    associations={containsSearchBar, containsProperty, containsHeader, containsMain, containsFooter, containsNavigation},
    generalizations={}
)
