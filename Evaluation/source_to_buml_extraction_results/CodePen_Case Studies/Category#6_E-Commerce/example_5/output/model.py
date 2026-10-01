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
ProjectWrapper = Class(name="ProjectWrapper")
ProjectContainer = Class(name="ProjectContainer")
Left = Class(name="Left")
Product = Class(name="Product")
Right = Class(name="Right")
Overlay = Class(name="Overlay")
ListItem = Class(name="ListItem")

# ProjectWrapper class attributes and methods

# ProjectContainer class attributes and methods

# Left class attributes and methods

# Product class attributes and methods

# Right class attributes and methods
Right_title: Property = Property(name="title", type=StringType)
Right_price: Property = Property(name="price", type=FloatType)
Right_description: Property = Property(name="description", type=StringType)
Right.attributes={Right_title, Right_description, Right_price}

# Overlay class attributes and methods

# ListItem class attributes and methods
ListItem_featureDescription: Property = Property(name="featureDescription", type=StringType)
ListItem.attributes={ListItem_featureDescription}

# Relationships
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Left", type=Left, multiplicity=Multiplicity(1, 1)),
        Property(name="Overlay", type=Overlay, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Right", type=Right, multiplicity=Multiplicity(1, 1)),
        Property(name="ListItem", type=ListItem, multiplicity=Multiplicity(0, 9999))
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="ProjectWrapper", type=ProjectWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="ProjectContainer", type=ProjectContainer, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="ProjectContainer", type=ProjectContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Left", type=Left, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="ProjectContainer", type=ProjectContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Right", type=Right, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Left", type=Left, multiplicity=Multiplicity(1, 1)),
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ProjectWrapper, ProjectContainer, Left, Product, Right, Overlay, ListItem},
    associations={association5, association6, association1, association2, association3, association4},
    generalizations={}
)
