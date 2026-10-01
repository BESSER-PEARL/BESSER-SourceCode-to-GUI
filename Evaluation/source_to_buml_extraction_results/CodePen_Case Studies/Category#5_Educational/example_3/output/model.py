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
OpenAITextToSpeechGeneration = Class(name="OpenAITextToSpeechGeneration")
AudioPlayer = Class(name="AudioPlayer")

# OpenAITextToSpeechGeneration class attributes and methods
OpenAITextToSpeechGeneration_openKey: Property = Property(name="openKey", type=StringType)
OpenAITextToSpeechGeneration_inputText: Property = Property(name="inputText", type=StringType)
OpenAITextToSpeechGeneration_charCount: Property = Property(name="charCount", type=IntegerType)
OpenAITextToSpeechGeneration_cost: Property = Property(name="cost", type=FloatType)
OpenAITextToSpeechGeneration_outputFileName: Property = Property(name="outputFileName", type=StringType)
OpenAITextToSpeechGeneration_selectVoice: Property = Property(name="selectVoice", type=StringType)
OpenAITextToSpeechGeneration.attributes={OpenAITextToSpeechGeneration_cost, OpenAITextToSpeechGeneration_inputText, OpenAITextToSpeechGeneration_selectVoice, OpenAITextToSpeechGeneration_charCount, OpenAITextToSpeechGeneration_openKey, OpenAITextToSpeechGeneration_outputFileName}

# AudioPlayer class attributes and methods
AudioPlayer_isPlaying: Property = Property(name="isPlaying", type=BooleanType)
AudioPlayer_currentTime: Property = Property(name="currentTime", type=TimeType)
AudioPlayer.attributes={AudioPlayer_isPlaying, AudioPlayer_currentTime}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="OpenAITextToSpeechGeneration", type=OpenAITextToSpeechGeneration, multiplicity=Multiplicity(1, 1)),
        Property(name="AudioPlayer", type=AudioPlayer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={OpenAITextToSpeechGeneration, AudioPlayer},
    associations={association1},
    generalizations={}
)
