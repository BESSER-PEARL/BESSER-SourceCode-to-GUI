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
IndexPage = Class(name="IndexPage")

# IndexPage class attributes and methods
IndexPage_index_header: Property = Property(name="index_header", type=StringType)
IndexPage_index_logo: Property = Property(name="index_logo", type=StringType)
IndexPage_index_nav: Property = Property(name="index_nav", type=StringType)
IndexPage_index_search: Property = Property(name="index_search", type=StringType)
IndexPage_index_form: Property = Property(name="index_form", type=StringType)
IndexPage_index_query: Property = Property(name="index_query", type=StringType)
IndexPage_index_footer: Property = Property(name="index_footer", type=StringType)
IndexPage_index_bottom: Property = Property(name="index_bottom", type=StringType)
IndexPage_index_links: Property = Property(name="index_links", type=StringType)
IndexPage_index_copyright: Property = Property(name="index_copyright", type=StringType)
IndexPage_modal: Property = Property(name="modal", type=StringType)
IndexPage_modal_dialog: Property = Property(name="modal_dialog", type=StringType)
IndexPage_modal_header: Property = Property(name="modal_header", type=StringType)
IndexPage_modal_body: Property = Property(name="modal_body", type=StringType)
IndexPage_modal_footer: Property = Property(name="modal_footer", type=StringType)
IndexPage.attributes={IndexPage_index_bottom, IndexPage_modal_dialog, IndexPage_modal, IndexPage_modal_footer, IndexPage_index_form, IndexPage_index_links, IndexPage_modal_header, IndexPage_index_logo, IndexPage_index_header, IndexPage_index_query, IndexPage_index_copyright, IndexPage_modal_body, IndexPage_index_nav, IndexPage_index_footer, IndexPage_index_search}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={IndexPage},
    associations={},
    generalizations={}
)
