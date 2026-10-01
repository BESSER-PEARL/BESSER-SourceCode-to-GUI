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
Image = Class(name="Image")
Button = Class(name="Button")
Section = Class(name="Section")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# Image class attributes and methods
Image_src: Property = Property(name="src", type=StringType)
Image.attributes={Image_src}

# Button class attributes and methods

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section_content: Property = Property(name="content", type=StringType)
Section.attributes={Section_title, Section_content}

# Footer class attributes and methods
Footer_socialMediaLinks: Property = Property(name="socialMediaLinks", type=StringType)
Footer_newsletterEmail: Property = Property(name="newsletterEmail", type=StringType)
Footer.attributes={Footer_newsletterEmail, Footer_socialMediaLinks}

# Relationships
containsImage: BinaryAssociation = BinaryAssociation(
    name="containsImage",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Image", type=Image, multiplicity=Multiplicity(1, 1))
    }
)
containsSection: BinaryAssociation = BinaryAssociation(
    name="containsSection",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(2, 2))
    }
)
containsFooter: BinaryAssociation = BinaryAssociation(
    name="containsFooter",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
hasButton: BinaryAssociation = BinaryAssociation(
    name="hasButton",
    ends={
        Property(name="Image", type=Image, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Button", type=Button, multiplicity=Multiplicity(1, 1))
    }
)
includesButton: BinaryAssociation = BinaryAssociation(
    name="includesButton",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Button", type=Button, multiplicity=Multiplicity(2, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Image, Button, Section, Footer},
    associations={containsImage, containsSection, containsFooter, hasButton, includesButton},
    generalizations={}
)
