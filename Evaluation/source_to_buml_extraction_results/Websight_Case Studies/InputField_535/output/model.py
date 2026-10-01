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
TravelAgency = Class(name="TravelAgency")
Header = Class(name="Header")
SearchBar = Class(name="SearchBar")
Destination = Class(name="Destination")
BookingSection = Class(name="BookingSection")

# TravelAgency class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header_subtitle: Property = Property(name="subtitle", type=StringType)
Header.attributes={Header_subtitle, Header_title}

# SearchBar class attributes and methods
SearchBar_placeholder: Property = Property(name="placeholder", type=StringType)
SearchBar.attributes={SearchBar_placeholder}

# Destination class attributes and methods
Destination_image: Property = Property(name="image", type=StringType)
Destination_description: Property = Property(name="description", type=StringType)
Destination.attributes={Destination_description, Destination_image}

# BookingSection class attributes and methods
BookingSection_title: Property = Property(name="title", type=StringType)
BookingSection_description: Property = Property(name="description", type=StringType)
BookingSection.attributes={BookingSection_title, BookingSection_description}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="TravelAgency", type=TravelAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
searchBar: BinaryAssociation = BinaryAssociation(
    name="searchBar",
    ends={
        Property(name="TravelAgency", type=TravelAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
destinations: BinaryAssociation = BinaryAssociation(
    name="destinations",
    ends={
        Property(name="TravelAgency", type=TravelAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="Destination", type=Destination, multiplicity=Multiplicity(3, 3))
    }
)
bookingSection: BinaryAssociation = BinaryAssociation(
    name="bookingSection",
    ends={
        Property(name="TravelAgency", type=TravelAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="BookingSection", type=BookingSection, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={TravelAgency, Header, SearchBar, Destination, BookingSection},
    associations={header, searchBar, destinations, bookingSection},
    generalizations={}
)
