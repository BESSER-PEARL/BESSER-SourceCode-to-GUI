from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from gui_metamodel import Screen, InputField, DataList, Layout, LayoutType, JustificationType, Collection, CollectionSourceType, InputFieldType, DataSourceElement, Class, Property, Styling, Size, Color, Position, PositionType, UnitSize
from besser.BUML.metamodel.structural import StringType, BooleanType

User = Class(name="User")
User_name = Property(name="name", type=StringType)
User_email = Property(name="email", type=StringType)
User.attributes = {User_name, User_email}
Address = Class(name="Address")
Address_city = Property(name="city", type=StringType)
Address.attributes = {Address_city}
MainPage = Class(name="MainPage")
MainPage_search = Property(name="search", type=StringType)
MainPage_loading = Property(name="loading", type=BooleanType)
MainPage_title = Property(name="title", type=StringType)
MainPage.attributes = {MainPage_search, MainPage_loading, MainPage_title}
layout = Layout(orientation="vertical", padding="20px", margin="20px", gap="10px", alignment=JustificationType.Center, wrap=True)
main_screen = Screen(name="MainScreen", view_elements=set(), x_dpi="160", y_dpi="160", screen_size="Large", is_main_page=True, layout=layout, description="")
search_input = InputField(name="SearchInput", description="Search by name or email", type=InputFieldType.Search, validationRules="", styling=Styling(size=Size(width="100%", height="40px", padding="10px", margin="0", font_size="1em", unit_size=UnitSize.PIXELS), color=Color(background_color="#fff", text_color="#333", border_color="#ddd"), position=Position(type=PositionType.Relative, alignment="center")))
user_data_list = DataList(name="UserList", list_sources={DataSourceElement(name="UserDataSource", dataSourceClass=User, fields=User.attributes)}, styling=Styling(size=Size(width="100%", height="auto", padding="10px", margin="0", unit_size=UnitSize.PIXELS), color=Color(background_color="#fff", text_color="#333", border_color="#eee"), position=Position(type=PositionType.Relative, alignment="center")), description="")
main_screen.view_elements.add(search_input)
main_screen.view_elements.add(user_data_list)
userList = Collection(name="userList", type=CollectionSourceType.List)
userAddress = Collection(name="userAddress", type=CollectionSourceType.List)
domain_model = DomainModel(name="DomainModel", types={MainPage, User, Address}, associations={userList, userAddress}, generalizations={})
