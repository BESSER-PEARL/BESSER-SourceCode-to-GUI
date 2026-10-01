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
Header = Class(name="Header")
Main = Class(name="Main")
Footer = Class(name="Footer")

# Header class attributes and methods
Header_publishing: Property = Property(name="publishing", type=StringType)
Header_gallery: Property = Property(name="gallery", type=StringType)
Header_foto: Property = Property(name="foto", type=StringType)
Header_email: Property = Property(name="email", type=StringType)
Header_videos: Property = Property(name="videos", type=StringType)
Header_buy: Property = Property(name="buy", type=StringType)
Header_faq: Property = Property(name="faq", type=StringType)
Header.attributes={Header_email, Header_videos, Header_foto, Header_gallery, Header_publishing, Header_faq, Header_buy}

# Main class attributes and methods
Main_search: Property = Property(name="search", type=StringType)
Main_logo: Property = Property(name="logo", type=StringType)
Main.attributes={Main_logo, Main_search}

# Footer class attributes and methods
Footer_chumhumAgency: Property = Property(name="chumhumAgency", type=StringType)
Footer_chumhumApps: Property = Property(name="chumhumApps", type=StringType)
Footer_chumhumWorkGroup: Property = Property(name="chumhumWorkGroup", type=StringType)
Footer_chumhumPhotos: Property = Property(name="chumhumPhotos", type=StringType)
Footer_copyright: Property = Property(name="copyright", type=StringType)
Footer.attributes={Footer_chumhumPhotos, Footer_chumhumApps, Footer_copyright, Footer_chumhumAgency, Footer_chumhumWorkGroup}

# Relationships
header_to_main: BinaryAssociation = BinaryAssociation(
    name="header_to_main",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
main_to_footer: BinaryAssociation = BinaryAssociation(
    name="main_to_footer",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Header, Main, Footer},
    associations={header_to_main, main_to_footer},
    generalizations={}
)
