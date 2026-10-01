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
HealthAndWellnessPage = Class(name="HealthAndWellnessPage")
Header = Class(name="Header")
OurServicesSection = Class(name="OurServicesSection")
ContactUsSection = Class(name="ContactUsSection")
ContactForm = Class(name="ContactForm")

# HealthAndWellnessPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header_description: Property = Property(name="description", type=StringType)
Header.attributes={Header_description, Header_title}

# OurServicesSection class attributes and methods
OurServicesSection_title: Property = Property(name="title", type=StringType)
OurServicesSection_description: Property = Property(name="description", type=StringType)
OurServicesSection.attributes={OurServicesSection_title, OurServicesSection_description}

# ContactUsSection class attributes and methods
ContactUsSection_title: Property = Property(name="title", type=StringType)
ContactUsSection_description: Property = Property(name="description", type=StringType)
ContactUsSection.attributes={ContactUsSection_title, ContactUsSection_description}

# ContactForm class attributes and methods
ContactForm_name: Property = Property(name="name", type=StringType)
ContactForm_email: Property = Property(name="email", type=StringType)
ContactForm_message: Property = Property(name="message", type=StringType)
ContactForm.attributes={ContactForm_message, ContactForm_email, ContactForm_name}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="HealthAndWellnessPage", type=HealthAndWellnessPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="HealthAndWellnessPage", type=HealthAndWellnessPage, multiplicity=Multiplicity(1, 1)),
        Property(name="OurServicesSection", type=OurServicesSection, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="HealthAndWellnessPage", type=HealthAndWellnessPage, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactUsSection", type=ContactUsSection, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="ContactUsSection", type=ContactUsSection, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactForm", type=ContactForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={HealthAndWellnessPage, Header, OurServicesSection, ContactUsSection, ContactForm},
    associations={association1, association2, association3, association4},
    generalizations={}
)
