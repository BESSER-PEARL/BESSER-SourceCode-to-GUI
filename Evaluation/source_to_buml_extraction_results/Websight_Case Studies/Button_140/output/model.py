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
RealEstateSite = Class(name="RealEstateSite")
Navigation = Class(name="Navigation")
Section = Class(name="Section")
Image = Class(name="Image")

# RealEstateSite class attributes and methods

# Navigation class attributes and methods

# Section class attributes and methods

# Image class attributes and methods

# Relationships
nav_1: BinaryAssociation = BinaryAssociation(
    name="nav_1",
    ends={
        Property(name="RealEstateSite", type=RealEstateSite, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 9999))
    }
)
sec_1: BinaryAssociation = BinaryAssociation(
    name="sec_1",
    ends={
        Property(name="RealEstateSite", type=RealEstateSite, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(2, 2))
    }
)
img_1: BinaryAssociation = BinaryAssociation(
    name="img_1",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Image", type=Image, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RealEstateSite, Navigation, Section, Image},
    associations={nav_1, sec_1, img_1},
    generalizations={}
)
