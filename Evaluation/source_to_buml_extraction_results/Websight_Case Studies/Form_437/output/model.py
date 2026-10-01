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
Navigation = Class(name="Navigation")
PropertyImageSlider = Class(name="PropertyImageSlider")
TwoColumnLayout = Class(name="TwoColumnLayout")
ContactForm = Class(name="ContactForm")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# Navigation class attributes and methods

# PropertyImageSlider class attributes and methods

# TwoColumnLayout class attributes and methods

# ContactForm class attributes and methods
ContactForm_name: Property = Property(name="name", type=StringType)
ContactForm_email: Property = Property(name="email", type=StringType)
ContactForm_message: Property = Property(name="message", type=StringType)
ContactForm.attributes={ContactForm_name, ContactForm_message, ContactForm_email}

# Footer class attributes and methods

# Relationships
slider: BinaryAssociation = BinaryAssociation(
    name="slider",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="PropertyImageSlider", type=PropertyImageSlider, multiplicity=Multiplicity(1, 1))
    }
)
layout: BinaryAssociation = BinaryAssociation(
    name="layout",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="TwoColumnLayout", type=TwoColumnLayout, multiplicity=Multiplicity(1, 1))
    }
)
nav: BinaryAssociation = BinaryAssociation(
    name="nav",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
form: BinaryAssociation = BinaryAssociation(
    name="form",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ContactForm", type=ContactForm, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Navigation, PropertyImageSlider, TwoColumnLayout, ContactForm, Footer},
    associations={slider, layout, nav, form, footer},
    generalizations={}
)
