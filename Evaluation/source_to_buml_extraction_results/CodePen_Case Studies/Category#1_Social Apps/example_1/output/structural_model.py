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
InventoryPage = Class(name="InventoryPage")
Footer = Class(name="Footer")

# InventoryPage class attributes and methods
InventoryPage_search: Property = Property(name="search", type=StringType)
InventoryPage.attributes={InventoryPage_search}

# Footer class attributes and methods
Footer_content: Property = Property(name="content", type=StringType)
Footer.attributes={Footer_content}

# Relationships
footerAssociation: BinaryAssociation = BinaryAssociation(
    name="footerAssociation",
    ends={
        Property(name="InventoryPage", type=InventoryPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={InventoryPage, Footer},
    associations={footerAssociation},
    generalizations={}
)
