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
UniversityPage = Class(name="UniversityPage")
Header = Class(name="Header")
Nav = Class(name="Nav")
Main = Class(name="Main")
Section = Class(name="Section")

# UniversityPage class attributes and methods
UniversityPage_bgColor: Property = Property(name="bgColor", type=StringType)
UniversityPage.attributes={UniversityPage_bgColor}

# Header class attributes and methods
Header_logo: Property = Property(name="logo", type=StringType)
Header_bgColor: Property = Property(name="bgColor", type=StringType)
Header_textColor: Property = Property(name="textColor", type=StringType)
Header.attributes={Header_bgColor, Header_logo, Header_textColor}

# Nav class attributes and methods
Nav_links: Property = Property(name="links", type=StringType)
Nav_bgColor: Property = Property(name="bgColor", type=StringType)
Nav_textColor: Property = Property(name="textColor", type=StringType)
Nav.attributes={Nav_bgColor, Nav_textColor, Nav_links}

# Main class attributes and methods
Main_sections: Property = Property(name="sections", type=StringType)
Main.attributes={Main_sections}

# Section class attributes and methods
Section_id: Property = Property(name="id", type=StringType)
Section_title: Property = Property(name="title", type=StringType)
Section_content: Property = Property(name="content", type=StringType)
Section_bgColor: Property = Property(name="bgColor", type=StringType)
Section.attributes={Section_title, Section_id, Section_bgColor, Section_content}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="UniversityPage", type=UniversityPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
navigation: BinaryAssociation = BinaryAssociation(
    name="navigation",
    ends={
        Property(name="UniversityPage", type=UniversityPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Nav", type=Nav, multiplicity=Multiplicity(1, 1))
    }
)
mainContent: BinaryAssociation = BinaryAssociation(
    name="mainContent",
    ends={
        Property(name="UniversityPage", type=UniversityPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
section: BinaryAssociation = BinaryAssociation(
    name="section",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={UniversityPage, Header, Nav, Main, Section},
    associations={header, navigation, mainContent, section},
    generalizations={}
)
