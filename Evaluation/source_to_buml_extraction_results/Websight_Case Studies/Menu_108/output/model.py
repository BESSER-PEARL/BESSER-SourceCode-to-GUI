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
Main = Class(name="Main")
Footer = Class(name="Footer")

# WebPage class attributes and methods
WebPage_header: Property = Property(name="header", type=StringType)
WebPage_main: Property = Property(name="main", type=StringType)
WebPage_footer: Property = Property(name="footer", type=StringType)
WebPage.attributes={WebPage_header, WebPage_footer, WebPage_main}

# Header class attributes and methods
Header_image: Property = Property(name="image", type=StringType)
Header_nav_links: Property = Property(name="nav_links", type=StringType)
Header.attributes={Header_image, Header_nav_links}

# Main class attributes and methods
Main_section_ids: Property = Property(name="section_ids", type=StringType)
Main_section_titles: Property = Property(name="section_titles", type=StringType)
Main_section_descriptions: Property = Property(name="section_descriptions", type=StringType)
Main.attributes={Main_section_descriptions, Main_section_ids, Main_section_titles}

# Footer class attributes and methods
Footer_text: Property = Property(name="text", type=StringType)
Footer.attributes={Footer_text}

# Relationships
contains_header: BinaryAssociation = BinaryAssociation(
    name="contains_header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
contains_main: BinaryAssociation = BinaryAssociation(
    name="contains_main",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
contains_footer: BinaryAssociation = BinaryAssociation(
    name="contains_footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Footer},
    associations={contains_header, contains_main, contains_footer},
    generalizations={}
)
