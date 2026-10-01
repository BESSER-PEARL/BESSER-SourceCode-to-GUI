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
Header = Class(name="Header")
Main = Class(name="Main")
Footer = Class(name="Footer")
SearchBar = Class(name="SearchBar")
Product = Class(name="Product")
Category = Class(name="Category")
SocialMedia = Class(name="SocialMedia")
Newsletter = Class(name="Newsletter")

# WebPage class attributes and methods

# Header class attributes and methods

# Main class attributes and methods

# Footer class attributes and methods

# SearchBar class attributes and methods
SearchBar_placeholder: Property = Property(name="placeholder", type=StringType)
SearchBar.attributes={SearchBar_placeholder}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product.attributes={Product_name}

# Category class attributes and methods
Category_name: Property = Property(name="name", type=StringType)
Category.attributes={Category_name}

# SocialMedia class attributes and methods
SocialMedia_platform: Property = Property(name="platform", type=StringType)
SocialMedia.attributes={SocialMedia_platform}

# Newsletter class attributes and methods
Newsletter_email: Property = Property(name="email", type=StringType)
Newsletter.attributes={Newsletter_email}

# Relationships
search: BinaryAssociation = BinaryAssociation(
    name="search",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
product: BinaryAssociation = BinaryAssociation(
    name="product",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
category: BinaryAssociation = BinaryAssociation(
    name="category",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Category", type=Category, multiplicity=Multiplicity(1, 1))
    }
)
social: BinaryAssociation = BinaryAssociation(
    name="social",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="SocialMedia", type=SocialMedia, multiplicity=Multiplicity(1, 1))
    }
)
newsletter: BinaryAssociation = BinaryAssociation(
    name="newsletter",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Newsletter", type=Newsletter, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Footer, SearchBar, Product, Category, SocialMedia, Newsletter},
    associations={search, header, main, footer, product, category, social, newsletter},
    generalizations={}
)
