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
Header = Class(name="Header")
Aside = Class(name="Aside")
Main = Class(name="Main")
Footer = Class(name="Footer")

# Header class attributes and methods
Header_classroomImage: Property = Property(name="classroomImage", type=StringType)
Header_logoImage: Property = Property(name="logoImage", type=StringType)
Header.attributes={Header_logoImage, Header_classroomImage}

# Aside class attributes and methods
Aside_courses: Property = Property(name="courses", type=StringType)
Aside.attributes={Aside_courses}

# Main class attributes and methods
Main_title: Property = Property(name="title", type=StringType)
Main_description: Property = Property(name="description", type=StringType)
Main_staffInfo: Property = Property(name="staffInfo", type=StringType)
Main.attributes={Main_title, Main_staffInfo, Main_description}

# Footer class attributes and methods
Footer_contactPhone: Property = Property(name="contactPhone", type=StringType)
Footer_contactEmail: Property = Property(name="contactEmail", type=StringType)
Footer_testimonials: Property = Property(name="testimonials", type=StringType)
Footer_newsletterEmail: Property = Property(name="newsletterEmail", type=StringType)
Footer.attributes={Footer_contactPhone, Footer_newsletterEmail, Footer_contactEmail, Footer_testimonials}

# Relationships
aside: BinaryAssociation = BinaryAssociation(
    name="aside",
    ends={
        Property(name="Aside", type=Aside, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Aside", type=Aside, multiplicity=Multiplicity(1, 1))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Header, Aside, Main, Footer},
    associations={aside, header, main},
    generalizations={}
)
