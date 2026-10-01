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
SiteWrap = Class(name="SiteWrap")
SiteNav = Class(name="SiteNav")
Name = Class(name="Name")
Note = Class(name="Note")
Main = Class(name="Main")
Header = Class(name="Header")
Breadcrumbs = Class(name="Breadcrumbs")
NavTabs = Class(name="NavTabs")
ContentColumns = Class(name="ContentColumns")
Col = Class(name="Col")
Item = Class(name="Item")

# SiteWrap class attributes and methods

# SiteNav class attributes and methods

# Name class attributes and methods

# Note class attributes and methods
Note_title: Property = Property(name="title", type=StringType)
Note_description: Property = Property(name="description", type=StringType)
Note.attributes={Note_description, Note_title}

# Main class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header.attributes={Header_title}

# Breadcrumbs class attributes and methods

# NavTabs class attributes and methods
NavTabs_dealsCount: Property = Property(name="dealsCount", type=IntegerType)
NavTabs_libraryCount: Property = Property(name="libraryCount", type=IntegerType)
NavTabs.attributes={NavTabs_libraryCount, NavTabs_dealsCount}

# ContentColumns class attributes and methods

# Col class attributes and methods

# Item class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="SiteWrap", type=SiteWrap, multiplicity=Multiplicity(1, 1)),
        Property(name="SiteNav", type=SiteNav, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="SiteWrap", type=SiteWrap, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="SiteNav", type=SiteNav, multiplicity=Multiplicity(1, 1)),
        Property(name="Name", type=Name, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="SiteNav", type=SiteNav, multiplicity=Multiplicity(1, 1)),
        Property(name="Note", type=Note, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentColumns", type=ContentColumns, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Breadcrumbs", type=Breadcrumbs, multiplicity=Multiplicity(1, 1))
    }
)
association8: BinaryAssociation = BinaryAssociation(
    name="association8",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="NavTabs", type=NavTabs, multiplicity=Multiplicity(1, 1))
    }
)
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="ContentColumns", type=ContentColumns, multiplicity=Multiplicity(4, 4)),
        Property(name="Col", type=Col, multiplicity=Multiplicity(1, 1))
    }
)
association10: BinaryAssociation = BinaryAssociation(
    name="association10",
    ends={
        Property(name="Col", type=Col, multiplicity=Multiplicity(8, 8)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SiteWrap, SiteNav, Name, Note, Main, Header, Breadcrumbs, NavTabs, ContentColumns, Col, Item},
    associations={association1, association2, association3, association4, association5, association6, association7, association8, association9, association10},
    generalizations={}
)
