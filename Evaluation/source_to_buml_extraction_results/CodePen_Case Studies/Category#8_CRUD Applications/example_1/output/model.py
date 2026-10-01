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
Product = Class(name="Product")
ProductList = Class(name="ProductList")
AddProduct = Class(name="AddProduct")
ProductEdit = Class(name="ProductEdit")
ProductDelete = Class(name="ProductDelete")

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product_price: Property = Property(name="price", type=FloatType)
Product.attributes={Product_price, Product_description, Product_name}

# ProductList class attributes and methods
ProductList_searchKey: Property = Property(name="searchKey", type=StringType)
ProductList.attributes={ProductList_searchKey}

# AddProduct class attributes and methods

# ProductEdit class attributes and methods

# ProductDelete class attributes and methods

# Relationships
listProducts: BinaryAssociation = BinaryAssociation(
    name="listProducts",
    ends={
        Property(name="ProductList", type=ProductList, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Product", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
addProduct: BinaryAssociation = BinaryAssociation(
    name="addProduct",
    ends={
        Property(name="AddProduct", type=AddProduct, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
editProduct: BinaryAssociation = BinaryAssociation(
    name="editProduct",
    ends={
        Property(name="ProductEdit", type=ProductEdit, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
deleteProduct: BinaryAssociation = BinaryAssociation(
    name="deleteProduct",
    ends={
        Property(name="ProductDelete", type=ProductDelete, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Product, ProductList, AddProduct, ProductEdit, ProductDelete},
    associations={listProducts, addProduct, editProduct, deleteProduct},
    generalizations={}
)
