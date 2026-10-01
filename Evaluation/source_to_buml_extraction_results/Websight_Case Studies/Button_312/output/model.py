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

# WebPage class attributes and methods
WebPage_subtitle: Property = Property(name="subtitle", type=StringType)
WebPage_description: Property = Property(name="description", type=StringType)
WebPage_title: Property = Property(name="title", type=StringType)
WebPage.attributes={WebPage_title, WebPage_description, WebPage_subtitle}

# Image class attributes and methods
Image_src: Property = Property(name="src", type=StringType)
Image_alt: Property = Property(name="alt", type=StringType)
Image.attributes={Image_src, Image_alt}

# Button class attributes and methods
Button_label: Property = Property(name="label", type=StringType)
Button.attributes={Button_label}

# Relationships
containsImage: BinaryAssociation = BinaryAssociation(
    name="containsImage",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Image", type=Image, multiplicity=Multiplicity(1, 1))
    }
)
containsButton: BinaryAssociation = BinaryAssociation(
    name="containsButton",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Button", type=Button, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Image, Button},
    associations={containsImage, containsButton},
    generalizations={}
)
