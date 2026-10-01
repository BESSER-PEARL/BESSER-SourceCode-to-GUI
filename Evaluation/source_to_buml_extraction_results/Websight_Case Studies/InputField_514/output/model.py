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
Image = Class(name="Image")
Navigation = Class(name="Navigation")
SearchBar = Class(name="SearchBar")
FeaturedListings = Class(name="FeaturedListings")
BlogSection = Class(name="BlogSection")

# RealEstatePage class attributes and methods

# Image class attributes and methods
Image_src: Property = Property(name="src", type=StringType)
Image_alt: Property = Property(name="alt", type=StringType)
Image.attributes={Image_alt, Image_src}

# Navigation class attributes and methods

# SearchBar class attributes and methods
SearchBar_placeholder: Property = Property(name="placeholder", type=StringType)
SearchBar.attributes={SearchBar_placeholder}

# FeaturedListings class attributes and methods

# BlogSection class attributes and methods

# Relationships
img: BinaryAssociation = BinaryAssociation(
    name="img",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="Image", type=Image, multiplicity=Multiplicity(1, 1))
    }
)
nav: BinaryAssociation = BinaryAssociation(
    name="nav",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
search: BinaryAssociation = BinaryAssociation(
    name="search",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
listings: BinaryAssociation = BinaryAssociation(
    name="listings",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="FeaturedListings", type=FeaturedListings, multiplicity=Multiplicity(1, 1))
    }
)
blog: BinaryAssociation = BinaryAssociation(
    name="blog",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="BlogSection", type=BlogSection, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RealEstatePage, Image, Navigation, SearchBar, FeaturedListings, BlogSection},
    associations={img, nav, search, listings, blog},
    generalizations={}
)
