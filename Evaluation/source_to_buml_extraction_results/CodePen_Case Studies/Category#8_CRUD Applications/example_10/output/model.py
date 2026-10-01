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
Bodega = Class(name="Bodega")

# Bodega class attributes and methods
Bodega_nombre: Property = Property(name="nombre", type=StringType)
Bodega_localizacion: Property = Property(name="localizacion", type=StringType)
Bodega_telefono: Property = Property(name="telefono", type=StringType)
Bodega_email: Property = Property(name="email", type=StringType)
Bodega.attributes={Bodega_nombre, Bodega_email, Bodega_localizacion, Bodega_telefono}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Bodega},
    associations={},
    generalizations={}
)
