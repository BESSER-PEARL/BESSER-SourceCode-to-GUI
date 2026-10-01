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
Aside = Class(name="Aside")
Footer = Class(name="Footer")
Form = Class(name="Form")

# WebPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header_subtitle: Property = Property(name="subtitle", type=StringType)
Header.attributes={Header_title, Header_subtitle}

# Main class attributes and methods

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section_description: Property = Property(name="description", type=StringType)
Section.attributes={Section_title, Section_description}

# Aside class attributes and methods
Aside_title: Property = Property(name="title", type=StringType)
Aside_description: Property = Property(name="description", type=StringType)
Aside.attributes={Aside_title, Aside_description}

# Footer class attributes and methods
Footer_title: Property = Property(name="title", type=StringType)
Footer.attributes={Footer_title}

# Form class attributes and methods
Form_name: Property = Property(name="name", type=StringType)
Form_email: Property = Property(name="email", type=StringType)
Form_message: Property = Property(name="message", type=StringType)
Form.attributes={Form_name, Form_message, Form_email}

# Relationships
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Aside", type=Aside, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Section, Aside, Footer, Form},
    associations={association3, association1, association2, association4, association5, association6},
    generalizations={}
)
