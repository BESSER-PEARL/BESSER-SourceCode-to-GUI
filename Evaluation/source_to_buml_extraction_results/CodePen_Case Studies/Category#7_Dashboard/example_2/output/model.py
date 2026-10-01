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
PageHeader = Class(name="PageHeader")
AdminMenu = Class(name="AdminMenu")
PageContent = Class(name="PageContent")

# PageHeader class attributes and methods
PageHeader_logo: Property = Property(name="logo", type=StringType)
PageHeader_toggleMobMenu: Property = Property(name="toggleMobMenu", type=BooleanType)
PageHeader.attributes={PageHeader_toggleMobMenu, PageHeader_logo}

# AdminMenu class attributes and methods
AdminMenu_appearance: Property = Property(name="appearance", type=StringType)
AdminMenu_settings: Property = Property(name="settings", type=StringType)
AdminMenu_options: Property = Property(name="options", type=StringType)
AdminMenu_charts: Property = Property(name="charts", type=StringType)
AdminMenu_mode: Property = Property(name="mode", type=BooleanType)
AdminMenu_collapseMenu: Property = Property(name="collapseMenu", type=BooleanType)
AdminMenu_menuHeading: Property = Property(name="menuHeading", type=StringType)
AdminMenu_pages: Property = Property(name="pages", type=StringType)
AdminMenu_users: Property = Property(name="users", type=StringType)
AdminMenu_trends: Property = Property(name="trends", type=StringType)
AdminMenu_collection: Property = Property(name="collection", type=StringType)
AdminMenu_comments: Property = Property(name="comments", type=StringType)
AdminMenu.attributes={AdminMenu_menuHeading, AdminMenu_settings, AdminMenu_collapseMenu, AdminMenu_collection, AdminMenu_mode, AdminMenu_options, AdminMenu_users, AdminMenu_comments, AdminMenu_appearance, AdminMenu_charts, AdminMenu_pages, AdminMenu_trends}

# PageContent class attributes and methods
PageContent_search: Property = Property(name="search", type=StringType)
PageContent_grid: Property = Property(name="grid", type=StringType)
PageContent_footerMadeBy: Property = Property(name="footerMadeBy", type=StringType)
PageContent_footerLogo: Property = Property(name="footerLogo", type=StringType)
PageContent_greeting: Property = Property(name="greeting", type=StringType)
PageContent_notifications: Property = Property(name="notifications", type=IntegerType)
PageContent.attributes={PageContent_footerLogo, PageContent_search, PageContent_greeting, PageContent_grid, PageContent_notifications, PageContent_footerMadeBy}

# Relationships
headerMenu: BinaryAssociation = BinaryAssociation(
    name="headerMenu",
    ends={
        Property(name="PageHeader", type=PageHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="AdminMenu", type=AdminMenu, multiplicity=Multiplicity(1, 1))
    }
)
contentHeader: BinaryAssociation = BinaryAssociation(
    name="contentHeader",
    ends={
        Property(name="PageContent", type=PageContent, multiplicity=Multiplicity(1, 1)),
        Property(name="PageHeader", type=PageHeader, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={PageHeader, AdminMenu, PageContent},
    associations={headerMenu, contentHeader},
    generalizations={}
)
