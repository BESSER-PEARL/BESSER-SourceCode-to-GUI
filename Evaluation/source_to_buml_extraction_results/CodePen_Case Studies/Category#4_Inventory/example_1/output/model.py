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
Dashboard = Class(name="Dashboard")
MovementTable = Class(name="MovementTable")
CashMovementTable = Class(name="CashMovementTable")
Charts = Class(name="Charts")

# Dashboard class attributes and methods
Dashboard_product: Property = Property(name="product", type=StringType)
Dashboard_quantityIn: Property = Property(name="quantityIn", type=IntegerType)
Dashboard_price: Property = Property(name="price", type=FloatType)
Dashboard_salePrice: Property = Property(name="salePrice", type=FloatType)
Dashboard_dateIn: Property = Property(name="dateIn", type=DateType)
Dashboard_productSale: Property = Property(name="productSale", type=StringType)
Dashboard_quantityOut: Property = Property(name="quantityOut", type=IntegerType)
Dashboard_dateOut: Property = Property(name="dateOut", type=DateType)
Dashboard_totalCost: Property = Property(name="totalCost", type=FloatType)
Dashboard_totalSales: Property = Property(name="totalSales", type=FloatType)
Dashboard_totalProfit: Property = Property(name="totalProfit", type=FloatType)
Dashboard_totalSaleProfit: Property = Property(name="totalSaleProfit", type=FloatType)
Dashboard.attributes={Dashboard_price, Dashboard_productSale, Dashboard_totalSales, Dashboard_totalCost, Dashboard_totalProfit, Dashboard_dateIn, Dashboard_product, Dashboard_dateOut, Dashboard_totalSaleProfit, Dashboard_quantityOut, Dashboard_quantityIn, Dashboard_salePrice}

# MovementTable class attributes and methods

# CashMovementTable class attributes and methods

# Charts class attributes and methods
Charts_revenueChart: Property = Property(name="revenueChart", type=StringType)
Charts_inventoryChart: Property = Property(name="inventoryChart", type=StringType)
Charts.attributes={Charts_revenueChart, Charts_inventoryChart}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Dashboard", type=Dashboard, multiplicity=Multiplicity(1, 1)),
        Property(name="MovementTable", type=MovementTable, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Dashboard", type=Dashboard, multiplicity=Multiplicity(1, 1)),
        Property(name="CashMovementTable", type=CashMovementTable, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Dashboard", type=Dashboard, multiplicity=Multiplicity(1, 1)),
        Property(name="Charts", type=Charts, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Dashboard, MovementTable, CashMovementTable, Charts},
    associations={association1, association2, association3},
    generalizations={}
)
