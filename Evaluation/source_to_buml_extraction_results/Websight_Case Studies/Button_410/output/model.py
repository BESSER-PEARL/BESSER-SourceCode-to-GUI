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
Navigation = Class(name="Navigation")
Section = Class(name="Section")
Footer = Class(name="Footer")
WebPage = Class(name="WebPage")

# Navigation class attributes and methods
Navigation_homeLink: Property = Property(name="homeLink", type=StringType)
Navigation_aboutLink: Property = Property(name="aboutLink", type=StringType)
Navigation_contactLink: Property = Property(name="contactLink", type=StringType)
Navigation.attributes={Navigation_aboutLink, Navigation_homeLink, Navigation_contactLink}

# Section class attributes and methods
Section_heading: Property = Property(name="heading", type=StringType)
Section_paragraph: Property = Property(name="paragraph", type=StringType)
Section.attributes={Section_heading, Section_paragraph}

# Footer class attributes and methods
Footer_privacyPolicyLink: Property = Property(name="privacyPolicyLink", type=StringType)
Footer_termsOfUseLink: Property = Property(name="termsOfUseLink", type=StringType)
Footer.attributes={Footer_termsOfUseLink, Footer_privacyPolicyLink}

# WebPage class attributes and methods
WebPage_title: Property = Property(name="title", type=StringType)
WebPage_description: Property = Property(name="description", type=StringType)
WebPage_imageUrl: Property = Property(name="imageUrl", type=StringType)
WebPage_footerText: Property = Property(name="footerText", type=StringType)
WebPage.attributes={WebPage_title, WebPage_footerText, WebPage_description, WebPage_imageUrl}

# Relationships
nav: BinaryAssociation = BinaryAssociation(
    name="nav",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
foot: BinaryAssociation = BinaryAssociation(
    name="foot",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
content: BinaryAssociation = BinaryAssociation(
    name="content",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Navigation, Section, Footer, WebPage},
    associations={nav, foot, content},
    generalizations={}
)
