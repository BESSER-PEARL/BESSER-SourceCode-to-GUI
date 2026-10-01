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
SearchForm = Class(name="SearchForm")

# WebPage class attributes and methods
WebPage_logo: Property = Property(name="logo", type=StringType)
WebPage_navLinks: Property = Property(name="navLinks", type=StringType)
WebPage_title: Property = Property(name="title", type=StringType)
WebPage_description: Property = Property(name="description", type=StringType)
WebPage_searchPlaceholder: Property = Property(name="searchPlaceholder", type=StringType)
WebPage.attributes={WebPage_description, WebPage_navLinks, WebPage_logo, WebPage_title, WebPage_searchPlaceholder}

# SearchForm class attributes and methods
SearchForm_searchInput: Property = Property(name="searchInput", type=StringType)
SearchForm.attributes={SearchForm_searchInput}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchForm", type=SearchForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, SearchForm},
    associations={contains},
    generalizations={}
)
