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
ItemForm = Class(name="ItemForm")
Search = Class(name="Search")
ItemTable = Class(name="ItemTable")

# ItemForm class attributes and methods
ItemForm_itemDescription: Property = Property(name="itemDescription", type=StringType)
ItemForm_price: Property = Property(name="price", type=FloatType)
ItemForm_itemCode: Property = Property(name="itemCode", type=StringType)
ItemForm.attributes={ItemForm_itemCode, ItemForm_price, ItemForm_itemDescription}

# Search class attributes and methods
Search_query: Property = Property(name="query", type=StringType)
Search.attributes={Search_query}

# ItemTable class attributes and methods
ItemTable_item: Property = Property(name="item", type=StringType)
ItemTable_description: Property = Property(name="description", type=StringType)
ItemTable_quantity: Property = Property(name="quantity", type=IntegerType)
ItemTable_discount: Property = Property(name="discount", type=FloatType)
ItemTable_price: Property = Property(name="price", type=FloatType)
ItemTable.attributes={ItemTable_quantity, ItemTable_discount, ItemTable_item, ItemTable_description, ItemTable_price}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="ItemForm", type=ItemForm, multiplicity=Multiplicity(1, 1)),
        Property(name="Search", type=Search, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="ItemForm", type=ItemForm, multiplicity=Multiplicity(1, 1)),
        Property(name="ItemTable", type=ItemTable, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ItemForm, Search, ItemTable},
    associations={association1, association2},
    generalizations={}
)
