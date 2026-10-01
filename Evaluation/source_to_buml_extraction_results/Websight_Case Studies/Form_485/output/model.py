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
SearchForm = Class(name="SearchForm")
Main = Class(name="Main")
Aside = Class(name="Aside")
Section = Class(name="Section")
Article = Class(name="Article")

# WebPage class attributes and methods
WebPage_title: Property = Property(name="title", type=StringType)
WebPage.attributes={WebPage_title}

# Header class attributes and methods
Header_headerTitle: Property = Property(name="headerTitle", type=StringType)
Header.attributes={Header_headerTitle}

# Navigation class attributes and methods
Navigation_linkCount: Property = Property(name="linkCount", type=IntegerType)
Navigation.attributes={Navigation_linkCount}

# SearchForm class attributes and methods
SearchForm_searchPlaceholder: Property = Property(name="searchPlaceholder", type=StringType)
SearchForm.attributes={SearchForm_searchPlaceholder}

# Main class attributes and methods

# Aside class attributes and methods
Aside_asideTitle: Property = Property(name="asideTitle", type=StringType)
Aside_postCount: Property = Property(name="postCount", type=IntegerType)
Aside.attributes={Aside_asideTitle, Aside_postCount}

# Section class attributes and methods
Section_sectionTitle: Property = Property(name="sectionTitle", type=StringType)
Section.attributes={Section_sectionTitle}

# Article class attributes and methods
Article_articleTitle: Property = Property(name="articleTitle", type=StringType)
Article_articleContent: Property = Property(name="articleContent", type=StringType)
Article.attributes={Article_articleTitle, Article_articleContent}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchForm", type=SearchForm, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Aside", type=Aside, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Article", type=Article, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, SearchForm, Main, Aside, Section, Article},
    associations={association1, association2, association3, association4, association5, association6, association7},
    generalizations={}
)
