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
ImageGallery = Class(name="ImageGallery")
Image = Class(name="Image")

# ImageGallery class attributes and methods
ImageGallery_q: Property = Property(name="q", type=StringType)
ImageGallery_image_type: Property = Property(name="image_type", type=StringType)
ImageGallery.attributes={ImageGallery_image_type, ImageGallery_q}

# Image class attributes and methods
Image_id: Property = Property(name="id", type=IntegerType)
Image_largeImageURL: Property = Property(name="largeImageURL", type=StringType)
Image_tags: Property = Property(name="tags", type=StringType)
Image.attributes={Image_tags, Image_largeImageURL, Image_id}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="ImageGallery", type=ImageGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="Image", type=Image, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ImageGallery, Image},
    associations={contains},
    generalizations={}
)
