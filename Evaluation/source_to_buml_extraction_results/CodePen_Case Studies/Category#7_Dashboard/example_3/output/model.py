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
Navbar = Class(name="Navbar")
Sidebar = Class(name="Sidebar")
Card = Class(name="Card")
Project = Class(name="Project")
Chart = Class(name="Chart")

# Navbar class attributes and methods
Navbar_brand: Property = Property(name="brand", type=StringType)
Navbar_search: Property = Property(name="search", type=StringType)
Navbar_signOutLink: Property = Property(name="signOutLink", type=StringType)
Navbar.attributes={Navbar_brand, Navbar_search, Navbar_signOutLink}

# Sidebar class attributes and methods
Sidebar_dashboardLink: Property = Property(name="dashboardLink", type=StringType)
Sidebar_ordersLink: Property = Property(name="ordersLink", type=StringType)
Sidebar_productsLink: Property = Property(name="productsLink", type=StringType)
Sidebar_customersLink: Property = Property(name="customersLink", type=StringType)
Sidebar_reportsLink: Property = Property(name="reportsLink", type=StringType)
Sidebar_integrationsLink: Property = Property(name="integrationsLink", type=StringType)
Sidebar_savedReports: Property = Property(name="savedReports", type=StringType)
Sidebar.attributes={Sidebar_ordersLink, Sidebar_savedReports, Sidebar_productsLink, Sidebar_customersLink, Sidebar_dashboardLink, Sidebar_reportsLink, Sidebar_integrationsLink}

# Card class attributes and methods
Card_title: Property = Property(name="title", type=StringType)
Card_value: Property = Property(name="value", type=StringType)
Card_stat: Property = Property(name="stat", type=StringType)
Card.attributes={Card_value, Card_title, Card_stat}

# Project class attributes and methods
Project_name: Property = Property(name="name", type=StringType)
Project_client: Property = Property(name="client", type=StringType)
Project_deadline: Property = Property(name="deadline", type=DateType)
Project_leader: Property = Property(name="leader", type=StringType)
Project_team: Property = Property(name="team", type=StringType)
Project_budget: Property = Property(name="budget", type=StringType)
Project_status: Property = Property(name="status", type=StringType)
Project.attributes={Project_team, Project_name, Project_client, Project_budget, Project_deadline, Project_status, Project_leader}

# Chart class attributes and methods
Chart_title: Property = Property(name="title", type=StringType)
Chart_tagline: Property = Property(name="tagline", type=StringType)
Chart.attributes={Chart_tagline, Chart_title}

# Relationships
Navbar_Sidebar: BinaryAssociation = BinaryAssociation(
    name="Navbar_Sidebar",
    ends={
        Property(name="Navbar", type=Navbar, multiplicity=Multiplicity(0, 9999)),
        Property(name="Sidebar", type=Sidebar, multiplicity=Multiplicity(0, 9999))
    }
)
Sidebar_Card: BinaryAssociation = BinaryAssociation(
    name="Sidebar_Card",
    ends={
        Property(name="Sidebar", type=Sidebar, multiplicity=Multiplicity(0, 9999)),
        Property(name="Card", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)
Sidebar_Project: BinaryAssociation = BinaryAssociation(
    name="Sidebar_Project",
    ends={
        Property(name="Sidebar", type=Sidebar, multiplicity=Multiplicity(0, 9999)),
        Property(name="Project", type=Project, multiplicity=Multiplicity(0, 9999))
    }
)
Sidebar_Chart: BinaryAssociation = BinaryAssociation(
    name="Sidebar_Chart",
    ends={
        Property(name="Sidebar", type=Sidebar, multiplicity=Multiplicity(0, 9999)),
        Property(name="Chart", type=Chart, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Navbar, Sidebar, Card, Project, Chart},
    associations={Navbar_Sidebar, Sidebar_Card, Sidebar_Project, Sidebar_Chart},
    generalizations={}
)
