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
EmailTemplate = Class(name="EmailTemplate")
Button = Class(name="Button")
Image = Class(name="Image")
SocialIcon = Class(name="SocialIcon")

# EmailTemplate class attributes and methods
EmailTemplate_header: Property = Property(name="header", type=StringType)
EmailTemplate_subheader: Property = Property(name="subheader", type=StringType)
EmailTemplate_paragraph: Property = Property(name="paragraph", type=StringType)
EmailTemplate_footer: Property = Property(name="footer", type=StringType)
EmailTemplate_title: Property = Property(name="title", type=StringType)
EmailTemplate_preheader: Property = Property(name="preheader", type=StringType)
EmailTemplate.attributes={EmailTemplate_paragraph, EmailTemplate_footer, EmailTemplate_header, EmailTemplate_subheader, EmailTemplate_title, EmailTemplate_preheader}

# Button class attributes and methods
Button_text: Property = Property(name="text", type=StringType)
Button_link: Property = Property(name="link", type=StringType)
Button.attributes={Button_text, Button_link}

# Image class attributes and methods
Image_src: Property = Property(name="src", type=StringType)
Image_alt: Property = Property(name="alt", type=StringType)
Image_width: Property = Property(name="width", type=IntegerType)
Image_height: Property = Property(name="height", type=IntegerType)
Image.attributes={Image_alt, Image_width, Image_height, Image_src}

# SocialIcon class attributes and methods
SocialIcon_platform: Property = Property(name="platform", type=StringType)
SocialIcon_link: Property = Property(name="link", type=StringType)
SocialIcon_iconSrc: Property = Property(name="iconSrc", type=StringType)
SocialIcon.attributes={SocialIcon_iconSrc, SocialIcon_platform, SocialIcon_link}

# Relationships
containsButton: BinaryAssociation = BinaryAssociation(
    name="containsButton",
    ends={
        Property(name="EmailTemplate", type=EmailTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="Button", type=Button, multiplicity=Multiplicity(0, 9999))
    }
)
containsImage: BinaryAssociation = BinaryAssociation(
    name="containsImage",
    ends={
        Property(name="EmailTemplate", type=EmailTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="Image", type=Image, multiplicity=Multiplicity(0, 9999))
    }
)
containsSocialIcon: BinaryAssociation = BinaryAssociation(
    name="containsSocialIcon",
    ends={
        Property(name="EmailTemplate", type=EmailTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="SocialIcon", type=SocialIcon, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={EmailTemplate, Button, Image, SocialIcon},
    associations={containsButton, containsImage, containsSocialIcon},
    generalizations={}
)
