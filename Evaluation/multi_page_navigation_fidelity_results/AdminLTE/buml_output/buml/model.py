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
StarterPage = Class(name="StarterPage")
Users = Class(name="Users")
Dashboard = Class(name="Dashboard")
DashboardV2 = Class(name="DashboardV2")
DashboardV3 = Class(name="DashboardV3")

# StarterPage class attributes and methods
StarterPage_starterCardTitle: Property = Property(name="starterCardTitle", type=StringType)
StarterPage_starterCardBodyText: Property = Property(name="starterCardBodyText", type=StringType)
StarterPage.attributes={StarterPage_starterCardBodyText, StarterPage_starterCardTitle}

# Users class attributes and methods
Users_usersShowingFrom: Property = Property(name="usersShowingFrom", type=IntegerType)
Users_usersShowingTo: Property = Property(name="usersShowingTo", type=IntegerType)
Users_usersTotal: Property = Property(name="usersTotal", type=IntegerType)
Users.attributes={Users_usersTotal, Users_usersShowingFrom, Users_usersShowingTo}

# Dashboard class attributes and methods
Dashboard_newOrders: Property = Property(name="newOrders", type=IntegerType)
Dashboard_bounceRatePercent: Property = Property(name="bounceRatePercent", type=FloatType)
Dashboard_userRegistrations: Property = Property(name="userRegistrations", type=IntegerType)
Dashboard_uniqueVisitors: Property = Property(name="uniqueVisitors", type=IntegerType)
Dashboard_directChatNewMessages: Property = Property(name="directChatNewMessages", type=IntegerType)
Dashboard.attributes={Dashboard_uniqueVisitors, Dashboard_directChatNewMessages, Dashboard_newOrders, Dashboard_userRegistrations, Dashboard_bounceRatePercent}

# DashboardV2 class attributes and methods
DashboardV2_cpuTrafficPercent: Property = Property(name="cpuTrafficPercent", type=FloatType)
DashboardV2_likes: Property = Property(name="likes", type=IntegerType)
DashboardV2_sales: Property = Property(name="sales", type=IntegerType)
DashboardV2_newMembers: Property = Property(name="newMembers", type=IntegerType)
DashboardV2_totalRevenue: Property = Property(name="totalRevenue", type=FloatType)
DashboardV2_totalCost: Property = Property(name="totalCost", type=FloatType)
DashboardV2_totalProfit: Property = Property(name="totalProfit", type=FloatType)
DashboardV2_goalCompletions: Property = Property(name="goalCompletions", type=IntegerType)
DashboardV2_inventory: Property = Property(name="inventory", type=IntegerType)
DashboardV2_mentions: Property = Property(name="mentions", type=IntegerType)
DashboardV2_downloads: Property = Property(name="downloads", type=IntegerType)
DashboardV2.attributes={DashboardV2_newMembers, DashboardV2_goalCompletions, DashboardV2_cpuTrafficPercent, DashboardV2_totalRevenue, DashboardV2_totalProfit, DashboardV2_inventory, DashboardV2_downloads, DashboardV2_likes, DashboardV2_totalCost, DashboardV2_mentions, DashboardV2_sales}

# DashboardV3 class attributes and methods
DashboardV3_visitorsTotal: Property = Property(name="visitorsTotal", type=IntegerType)
DashboardV3_visitorsChangePercent: Property = Property(name="visitorsChangePercent", type=FloatType)
DashboardV3_salesTotal: Property = Property(name="salesTotal", type=FloatType)
DashboardV3_salesChangePercent: Property = Property(name="salesChangePercent", type=FloatType)
DashboardV3_conversionRatePercent: Property = Property(name="conversionRatePercent", type=FloatType)
DashboardV3_salesRatePercent: Property = Property(name="salesRatePercent", type=FloatType)
DashboardV3_registrationRatePercent: Property = Property(name="registrationRatePercent", type=FloatType)
DashboardV3.attributes={DashboardV3_visitorsTotal, DashboardV3_visitorsChangePercent, DashboardV3_registrationRatePercent, DashboardV3_salesTotal, DashboardV3_salesChangePercent, DashboardV3_conversionRatePercent, DashboardV3_salesRatePercent}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={StarterPage, Users, Dashboard, DashboardV2, DashboardV3},
    associations={},
    generalizations={},
    metadata=None
)
