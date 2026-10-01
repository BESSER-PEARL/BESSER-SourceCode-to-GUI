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
Superhero = Class(name="Superhero")
SuperheroesList = Class(name="SuperheroesList")
HeroDetail = Class(name="HeroDetail")
HeroAdd = Class(name="HeroAdd")
HeroEdit = Class(name="HeroEdit")
HeroDelete = Class(name="HeroDelete")

# Superhero class attributes and methods
Superhero_id: Property = Property(name="id", type=IntegerType)
Superhero_name: Property = Property(name="name", type=StringType)
Superhero_power: Property = Property(name="power", type=StringType)
Superhero_badass: Property = Property(name="badass", type=IntegerType)
Superhero.attributes={Superhero_id, Superhero_badass, Superhero_name, Superhero_power}

# SuperheroesList class attributes and methods
SuperheroesList_filteredHeroesCount: Property = Property(name="filteredHeroesCount", type=IntegerType)
SuperheroesList.attributes={SuperheroesList_filteredHeroesCount}

# HeroDetail class attributes and methods
HeroDetail_heroId: Property = Property(name="heroId", type=IntegerType)
HeroDetail.attributes={HeroDetail_heroId}

# HeroAdd class attributes and methods
HeroAdd_newHeroName: Property = Property(name="newHeroName", type=StringType)
HeroAdd.attributes={HeroAdd_newHeroName}

# HeroEdit class attributes and methods
HeroEdit_editHeroId: Property = Property(name="editHeroId", type=IntegerType)
HeroEdit.attributes={HeroEdit_editHeroId}

# HeroDelete class attributes and methods
HeroDelete_deleteHeroId: Property = Property(name="deleteHeroId", type=IntegerType)
HeroDelete.attributes={HeroDelete_deleteHeroId}

# Relationships
listContains: BinaryAssociation = BinaryAssociation(
    name="listContains",
    ends={
        Property(name="SuperheroesList", type=SuperheroesList, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Superhero", type=Superhero, multiplicity=Multiplicity(0, 9999))
    }
)
detailOf: BinaryAssociation = BinaryAssociation(
    name="detailOf",
    ends={
        Property(name="HeroDetail", type=HeroDetail, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Superhero", type=Superhero, multiplicity=Multiplicity(1, 1))
    }
)
addNew: BinaryAssociation = BinaryAssociation(
    name="addNew",
    ends={
        Property(name="HeroAdd", type=HeroAdd, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Superhero", type=Superhero, multiplicity=Multiplicity(1, 1))
    }
)
editExisting: BinaryAssociation = BinaryAssociation(
    name="editExisting",
    ends={
        Property(name="HeroEdit", type=HeroEdit, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Superhero", type=Superhero, multiplicity=Multiplicity(1, 1))
    }
)
deleteExisting: BinaryAssociation = BinaryAssociation(
    name="deleteExisting",
    ends={
        Property(name="HeroDelete", type=HeroDelete, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Superhero", type=Superhero, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Superhero, SuperheroesList, HeroDetail, HeroAdd, HeroEdit, HeroDelete},
    associations={listContains, detailOf, addNew, editExisting, deleteExisting},
    generalizations={}
)
