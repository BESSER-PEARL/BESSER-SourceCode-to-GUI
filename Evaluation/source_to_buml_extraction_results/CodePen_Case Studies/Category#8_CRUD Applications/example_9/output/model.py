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
EditProduct = Class(name="EditProduct")
DeleteProduct = Class(name="DeleteProduct")

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product_price: Property = Property(name="price", type=FloatType)
Product.attributes={Product_description, Product_price, Product_name}

# ProductList class attributes and methods
ProductList_searchKey: Property = Property(name="searchKey", type=StringType)
ProductList.attributes={ProductList_searchKey}

# AddProduct class attributes and methods
AddProduct_productName: Property = Property(name="productName", type=StringType)
AddProduct_productDescription: Property = Property(name="productDescription", type=StringType)
AddProduct_productPrice: Property = Property(name="productPrice", type=FloatType)
AddProduct.attributes={AddProduct_productDescription, AddProduct_productPrice, AddProduct_productName}

# EditProduct class attributes and methods
EditProduct_productName: Property = Property(name="productName", type=StringType)
EditProduct_productDescription: Property = Property(name="productDescription", type=StringType)
EditProduct_productPrice: Property = Property(name="productPrice", type=FloatType)
EditProduct.attributes={EditProduct_productDescription, EditProduct_productName, EditProduct_productPrice}

# DeleteProduct class attributes and methods
DeleteProduct_productName: Property = Property(name="productName", type=StringType)
DeleteProduct.attributes={DeleteProduct_productName}

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
        Property(name="EditProduct", type=EditProduct, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
deleteProduct: BinaryAssociation = BinaryAssociation(
    name="deleteProduct",
    ends={
        Property(name="DeleteProduct", type=DeleteProduct, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Product, ProductList, AddProduct, EditProduct, DeleteProduct},
    associations={listProducts, addProduct, editProduct, deleteProduct},
    generalizations={}
)
