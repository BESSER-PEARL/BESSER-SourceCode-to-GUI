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
SoftwareCompanyPage = Class(name="SoftwareCompanyPage")
Header = Class(name="Header")
Main = Class(name="Main")
Section = Class(name="Section")
Footer = Class(name="Footer")

# SoftwareCompanyPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header_description: Property = Property(name="description", type=StringType)
Header.attributes={Header_description, Header_title}

# Main class attributes and methods

# Section class attributes and methods
Section_sectionTitle: Property = Property(name="sectionTitle", type=StringType)
Section_sectionDescription: Property = Property(name="sectionDescription", type=StringType)
Section.attributes={Section_sectionDescription, Section_sectionTitle}

# Footer class attributes and methods
Footer_copyrightInfo: Property = Property(name="copyrightInfo", type=StringType)
Footer.attributes={Footer_copyrightInfo}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="SoftwareCompanyPage", type=SoftwareCompanyPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
mainContent: BinaryAssociation = BinaryAssociation(
    name="mainContent",
    ends={
        Property(name="SoftwareCompanyPage", type=SoftwareCompanyPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="SoftwareCompanyPage", type=SoftwareCompanyPage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mainSection: BinaryAssociation = BinaryAssociation(
    name="mainSection",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SoftwareCompanyPage, Header, Main, Section, Footer},
    associations={header, mainContent, footer, mainSection},
    generalizations={}
)
