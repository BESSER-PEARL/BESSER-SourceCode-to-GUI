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
Wrapper = Class(name="Wrapper")
Logo = Class(name="Logo")
HeroImage = Class(name="HeroImage")
SupHeader = Class(name="SupHeader")
Header = Class(name="Header")
Paragraph = Class(name="Paragraph")
Button = Class(name="Button")
Line = Class(name="Line")
Footer = Class(name="Footer")

# EmailTemplate class attributes and methods
EmailTemplate_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
EmailTemplate_textColor: Property = Property(name="textColor", type=StringType)
EmailTemplate_width: Property = Property(name="width", type=IntegerType)
EmailTemplate_height: Property = Property(name="height", type=IntegerType)
EmailTemplate.attributes={EmailTemplate_textColor, EmailTemplate_width, EmailTemplate_height, EmailTemplate_backgroundColor}

# Wrapper class attributes and methods
Wrapper_width: Property = Property(name="width", type=IntegerType)
Wrapper_maxWidth: Property = Property(name="maxWidth", type=IntegerType)
Wrapper.attributes={Wrapper_width, Wrapper_maxWidth}

# Logo class attributes and methods
Logo_altText: Property = Property(name="altText", type=StringType)
Logo_title: Property = Property(name="title", type=StringType)
Logo_url: Property = Property(name="url", type=StringType)
Logo_imageSrc: Property = Property(name="imageSrc", type=StringType)
Logo.attributes={Logo_title, Logo_url, Logo_imageSrc, Logo_altText}

# HeroImage class attributes and methods
HeroImage_url: Property = Property(name="url", type=StringType)
HeroImage_imageSrc: Property = Property(name="imageSrc", type=StringType)
HeroImage_altText: Property = Property(name="altText", type=StringType)
HeroImage_title: Property = Property(name="title", type=StringType)
HeroImage_width: Property = Property(name="width", type=IntegerType)
HeroImage.attributes={HeroImage_url, HeroImage_width, HeroImage_imageSrc, HeroImage_altText, HeroImage_title}

# SupHeader class attributes and methods
SupHeader_text: Property = Property(name="text", type=StringType)
SupHeader_textColor: Property = Property(name="textColor", type=StringType)
SupHeader_fontFamily: Property = Property(name="fontFamily", type=StringType)
SupHeader.attributes={SupHeader_fontFamily, SupHeader_text, SupHeader_textColor}

# Header class attributes and methods
Header_text: Property = Property(name="text", type=StringType)
Header_textColor: Property = Property(name="textColor", type=StringType)
Header_fontFamily: Property = Property(name="fontFamily", type=StringType)
Header.attributes={Header_textColor, Header_text, Header_fontFamily}

# Paragraph class attributes and methods
Paragraph_text: Property = Property(name="text", type=StringType)
Paragraph_textColor: Property = Property(name="textColor", type=StringType)
Paragraph_fontFamily: Property = Property(name="fontFamily", type=StringType)
Paragraph.attributes={Paragraph_text, Paragraph_textColor, Paragraph_fontFamily}

# Button class attributes and methods
Button_url: Property = Property(name="url", type=StringType)
Button_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
Button_textColor: Property = Property(name="textColor", type=StringType)
Button_fontFamily: Property = Property(name="fontFamily", type=StringType)
Button.attributes={Button_url, Button_backgroundColor, Button_fontFamily, Button_textColor}

# Line class attributes and methods
Line_color: Property = Property(name="color", type=StringType)
Line.attributes={Line_color}

# Footer class attributes and methods
Footer_text: Property = Property(name="text", type=StringType)
Footer_textColor: Property = Property(name="textColor", type=StringType)
Footer_fontFamily: Property = Property(name="fontFamily", type=StringType)
Footer.attributes={Footer_text, Footer_textColor, Footer_fontFamily}

# Relationships
containsParagraph: BinaryAssociation = BinaryAssociation(
    name="containsParagraph",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="Paragraph", type=Paragraph, multiplicity=Multiplicity(1, 1))
    }
)
containsButton: BinaryAssociation = BinaryAssociation(
    name="containsButton",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="Button", type=Button, multiplicity=Multiplicity(1, 1))
    }
)
containsWrapper: BinaryAssociation = BinaryAssociation(
    name="containsWrapper",
    ends={
        Property(name="EmailTemplate", type=EmailTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1))
    }
)
containsLogo: BinaryAssociation = BinaryAssociation(
    name="containsLogo",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo", type=Logo, multiplicity=Multiplicity(1, 1))
    }
)
containsHeroImage: BinaryAssociation = BinaryAssociation(
    name="containsHeroImage",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="HeroImage", type=HeroImage, multiplicity=Multiplicity(1, 1))
    }
)
containsSupHeader: BinaryAssociation = BinaryAssociation(
    name="containsSupHeader",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="SupHeader", type=SupHeader, multiplicity=Multiplicity(1, 1))
    }
)
containsHeader: BinaryAssociation = BinaryAssociation(
    name="containsHeader",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
containsLine: BinaryAssociation = BinaryAssociation(
    name="containsLine",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="Line", type=Line, multiplicity=Multiplicity(1, 1))
    }
)
containsFooter: BinaryAssociation = BinaryAssociation(
    name="containsFooter",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={EmailTemplate, Wrapper, Logo, HeroImage, SupHeader, Header, Paragraph, Button, Line, Footer},
    associations={containsParagraph, containsButton, containsWrapper, containsLogo, containsHeroImage, containsSupHeader, containsHeader, containsLine, containsFooter},
    generalizations={}
)
