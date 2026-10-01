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
Expenses = Class(name="Expenses")
Header = Class(name="Header")
Menu = Class(name="Menu")
Account = Class(name="Account")
AccountBox = Class(name="AccountBox")
Aside = Class(name="Aside")
Dashboard = Class(name="Dashboard")
Profits = Class(name="Profits")

# Expenses class attributes and methods
Expenses_amount: Property = Property(name="amount", type=StringType)
Expenses_description: Property = Property(name="description", type=StringType)
Expenses.attributes={Expenses_amount, Expenses_description}

# Header class attributes and methods
Header_menu: Property = Property(name="menu", type=StringType)
Header_account: Property = Property(name="account", type=StringType)
Header_accountBox: Property = Property(name="accountBox", type=StringType)
Header.attributes={Header_menu, Header_account, Header_accountBox}

# Menu class attributes and methods
Menu_analytics: Property = Property(name="analytics", type=StringType)
Menu_reports: Property = Property(name="reports", type=StringType)
Menu_settings: Property = Property(name="settings", type=StringType)
Menu_viewProfile: Property = Property(name="viewProfile", type=StringType)
Menu_messages: Property = Property(name="messages", type=StringType)
Menu_logOut: Property = Property(name="logOut", type=StringType)
Menu.attributes={Menu_settings, Menu_analytics, Menu_viewProfile, Menu_messages, Menu_reports, Menu_logOut}

# Account class attributes and methods
Account_profileImage: Property = Property(name="profileImage", type=StringType)
Account_accountName: Property = Property(name="accountName", type=StringType)
Account.attributes={Account_profileImage, Account_accountName}

# AccountBox class attributes and methods
AccountBox_userName: Property = Property(name="userName", type=StringType)
AccountBox_viewProfile: Property = Property(name="viewProfile", type=StringType)
AccountBox_settings: Property = Property(name="settings", type=StringType)
AccountBox_messages: Property = Property(name="messages", type=StringType)
AccountBox_logOut: Property = Property(name="logOut", type=StringType)
AccountBox.attributes={AccountBox_settings, AccountBox_messages, AccountBox_userName, AccountBox_logOut, AccountBox_viewProfile}

# Aside class attributes and methods
Aside_analytics: Property = Property(name="analytics", type=StringType)
Aside_reports: Property = Property(name="reports", type=StringType)
Aside_settings: Property = Property(name="settings", type=StringType)
Aside.attributes={Aside_settings, Aside_analytics, Aside_reports}

# Dashboard class attributes and methods
Dashboard_chart: Property = Property(name="chart", type=StringType)
Dashboard_profits: Property = Property(name="profits", type=StringType)
Dashboard_expenses: Property = Property(name="expenses", type=StringType)
Dashboard.attributes={Dashboard_chart, Dashboard_expenses, Dashboard_profits}

# Profits class attributes and methods
Profits_description: Property = Property(name="description", type=StringType)
Profits_amount: Property = Property(name="amount", type=StringType)
Profits.attributes={Profits_amount, Profits_description}

# Relationships
header_menu: BinaryAssociation = BinaryAssociation(
    name="header_menu",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
header_account: BinaryAssociation = BinaryAssociation(
    name="header_account",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Account", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
header_accountBox: BinaryAssociation = BinaryAssociation(
    name="header_accountBox",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="AccountBox", type=AccountBox, multiplicity=Multiplicity(1, 1))
    }
)
dashboard_profits: BinaryAssociation = BinaryAssociation(
    name="dashboard_profits",
    ends={
        Property(name="Dashboard", type=Dashboard, multiplicity=Multiplicity(1, 1)),
        Property(name="Profits", type=Profits, multiplicity=Multiplicity(1, 1))
    }
)
dashboard_expenses: BinaryAssociation = BinaryAssociation(
    name="dashboard_expenses",
    ends={
        Property(name="Dashboard", type=Dashboard, multiplicity=Multiplicity(1, 1)),
        Property(name="Expenses", type=Expenses, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Expenses, Header, Menu, Account, AccountBox, Aside, Dashboard, Profits},
    associations={header_menu, header_account, header_accountBox, dashboard_profits, dashboard_expenses},
    generalizations={}
)
