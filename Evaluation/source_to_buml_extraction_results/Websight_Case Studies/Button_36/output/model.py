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
RealEstatePage = Class(name="RealEstatePage")
FeaturedListings = Class(name="FeaturedListings")
Testimonials = Class(name="Testimonials")
AboutUs = Class(name="AboutUs")
ContactUs = Class(name="ContactUs")

# RealEstatePage class attributes and methods
RealEstatePage_headerImage: Property = Property(name="headerImage", type=StringType)
RealEstatePage_title: Property = Property(name="title", type=StringType)
RealEstatePage_description: Property = Property(name="description", type=StringType)
RealEstatePage.attributes={RealEstatePage_title, RealEstatePage_headerImage, RealEstatePage_description}

# FeaturedListings class attributes and methods
FeaturedListings_listingDescription: Property = Property(name="listingDescription", type=StringType)
FeaturedListings_listingTitle: Property = Property(name="listingTitle", type=StringType)
FeaturedListings.attributes={FeaturedListings_listingTitle, FeaturedListings_listingDescription}

# Testimonials class attributes and methods
Testimonials_testimonialTitle: Property = Property(name="testimonialTitle", type=StringType)
Testimonials_testimonialDescription: Property = Property(name="testimonialDescription", type=StringType)
Testimonials.attributes={Testimonials_testimonialTitle, Testimonials_testimonialDescription}

# AboutUs class attributes and methods
AboutUs_aboutTitle: Property = Property(name="aboutTitle", type=StringType)
AboutUs_aboutDescription: Property = Property(name="aboutDescription", type=StringType)
AboutUs.attributes={AboutUs_aboutTitle, AboutUs_aboutDescription}

# ContactUs class attributes and methods
ContactUs_contactTitle: Property = Property(name="contactTitle", type=StringType)
ContactUs_contactDescription: Property = Property(name="contactDescription", type=StringType)
ContactUs.attributes={ContactUs_contactDescription, ContactUs_contactTitle}

# Relationships
FL1: BinaryAssociation = BinaryAssociation(
    name="FL1",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="FeaturedListings", type=FeaturedListings, multiplicity=Multiplicity(1, 1))
    }
)
T1: BinaryAssociation = BinaryAssociation(
    name="T1",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="Testimonials", type=Testimonials, multiplicity=Multiplicity(1, 1))
    }
)
AU1: BinaryAssociation = BinaryAssociation(
    name="AU1",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="AboutUs", type=AboutUs, multiplicity=Multiplicity(1, 1))
    }
)
CU1: BinaryAssociation = BinaryAssociation(
    name="CU1",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactUs", type=ContactUs, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RealEstatePage, FeaturedListings, Testimonials, AboutUs, ContactUs},
    associations={FL1, T1, AU1, CU1},
    generalizations={}
)
