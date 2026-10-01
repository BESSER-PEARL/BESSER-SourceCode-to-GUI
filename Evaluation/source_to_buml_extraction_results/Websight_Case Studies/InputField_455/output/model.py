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
SearchBar = Class(name="SearchBar")
Image = Class(name="Image")
Restaurant = Class(name="Restaurant")
DeliveryArea = Class(name="DeliveryArea")

# WebPage class attributes and methods
WebPage_title: Property = Property(name="title", type=StringType)
WebPage_description: Property = Property(name="description", type=StringType)
WebPage.attributes={WebPage_description, WebPage_title}

# SearchBar class attributes and methods
SearchBar_placeholder: Property = Property(name="placeholder", type=StringType)
SearchBar.attributes={SearchBar_placeholder}

# Image class attributes and methods
Image_src: Property = Property(name="src", type=StringType)
Image_alt: Property = Property(name="alt", type=StringType)
Image.attributes={Image_alt, Image_src}

# Restaurant class attributes and methods
Restaurant_name: Property = Property(name="name", type=StringType)
Restaurant.attributes={Restaurant_name}

# DeliveryArea class attributes and methods
DeliveryArea_name: Property = Property(name="name", type=StringType)
DeliveryArea.attributes={DeliveryArea_name}

# Relationships
deliveryAreas: BinaryAssociation = BinaryAssociation(
    name="deliveryAreas",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="DeliveryArea", type=DeliveryArea, multiplicity=Multiplicity(0, 9999))
    }
)
searchBar: BinaryAssociation = BinaryAssociation(
    name="searchBar",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
images: BinaryAssociation = BinaryAssociation(
    name="images",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Image", type=Image, multiplicity=Multiplicity(0, 9999))
    }
)
restaurants: BinaryAssociation = BinaryAssociation(
    name="restaurants",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Restaurant", type=Restaurant, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, SearchBar, Image, Restaurant, DeliveryArea},
    associations={deliveryAreas, searchBar, images, restaurants},
    generalizations={}
)
