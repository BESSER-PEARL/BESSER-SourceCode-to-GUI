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
Cart = Class(name="Cart")
Wrapper = Class(name="Wrapper")
ProductSection = Class(name="ProductSection")
Circle = Class(name="Circle")
ProdDescription = Class(name="ProdDescription")
Article = Class(name="Article")
Container = Class(name="Container")
Header = Class(name="Header")
MainNav = Class(name="MainNav")
Logo = Class(name="Logo")
Navigation = Class(name="Navigation")
Search = Class(name="Search")

# Cart class attributes and methods

# Wrapper class attributes and methods

# ProductSection class attributes and methods

# Circle class attributes and methods

# ProdDescription class attributes and methods

# Article class attributes and methods
Article_title: Property = Property(name="title", type=StringType)
Article_description: Property = Property(name="description", type=StringType)
Article.attributes={Article_title, Article_description}

# Container class attributes and methods

# Header class attributes and methods

# MainNav class attributes and methods

# Logo class attributes and methods

# Navigation class attributes and methods

# Search class attributes and methods

# Relationships
headerLink: BinaryAssociation = BinaryAssociation(
    name="headerLink",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
mainNavLink: BinaryAssociation = BinaryAssociation(
    name="mainNavLink",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="MainNav", type=MainNav, multiplicity=Multiplicity(1, 1))
    }
)
logoLink: BinaryAssociation = BinaryAssociation(
    name="logoLink",
    ends={
        Property(name="MainNav", type=MainNav, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Logo", type=Logo, multiplicity=Multiplicity(1, 1))
    }
)
navigationLink: BinaryAssociation = BinaryAssociation(
    name="navigationLink",
    ends={
        Property(name="MainNav", type=MainNav, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
searchLink: BinaryAssociation = BinaryAssociation(
    name="searchLink",
    ends={
        Property(name="MainNav", type=MainNav, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Search", type=Search, multiplicity=Multiplicity(1, 1))
    }
)
cartLink: BinaryAssociation = BinaryAssociation(
    name="cartLink",
    ends={
        Property(name="MainNav", type=MainNav, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Cart", type=Cart, multiplicity=Multiplicity(1, 1))
    }
)
circleLink: BinaryAssociation = BinaryAssociation(
    name="circleLink",
    ends={
        Property(name="ProductSection", type=ProductSection, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Circle", type=Circle, multiplicity=Multiplicity(1, 1))
    }
)
prodDescriptionLink: BinaryAssociation = BinaryAssociation(
    name="prodDescriptionLink",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="ProdDescription", type=ProdDescription, multiplicity=Multiplicity(1, 1))
    }
)
articleLink: BinaryAssociation = BinaryAssociation(
    name="articleLink",
    ends={
        Property(name="ProdDescription", type=ProdDescription, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Article", type=Article, multiplicity=Multiplicity(1, 1))
    }
)
wrapperLink: BinaryAssociation = BinaryAssociation(
    name="wrapperLink",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1))
    }
)
productSectionLink: BinaryAssociation = BinaryAssociation(
    name="productSectionLink",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="ProductSection", type=ProductSection, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Cart, Wrapper, ProductSection, Circle, ProdDescription, Article, Container, Header, MainNav, Logo, Navigation, Search},
    associations={headerLink, mainNavLink, logoLink, navigationLink, searchLink, cartLink, circleLink, prodDescriptionLink, articleLink, wrapperLink, productSectionLink},
    generalizations={}
)
