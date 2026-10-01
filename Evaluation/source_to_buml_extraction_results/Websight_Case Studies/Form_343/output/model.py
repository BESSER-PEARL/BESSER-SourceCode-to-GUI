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
TravelAgencyPage = Class(name="TravelAgencyPage")
Header = Class(name="Header")
Navigation = Class(name="Navigation")
SearchForm = Class(name="SearchForm")
MainContent = Class(name="MainContent")
WelcomeSection = Class(name="WelcomeSection")
Footer = Class(name="Footer")

# TravelAgencyPage class attributes and methods

# Header class attributes and methods

# Navigation class attributes and methods

# SearchForm class attributes and methods
SearchForm_searchQuery: Property = Property(name="searchQuery", type=StringType)
SearchForm.attributes={SearchForm_searchQuery}

# MainContent class attributes and methods

# WelcomeSection class attributes and methods

# Footer class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="WelcomeSection", type=WelcomeSection, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SearchForm", type=SearchForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={TravelAgencyPage, Header, Navigation, SearchForm, MainContent, WelcomeSection, Footer},
    associations={association1, association2, association6, association3, association4, association5},
    generalizations={}
)
