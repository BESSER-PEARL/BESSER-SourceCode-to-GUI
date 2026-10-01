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
Testimonials = Class(name="Testimonials")
WebPage = Class(name="WebPage")
Header = Class(name="Header")
Navigation = Class(name="Navigation")
Main = Class(name="Main")
Section = Class(name="Section")
Footer = Class(name="Footer")
Destinations = Class(name="Destinations")
Packages = Class(name="Packages")

# Testimonials class attributes and methods

# WebPage class attributes and methods

# Header class attributes and methods

# Navigation class attributes and methods

# Main class attributes and methods

# Section class attributes and methods
Section_id: Property = Property(name="id", type=StringType)
Section.attributes={Section_id}

# Footer class attributes and methods

# Destinations class attributes and methods

# Packages class attributes and methods

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
navigation: BinaryAssociation = BinaryAssociation(
    name="navigation",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
packages: BinaryAssociation = BinaryAssociation(
    name="packages",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Packages", type=Packages, multiplicity=Multiplicity(1, 1))
    }
)
sections: BinaryAssociation = BinaryAssociation(
    name="sections",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(3, 3))
    }
)
destinations: BinaryAssociation = BinaryAssociation(
    name="destinations",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Destinations", type=Destinations, multiplicity=Multiplicity(1, 1))
    }
)
testimonials: BinaryAssociation = BinaryAssociation(
    name="testimonials",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Testimonials", type=Testimonials, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Testimonials, WebPage, Header, Navigation, Main, Section, Footer, Destinations, Packages},
    associations={header, navigation, main, footer, packages, sections, destinations, testimonials},
    generalizations={}
)
