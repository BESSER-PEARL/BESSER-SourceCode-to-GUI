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
QuizPage = Class(name="QuizPage")
QuizContainer = Class(name="QuizContainer")
Modal = Class(name="Modal")

# QuizPage class attributes and methods

# QuizContainer class attributes and methods
QuizContainer_question: Property = Property(name="question", type=StringType)
QuizContainer_answer: Property = Property(name="answer", type=StringType)
QuizContainer_result: Property = Property(name="result", type=StringType)
QuizContainer.attributes={QuizContainer_answer, QuizContainer_question, QuizContainer_result}

# Modal class attributes and methods
Modal_explanation: Property = Property(name="explanation", type=StringType)
Modal.attributes={Modal_explanation}

# Relationships
contains_quiz: BinaryAssociation = BinaryAssociation(
    name="contains_quiz",
    ends={
        Property(name="QuizPage", type=QuizPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="QuizContainer", type=QuizContainer, multiplicity=Multiplicity(1, 1))
    }
)
contains_modal: BinaryAssociation = BinaryAssociation(
    name="contains_modal",
    ends={
        Property(name="QuizPage", type=QuizPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Modal", type=Modal, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={QuizPage, QuizContainer, Modal},
    associations={contains_quiz, contains_modal},
    generalizations={}
)
