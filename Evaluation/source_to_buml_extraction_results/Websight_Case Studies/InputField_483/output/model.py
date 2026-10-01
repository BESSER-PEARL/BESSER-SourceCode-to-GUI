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
MainContent = Class(name="MainContent")
Footer = Class(name="Footer")

# TravelAgencyPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header_subtitle: Property = Property(name="subtitle", type=StringType)
Header.attributes={Header_title, Header_subtitle}

# Navigation class attributes and methods
Navigation_destinationsLink: Property = Property(name="destinationsLink", type=StringType)
Navigation_travelStylesLink: Property = Property(name="travelStylesLink", type=StringType)
Navigation_toursLink: Property = Property(name="toursLink", type=StringType)
Navigation_dealsLink: Property = Property(name="dealsLink", type=StringType)
Navigation_searchInput: Property = Property(name="searchInput", type=StringType)
Navigation.attributes={Navigation_toursLink, Navigation_travelStylesLink, Navigation_searchInput, Navigation_destinationsLink, Navigation_dealsLink}

# MainContent class attributes and methods

# Footer class attributes and methods

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
navigation: BinaryAssociation = BinaryAssociation(
    name="navigation",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
mainContent: BinaryAssociation = BinaryAssociation(
    name="mainContent",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={TravelAgencyPage, Header, Navigation, MainContent, Footer},
    associations={header, navigation, mainContent, footer},
    generalizations={}
)
