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
Section = Class(name="Section")
Image = Class(name="Image")
Paragraph = Class(name="Paragraph")

# WebPage class attributes and methods

# Header class attributes and methods

# Main class attributes and methods

# Section class attributes and methods

# Image class attributes and methods
Image_src: Property = Property(name="src", type=StringType)
Image_alt: Property = Property(name="alt", type=StringType)
Image.attributes={Image_alt, Image_src}

# Paragraph class attributes and methods
Paragraph_text: Property = Property(name="text", type=StringType)
Paragraph.attributes={Paragraph_text}

# Relationships
headerLink: BinaryAssociation = BinaryAssociation(
    name="headerLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
mainContent: BinaryAssociation = BinaryAssociation(
    name="mainContent",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
sectionContent: BinaryAssociation = BinaryAssociation(
    name="sectionContent",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(2, 2))
    }
)
sectionImage: BinaryAssociation = BinaryAssociation(
    name="sectionImage",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Image", type=Image, multiplicity=Multiplicity(1, 1))
    }
)
sectionText: BinaryAssociation = BinaryAssociation(
    name="sectionText",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Paragraph", type=Paragraph, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Section, Image, Paragraph},
    associations={headerLink, mainContent, sectionContent, sectionImage, sectionText},
    generalizations={}
)
