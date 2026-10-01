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
Testimonial = Class(name="Testimonial")
TeamMember = Class(name="TeamMember")
ContactForm = Class(name="ContactForm")
Footer = Class(name="Footer")
WebPage = Class(name="WebPage")
Navigation = Class(name="Navigation")
HeroSection = Class(name="HeroSection")
Image = Class(name="Image")
Service = Class(name="Service")

# Testimonial class attributes and methods
Testimonial_content: Property = Property(name="content", type=StringType)
Testimonial.attributes={Testimonial_content}

# TeamMember class attributes and methods
TeamMember_name: Property = Property(name="name", type=StringType)
TeamMember.attributes={TeamMember_name}

# ContactForm class attributes and methods
ContactForm_name: Property = Property(name="name", type=StringType)
ContactForm_email: Property = Property(name="email", type=StringType)
ContactForm_message: Property = Property(name="message", type=StringType)
ContactForm.attributes={ContactForm_message, ContactForm_email, ContactForm_name}

# Footer class attributes and methods

# WebPage class attributes and methods

# Navigation class attributes and methods

# HeroSection class attributes and methods
HeroSection_title: Property = Property(name="title", type=StringType)
HeroSection_description: Property = Property(name="description", type=StringType)
HeroSection.attributes={HeroSection_description, HeroSection_title}

# Image class attributes and methods
Image_src: Property = Property(name="src", type=StringType)
Image.attributes={Image_src}

# Service class attributes and methods
Service_name: Property = Property(name="name", type=StringType)
Service.attributes={Service_name}

# Relationships
nav: BinaryAssociation = BinaryAssociation(
    name="nav",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
hero: BinaryAssociation = BinaryAssociation(
    name="hero",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="HeroSection", type=HeroSection, multiplicity=Multiplicity(1, 1))
    }
)
heroImage: BinaryAssociation = BinaryAssociation(
    name="heroImage",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Image", type=Image, multiplicity=Multiplicity(1, 1))
    }
)
services: BinaryAssociation = BinaryAssociation(
    name="services",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Service", type=Service, multiplicity=Multiplicity(1, 9999))
    }
)
testimonials: BinaryAssociation = BinaryAssociation(
    name="testimonials",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Testimonial", type=Testimonial, multiplicity=Multiplicity(1, 9999))
    }
)
team: BinaryAssociation = BinaryAssociation(
    name="team",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="TeamMember", type=TeamMember, multiplicity=Multiplicity(1, 9999))
    }
)
contact: BinaryAssociation = BinaryAssociation(
    name="contact",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactForm", type=ContactForm, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Testimonial, TeamMember, ContactForm, Footer, WebPage, Navigation, HeroSection, Image, Service},
    associations={nav, hero, heroImage, services, testimonials, team, contact, footer},
    generalizations={}
)
