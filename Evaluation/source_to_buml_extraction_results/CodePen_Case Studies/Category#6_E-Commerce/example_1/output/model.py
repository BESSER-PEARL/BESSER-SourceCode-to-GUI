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
TaksitTablosu = Class(name="TaksitTablosu")
KrediKarti = Class(name="KrediKarti")
Taksit = Class(name="Taksit")
VadeFarksizTaksitSecenekleri = Class(name="VadeFarksizTaksitSecenekleri")

# TaksitTablosu class attributes and methods

# KrediKarti class attributes and methods

# Taksit class attributes and methods
Taksit_ikiTaksitAkbank: Property = Property(name="ikiTaksitAkbank", type=StringType)
Taksit_ucTaksitAkbank: Property = Property(name="ucTaksitAkbank", type=StringType)
Taksit_dortTaksitAkbank: Property = Property(name="dortTaksitAkbank", type=StringType)
Taksit_besTaksitAkbank: Property = Property(name="besTaksitAkbank", type=StringType)
Taksit_altiTaksitAkbank: Property = Property(name="altiTaksitAkbank", type=StringType)
Taksit_ikiTaksitBonus: Property = Property(name="ikiTaksitBonus", type=StringType)
Taksit_dortTaksitBonus: Property = Property(name="dortTaksitBonus", type=StringType)
Taksit_besTaksitBonus: Property = Property(name="besTaksitBonus", type=StringType)
Taksit_altiTaksitBonus: Property = Property(name="altiTaksitBonus", type=StringType)
Taksit_ikiTaksitWord: Property = Property(name="ikiTaksitWord", type=StringType)
Taksit_ucTaksitWord: Property = Property(name="ucTaksitWord", type=StringType)
Taksit_dortTaksitWord: Property = Property(name="dortTaksitWord", type=StringType)
Taksit_besTaksitWord: Property = Property(name="besTaksitWord", type=StringType)
Taksit_altiTaksitWord: Property = Property(name="altiTaksitWord", type=StringType)
Taksit_ikiTaksitZiraat: Property = Property(name="ikiTaksitZiraat", type=StringType)
Taksit_ucTaksitZiraat: Property = Property(name="ucTaksitZiraat", type=StringType)
Taksit_dortTaksitZiraat: Property = Property(name="dortTaksitZiraat", type=StringType)
Taksit_besTaksitZiraat: Property = Property(name="besTaksitZiraat", type=StringType)
Taksit_altiTaksitZiraat: Property = Property(name="altiTaksitZiraat", type=StringType)
Taksit_ikiTaksitFinans: Property = Property(name="ikiTaksitFinans", type=StringType)
Taksit_ucTaksitFinans: Property = Property(name="ucTaksitFinans", type=StringType)
Taksit_dortTaksitFinans: Property = Property(name="dortTaksitFinans", type=StringType)
Taksit_besTaksitFinans: Property = Property(name="besTaksitFinans", type=StringType)
Taksit_altiTaksitFinans: Property = Property(name="altiTaksitFinans", type=StringType)
Taksit_ucTaksitBonus: Property = Property(name="ucTaksitBonus", type=StringType)
Taksit.attributes={Taksit_ucTaksitFinans, Taksit_dortTaksitFinans, Taksit_ikiTaksitBonus, Taksit_besTaksitFinans, Taksit_altiTaksitFinans, Taksit_dortTaksitBonus, Taksit_ucTaksitAkbank, Taksit_altiTaksitAkbank, Taksit_besTaksitBonus, Taksit_ikiTaksitFinans, Taksit_altiTaksitBonus, Taksit_ikiTaksitWord, Taksit_ucTaksitWord, Taksit_dortTaksitWord, Taksit_besTaksitWord, Taksit_ucTaksitBonus, Taksit_altiTaksitWord, Taksit_ikiTaksitZiraat, Taksit_ikiTaksitAkbank, Taksit_ucTaksitZiraat, Taksit_dortTaksitZiraat, Taksit_besTaksitZiraat, Taksit_altiTaksitZiraat, Taksit_besTaksitAkbank, Taksit_dortTaksitAkbank}

# VadeFarksizTaksitSecenekleri class attributes and methods

# Relationships
tablosuKrediKarti: BinaryAssociation = BinaryAssociation(
    name="tablosuKrediKarti",
    ends={
        Property(name="TaksitTablosu", type=TaksitTablosu, multiplicity=Multiplicity(1, 1)),
        Property(name="KrediKarti", type=KrediKarti, multiplicity=Multiplicity(5, 5))
    }
)
kartiTaksit: BinaryAssociation = BinaryAssociation(
    name="kartiTaksit",
    ends={
        Property(name="KrediKarti", type=KrediKarti, multiplicity=Multiplicity(1, 1)),
        Property(name="Taksit", type=Taksit, multiplicity=Multiplicity(1, 1))
    }
)
vadeTaksitTablosu: BinaryAssociation = BinaryAssociation(
    name="vadeTaksitTablosu",
    ends={
        Property(name="VadeFarksizTaksitSecenekleri", type=VadeFarksizTaksitSecenekleri, multiplicity=Multiplicity(1, 1)),
        Property(name="TaksitTablosu", type=TaksitTablosu, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={TaksitTablosu, KrediKarti, Taksit, VadeFarksizTaksitSecenekleri},
    associations={tablosuKrediKarti, kartiTaksit, vadeTaksitTablosu},
    generalizations={}
)
