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
Navigation = Class(name="Navigation")

# RealEstatePage class attributes and methods
RealEstatePage_title: Property = Property(name="title", type=StringType)
RealEstatePage_searchPlaceholder: Property = Property(name="searchPlaceholder", type=StringType)
RealEstatePage_welcomeMessage: Property = Property(name="welcomeMessage", type=StringType)
RealEstatePage_description: Property = Property(name="description", type=StringType)
RealEstatePage.attributes={RealEstatePage_searchPlaceholder, RealEstatePage_welcomeMessage, RealEstatePage_description, RealEstatePage_title}

# Navigation class attributes and methods
Navigation_propertiesLink: Property = Property(name="propertiesLink", type=StringType)
Navigation_homeLink: Property = Property(name="homeLink", type=StringType)
Navigation_aboutUsLink: Property = Property(name="aboutUsLink", type=StringType)
Navigation_contactLink: Property = Property(name="contactLink", type=StringType)
Navigation.attributes={Navigation_propertiesLink, Navigation_homeLink, Navigation_contactLink, Navigation_aboutUsLink}

# Relationships
nav: BinaryAssociation = BinaryAssociation(
    name="nav",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RealEstatePage, Navigation},
    associations={nav},
    generalizations={}
)
