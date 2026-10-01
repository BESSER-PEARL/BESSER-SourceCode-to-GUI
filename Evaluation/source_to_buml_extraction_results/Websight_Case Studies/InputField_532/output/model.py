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

# WebPage class attributes and methods
WebPage_logo: Property = Property(name="logo", type=StringType)
WebPage_relatedProducts: Property = Property(name="relatedProducts", type=StringType)
WebPage_footerText: Property = Property(name="footerText", type=StringType)
WebPage_navLinks: Property = Property(name="navLinks", type=StringType)
WebPage_cartLink: Property = Property(name="cartLink", type=StringType)
WebPage_searchInput: Property = Property(name="searchInput", type=StringType)
WebPage_categories: Property = Property(name="categories", type=StringType)
WebPage_products: Property = Property(name="products", type=StringType)
WebPage.attributes={WebPage_footerText, WebPage_categories, WebPage_searchInput, WebPage_relatedProducts, WebPage_navLinks, WebPage_cartLink, WebPage_logo, WebPage_products}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
