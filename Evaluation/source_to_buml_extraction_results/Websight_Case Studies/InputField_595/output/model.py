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
Navigation = Class(name="Navigation")
SearchBar = Class(name="SearchBar")
HeroImage = Class(name="HeroImage")
PopularDishesSection = Class(name="PopularDishesSection")
CustomerTestimonialsSection = Class(name="CustomerTestimonialsSection")
CallToActionSection = Class(name="CallToActionSection")

# WebPage class attributes and methods

# Header class attributes and methods

# Navigation class attributes and methods

# SearchBar class attributes and methods

# HeroImage class attributes and methods

# PopularDishesSection class attributes and methods

# CustomerTestimonialsSection class attributes and methods

# CallToActionSection class attributes and methods

# Relationships
containsHeader: BinaryAssociation = BinaryAssociation(
    name="containsHeader",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
includesNavigation: BinaryAssociation = BinaryAssociation(
    name="includesNavigation",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
includesSearchBar: BinaryAssociation = BinaryAssociation(
    name="includesSearchBar",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
containsCallToAction: BinaryAssociation = BinaryAssociation(
    name="containsCallToAction",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CallToActionSection", type=CallToActionSection, multiplicity=Multiplicity(1, 1))
    }
)
containsHeroImage: BinaryAssociation = BinaryAssociation(
    name="containsHeroImage",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="HeroImage", type=HeroImage, multiplicity=Multiplicity(1, 1))
    }
)
containsPopularDishes: BinaryAssociation = BinaryAssociation(
    name="containsPopularDishes",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="PopularDishesSection", type=PopularDishesSection, multiplicity=Multiplicity(1, 1))
    }
)
containsTestimonials: BinaryAssociation = BinaryAssociation(
    name="containsTestimonials",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CustomerTestimonialsSection", type=CustomerTestimonialsSection, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, SearchBar, HeroImage, PopularDishesSection, CustomerTestimonialsSection, CallToActionSection},
    associations={containsHeader, includesNavigation, includesSearchBar, containsCallToAction, containsHeroImage, containsPopularDishes, containsTestimonials},
    generalizations={}
)
