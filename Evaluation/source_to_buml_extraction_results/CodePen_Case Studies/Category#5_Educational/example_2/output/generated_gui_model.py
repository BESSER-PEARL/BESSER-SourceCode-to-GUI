from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
##############################
#      GUI model definition  #
##############################

####### Styling definitions ################

# Screen layout
ScreenLayout = Layout(
    type=LayoutType.Flex,
    orientation="vertical",
    gap="15px",
    alignment=JustificationType.Center
)

# Button styling
ButtonColor = Color(
    background_color="#007BFF",
    text_color="#FFFFFF",
    border_color="#0056b3"
)
buttonPosition = Position(
    type=PositionType.Relative,
    z_index=10
)
buttonSize = Size(
    width="100%",
    height="40px",
    padding="10px",
    margin="10px",
    font_size="16px",
    unit_size=UnitSize.PIXELS
)
buttonStyling = Styling(
    size=buttonSize,
    position=buttonPosition,
    color=ButtonColor
)

# Modal styling
ModalColor = Color(
    background_color="#FFFFFF",
    text_color="#000000",
    border_color="#CCCCCC"
)
modalPosition = Position(
    type=PositionType.Fixed,
    top="50%",
    left="50%",
    alignment="center",
    z_index=100
)
modalSize = Size(
    width="80%",
    height="auto",
    padding="20px",
    font_size="16px",
    unit_size=UnitSize.PIXELS
)
modalStyling = Styling(
    size=modalSize,
    position=modalPosition,
    color=ModalColor
)

##### Elements for Quiz Page Screen #####

# ViewComponent definition
viewComponent = ViewComponent(
    name="QuizView",
    description="Interactive quiz with questions and answers"
)

# Input field for answer
answerInput = InputField(
    name="AnswerInput",
    description="Input field for the answer",
    type="Text",
    styling=Styling(
        size=Size(
            width="100%",
            padding="10px",
            font_size="16px",
            unit_size=UnitSize.PIXELS
        )
    )
)

# Button for explaining the answer
explainButton = Button(
    name="ExplainButton",
    description="Explain the answer",
    label="Explain Answer",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.None,
    styling=Styling(
        size=Size(
            width="100%",
            padding="10px",
            font_size="16px",
            unit_size=UnitSize.PIXELS
        ),
        color=Color(
            background_color="#fca311",
            text_color="#FFFFFF",
            border_color="#c28700"
        )
    )
)

# Button for submitting the answer
submitButton = Button(
    name="SubmitButton",
    description="Submit the answer",
    label="Submit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Submit,
    styling=Styling(
        size=Size(
            width="100%",
            padding="10px",
            font_size="16px",
            unit_size=UnitSize.PIXELS
        ),
        color=Color(
            background_color="#008489",
            text_color="#FFFFFF",
            border_color="#005c5f"
        )
    )
)

# Modal for explanation
explanationModal = ViewComponent(
    name="ExplanationModal",
    description="Modal for showing explanation",
    styling=modalStyling
)

# Button for next question
nextButton = Button(
    name="NextButton",
    description="Proceed to the next question",
    label="Next Question",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Next,
    styling=Styling(
        size=Size(
            width="100%",
            padding="10px",
            font_size="16px",
            unit_size=UnitSize.PIXELS
        ),
        color=Color(
            background_color="#008489",
            text_color="#FFFFFF",
            border_color="#005c5f"
        )
    )
)

# Quiz Page Screen definition
QuizPageScreen = Screen(
    name="QuizPage",
    description="Interactive quiz page with questions and answers",
    x_dpi="QuizContainer_question",
    y_dpi="QuizContainer_answer",
    screen_size="Medium",
    view_elements={answerInput, explainButton, submitButton, explanationModal, nextButton},
    is_main_page=True,
    layout=ScreenLayout
)

# Module definition
QuizModule = Module(
    name="QuizModule",
    screens={QuizPageScreen}
)

# Application definition
gui_model = GUIModel(
    name="InteractiveQuizApp",
    package="com.example.interactivequiz",
    versionCode="1",
    versionName="1.0",
    description="An interactive quiz application with explanations.",
    screenCompatibility=True,
    modules={QuizModule}
)
