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
WebPage = Class(name="WebPage")
FeaturedCourses = Class(name="FeaturedCourses")
Instructors = Class(name="Instructors")
StudentTestimonials = Class(name="StudentTestimonials")
Footer = Class(name="Footer")

# WebPage class attributes and methods
WebPage_logo: Property = Property(name="logo", type=StringType)
WebPage_searchInput: Property = Property(name="searchInput", type=StringType)
WebPage.attributes={WebPage_searchInput, WebPage_logo}

# FeaturedCourses class attributes and methods
FeaturedCourses_courseTitle: Property = Property(name="courseTitle", type=StringType)
FeaturedCourses_courseDescription: Property = Property(name="courseDescription", type=StringType)
FeaturedCourses_courseDuration: Property = Property(name="courseDuration", type=TimeDeltaType)
FeaturedCourses.attributes={FeaturedCourses_courseTitle, FeaturedCourses_courseDescription, FeaturedCourses_courseDuration}

# Instructors class attributes and methods
Instructors_instructorName: Property = Property(name="instructorName", type=StringType)
Instructors_instructorBio: Property = Property(name="instructorBio", type=StringType)
Instructors.attributes={Instructors_instructorBio, Instructors_instructorName}

# StudentTestimonials class attributes and methods
StudentTestimonials_studentName: Property = Property(name="studentName", type=StringType)
StudentTestimonials_testimonialText: Property = Property(name="testimonialText", type=StringType)
StudentTestimonials.attributes={StudentTestimonials_studentName, StudentTestimonials_testimonialText}

# Footer class attributes and methods
Footer_copyright: Property = Property(name="copyright", type=StringType)
Footer_blogLink: Property = Property(name="blogLink", type=StringType)
Footer_contactLink: Property = Property(name="contactLink", type=StringType)
Footer_faqLink: Property = Property(name="faqLink", type=StringType)
Footer.attributes={Footer_blogLink, Footer_faqLink, Footer_contactLink, Footer_copyright}

# Relationships
fc1: BinaryAssociation = BinaryAssociation(
    name="fc1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="FeaturedCourses", type=FeaturedCourses, multiplicity=Multiplicity(1, 1))
    }
)
ins1: BinaryAssociation = BinaryAssociation(
    name="ins1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Instructors", type=Instructors, multiplicity=Multiplicity(1, 1))
    }
)
st1: BinaryAssociation = BinaryAssociation(
    name="st1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="StudentTestimonials", type=StudentTestimonials, multiplicity=Multiplicity(1, 1))
    }
)
ftr1: BinaryAssociation = BinaryAssociation(
    name="ftr1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, FeaturedCourses, Instructors, StudentTestimonials, Footer},
    associations={fc1, ins1, st1, ftr1},
    generalizations={}
)
