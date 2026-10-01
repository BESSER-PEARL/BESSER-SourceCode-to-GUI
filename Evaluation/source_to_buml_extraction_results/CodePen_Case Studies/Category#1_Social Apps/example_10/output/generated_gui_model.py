from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from metamodel import Screen, ViewContainer, Menu, MenuItem, Layout, LayoutType, JustificationType, PositionType, Size, UnitSize, Color, Position, Styling

social_media_screen = Screen(
    name="SocialMediaScreen",
    layout=Layout(orientation="vertical", padding="10px", margin="10px", gap="5px", alignment=JustificationType.Center, wrap=True),
    view_elements={
        ViewContainer(
            name="SocialMediaContainer",
            description="Container for social media links",
            layout=Layout(orientation="horizontal", padding="4px 10px", margin="0", gap="10px", alignment=JustificationType.Center, wrap=False),
            view_elements={
                Menu(
                    name="SocialMediaMenu",
                    description="Menu for social media links",
                    menuItems={MenuItem(label="Facebook"), MenuItem(label="Twitter"), MenuItem(label="Instagram"), MenuItem(label="Google Plus")},
                    styling=Styling(size=Size(width="auto", height="auto", padding="0", margin="0", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Fixed, top="0", bottom="0", left="0", right="0", alignment="center"), color=Color(background_color="#212121", text_color="#ccc", border_color="transparent")),
                )
            },
        )
    },
    description="",
    screen_size="",
    y_dpi="",
    x_dpi="",
)
