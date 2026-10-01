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
FoodSite = Class(name="FoodSite")
SearchBar = Class(name="SearchBar")
Table = Class(name="Table")
Category = Class(name="Category")
Recipe = Class(name="Recipe")
NutritionInfo = Class(name="NutritionInfo")

# FoodSite class attributes and methods

# SearchBar class attributes and methods

# Table class attributes and methods

# Category class attributes and methods

# Recipe class attributes and methods

# NutritionInfo class attributes and methods

# Relationships
hasCategory: BinaryAssociation = BinaryAssociation(
    name="hasCategory",
    ends={
        Property(name="Table", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Category", type=Category, multiplicity=Multiplicity(1, 1))
    }
)
containsSearchBar: BinaryAssociation = BinaryAssociation(
    name="containsSearchBar",
    ends={
        Property(name="FoodSite", type=FoodSite, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
hasRecipe: BinaryAssociation = BinaryAssociation(
    name="hasRecipe",
    ends={
        Property(name="Table", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Recipe", type=Recipe, multiplicity=Multiplicity(1, 1))
    }
)
hasNutritionInfo: BinaryAssociation = BinaryAssociation(
    name="hasNutritionInfo",
    ends={
        Property(name="Table", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="NutritionInfo", type=NutritionInfo, multiplicity=Multiplicity(1, 1))
    }
)
containsTable: BinaryAssociation = BinaryAssociation(
    name="containsTable",
    ends={
        Property(name="FoodSite", type=FoodSite, multiplicity=Multiplicity(1, 1)),
        Property(name="Table", type=Table, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={FoodSite, SearchBar, Table, Category, Recipe, NutritionInfo},
    associations={hasCategory, containsSearchBar, hasRecipe, hasNutritionInfo, containsTable},
    generalizations={}
)
