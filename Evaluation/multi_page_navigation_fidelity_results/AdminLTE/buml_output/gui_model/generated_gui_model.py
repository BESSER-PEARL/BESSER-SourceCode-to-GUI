exec(open(r"D:\VSCodeBESSER\HTML-to-BUML-Convertor\multi_pages_evalaution\eval_results\AdminLTE\buml_output\buml\model.py").read())
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui.graphical_ui import *
from besser.BUML.metamodel.gui.style import *

# ── Shared style tokens ───────────────────────────────────────────────────────
ScreenLayout = Layout(orientation="vertical", padding="0", margin="0", gap="24px",
                      alignment=JustificationType.LEFT, wrap=True)
SidebarLayout = Layout(orientation="vertical", padding="0", margin="0", gap="8px",
                       alignment=JustificationType.LEFT, wrap=True)
ContentLayout = Layout(orientation="vertical", padding="24px", margin="0", gap="16px",
                       alignment=JustificationType.LEFT, wrap=True)

SidebarColor = Color(background_color="#343A40", text_color="#C2C7D0", border_color="")
SidebarPosition = Position(top="0", left="0", right="", bottom="0", alignment="", z_index=50)
SidebarSize = Size(width="250px", height="100%", padding="0", margin="0",
                   font_size="14px", icon_size="", unit_size=UnitSize.PIXELS)
SidebarStyling = Styling(size=SidebarSize, position=SidebarPosition, color=SidebarColor)

NavBtnColor = Color(background_color="", text_color="#C2C7D0", border_color="")
NavBtnPosition = Position(top="", left="", right="", bottom="", alignment="", z_index=0)
NavBtnSize = Size(width="100%", height="40px", padding="8px 16px", margin="0",
                  font_size="14px", icon_size="", unit_size=UnitSize.PERCENTAGE)
NavBtnStyling = Styling(size=NavBtnSize, position=NavBtnPosition, color=NavBtnColor)

ContentColor = Color(background_color="#F4F6F9", text_color="#1F2937", border_color="")
ContentPosition = Position(top="", left="", right="", bottom="", alignment="", z_index=0)
ContentSize = Size(width="100%", height="auto", padding="20px", margin="0",
                   font_size="14px", icon_size="", unit_size=UnitSize.PERCENTAGE)
ContentStyling = Styling(size=ContentSize, position=ContentPosition, color=ContentColor)

TitleColor = Color(background_color="", text_color="#1F2937", border_color="")
TitlePosition = Position(top="", left="", right="", bottom="", alignment="", z_index=0)
TitleSize = Size(width="auto", height="auto", padding="0", margin="0 0 20px 0",
                 font_size="24px", icon_size="", unit_size=UnitSize.PIXELS)
TitleStyling = Styling(size=TitleSize, position=TitlePosition, color=TitleColor)

CardColor = Color(background_color="#FFFFFF", text_color="#1F2937", border_color="#DEE2E6")
CardPosition = Position(top="", left="", right="", bottom="", alignment="", z_index=0)
CardSize = Size(width="100%", height="auto", padding="16px", margin="0 0 16px 0",
                font_size="14px", icon_size="", unit_size=UnitSize.PERCENTAGE)
CardStyling = Styling(size=CardSize, position=CardPosition, color=CardColor)

PrimaryBtnColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="")
PrimaryBtnSize = Size(width="auto", height="38px", padding="6px 16px", margin="0",
                      font_size="14px", icon_size="", unit_size=UnitSize.AUTO)
PrimaryBtnPosition = Position(top="", left="", right="", bottom="", alignment="", z_index=0)
PrimaryBtnStyling = Styling(size=PrimaryBtnSize, position=PrimaryBtnPosition, color=PrimaryBtnColor)

InputColor = Color(background_color="#FFFFFF", text_color="#495057", border_color="#CED4DA")
InputPosition = Position(top="", left="", right="", bottom="", alignment="", z_index=0)
InputSize = Size(width="100%", height="38px", padding="6px 12px", margin="0 0 12px 0",
                 font_size="14px", icon_size="", unit_size=UnitSize.PERCENTAGE)
InputStyling = Styling(size=InputSize, position=InputPosition, color=InputColor)

# ── 1. DASHBOARD (index.html)  ────────────────────────────────────────────────
dashSidebar = ViewContainer(name="DashboardSidebar", description="Sidebar navigation",
                            layout=SidebarLayout, styling=SidebarStyling, view_elements="")

navToDash2  = Button(name="NavToDashV2",    label="Dashboard v2",   description="Sidebar: Dashboard v2",
                     buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                     targetScreen=None, styling=NavBtnStyling)
navToDash3  = Button(name="NavToDashV3",    label="Dashboard v3",   description="Sidebar: Dashboard v3",
                     buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                     targetScreen=None, styling=NavBtnStyling)
navToStart  = Button(name="NavToStarter",   label="Starter",        description="Sidebar: Starter",
                     buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                     targetScreen=None, styling=NavBtnStyling)
navToUsers  = Button(name="NavToUsers",     label="Users",          description="Sidebar: Users",
                     buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                     targetScreen=None, styling=NavBtnStyling)

dashContent = ViewContainer(name="DashboardContent", description="Main content area",
                            layout=ContentLayout, styling=ContentStyling, view_elements="")
dashTitle   = ViewComponent(name="DashboardTitle", description="Dashboard page title", styling=TitleStyling)

dashDs = DataSourceElement(name="DashboardDataSource", dataSourceClass=Dashboard,
                           fields={Dashboard_newOrders, Dashboard_bounceRatePercent,
                                   Dashboard_userRegistrations, Dashboard_uniqueVisitors,
                                   Dashboard_directChatNewMessages})
dashList = DataList(name="DashboardStatsList", description="Dashboard stats", list_sources={dashDs},
                    styling=CardStyling)

DashboardScreen = Screen(name="DashboardScreen", description="AdminLTE main dashboard (index.html)",
                         x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium",
                         view_elements={dashSidebar, navToDash2, navToDash3, navToStart, navToUsers,
                                        dashContent, dashTitle, dashList},
                         is_main_page=True, layout=ScreenLayout)

# ── 2. DASHBOARD V2 (index2.html)  ───────────────────────────────────────────
dash2Sidebar = ViewContainer(name="DashV2Sidebar", description="Sidebar navigation",
                             layout=SidebarLayout, styling=SidebarStyling, view_elements="")

nav2ToDash   = Button(name="Nav2ToDash",    label="Dashboard",    description="Sidebar: Dashboard",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
nav2ToDash3  = Button(name="Nav2ToDashV3",  label="Dashboard v3", description="Sidebar: Dashboard v3",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
nav2ToStart  = Button(name="Nav2ToStarter", label="Starter",      description="Sidebar: Starter",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
nav2ToUsers  = Button(name="Nav2ToUsers",   label="Users",        description="Sidebar: Users",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)

dash2Content = ViewContainer(name="DashV2Content", description="Main content area",
                             layout=ContentLayout, styling=ContentStyling, view_elements="")
dash2Title   = ViewComponent(name="DashV2Title", description="Dashboard v2 title", styling=TitleStyling)

dash2Ds = DataSourceElement(name="DashV2DataSource", dataSourceClass=DashboardV2,
                            fields={DashboardV2_cpuTrafficPercent, DashboardV2_likes,
                                    DashboardV2_sales, DashboardV2_newMembers,
                                    DashboardV2_totalRevenue, DashboardV2_totalProfit})
dash2List = DataList(name="DashV2StatsList", description="Dashboard v2 stats",
                     list_sources={dash2Ds}, styling=CardStyling)

DashboardV2Screen = Screen(name="DashboardV2Screen", description="AdminLTE dashboard v2 (index2.html)",
                           x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium",
                           view_elements={dash2Sidebar, nav2ToDash, nav2ToDash3, nav2ToStart, nav2ToUsers,
                                          dash2Content, dash2Title, dash2List},
                           is_main_page=False, layout=ScreenLayout)

# ── 3. DASHBOARD V3 (index3.html)  ───────────────────────────────────────────
dash3Sidebar = ViewContainer(name="DashV3Sidebar", description="Sidebar navigation",
                             layout=SidebarLayout, styling=SidebarStyling, view_elements="")

nav3ToDash   = Button(name="Nav3ToDash",    label="Dashboard",    description="Sidebar: Dashboard",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
nav3ToDash2  = Button(name="Nav3ToDashV2",  label="Dashboard v2", description="Sidebar: Dashboard v2",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
nav3ToStart  = Button(name="Nav3ToStarter", label="Starter",      description="Sidebar: Starter",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
nav3ToUsers  = Button(name="Nav3ToUsers",   label="Users",        description="Sidebar: Users",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)

dash3Content = ViewContainer(name="DashV3Content", description="Main content area",
                             layout=ContentLayout, styling=ContentStyling, view_elements="")
dash3Title   = ViewComponent(name="DashV3Title", description="Dashboard v3 title", styling=TitleStyling)

dash3Ds = DataSourceElement(name="DashV3DataSource", dataSourceClass=DashboardV3,
                            fields={DashboardV3_visitorsTotal, DashboardV3_visitorsChangePercent,
                                    DashboardV3_salesTotal, DashboardV3_conversionRatePercent})
dash3List = DataList(name="DashV3StatsList", description="Dashboard v3 stats",
                     list_sources={dash3Ds}, styling=CardStyling)

DashboardV3Screen = Screen(name="DashboardV3Screen", description="AdminLTE dashboard v3 (index3.html)",
                           x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium",
                           view_elements={dash3Sidebar, nav3ToDash, nav3ToDash2, nav3ToStart, nav3ToUsers,
                                          dash3Content, dash3Title, dash3List},
                           is_main_page=False, layout=ScreenLayout)

# ── 4. STARTER (starter.html)  ───────────────────────────────────────────────
startSidebar = ViewContainer(name="StarterSidebar", description="Sidebar navigation",
                             layout=SidebarLayout, styling=SidebarStyling, view_elements="")

navSToDash   = Button(name="NavSToDash",    label="Dashboard",    description="Sidebar: Dashboard",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
navSToDash2  = Button(name="NavSToDashV2",  label="Dashboard v2", description="Sidebar: Dashboard v2",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
navSToDash3  = Button(name="NavSToDashV3",  label="Dashboard v3", description="Sidebar: Dashboard v3",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
navSToUsers  = Button(name="NavSToUsers",   label="Users",        description="Sidebar: Users",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)

startContent = ViewContainer(name="StarterContent", description="Starter page content",
                             layout=ContentLayout, styling=ContentStyling, view_elements="")
startTitle   = ViewComponent(name="StarterTitle", description="Starter page title", styling=TitleStyling)

startDs = DataSourceElement(name="StarterDataSource", dataSourceClass=StarterPage,
                            fields={StarterPage_starterCardTitle, StarterPage_starterCardBodyText})
startList = DataList(name="StarterContentList", description="Starter content",
                     list_sources={startDs}, styling=CardStyling)

StarterScreen = Screen(name="StarterScreen", description="AdminLTE starter page (starter.html)",
                       x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium",
                       view_elements={startSidebar, navSToDash, navSToDash2, navSToDash3, navSToUsers,
                                      startContent, startTitle, startList},
                       is_main_page=False, layout=ScreenLayout)

# ── 5. USERS (users.html)  ───────────────────────────────────────────────────
usersSidebar = ViewContainer(name="UsersSidebar", description="Sidebar navigation",
                             layout=SidebarLayout, styling=SidebarStyling, view_elements="")

navUToDash   = Button(name="NavUToDash",    label="Dashboard",    description="Sidebar: Dashboard",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
navUToDash2  = Button(name="NavUToDashV2",  label="Dashboard v2", description="Sidebar: Dashboard v2",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
navUToDash3  = Button(name="NavUToDashV3",  label="Dashboard v3", description="Sidebar: Dashboard v3",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)
navUToStart  = Button(name="NavUToStarter", label="Starter",      description="Sidebar: Starter",
                      buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate,
                      targetScreen=None, styling=NavBtnStyling)

usersContent = ViewContainer(name="UsersContent", description="Users table area",
                             layout=ContentLayout, styling=ContentStyling, view_elements="")
usersTitle   = ViewComponent(name="UsersTitle", description="Users page title", styling=TitleStyling)

searchInput  = InputField(name="UserSearchInput", description="Search users by name or email",
                          field_type=InputFieldType.Text, validationRules="", styling=InputStyling)
addUserBtn   = Button(name="AddUserButton", label="Add User", description="Open add user modal",
                      buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.OpenForm,
                      targetScreen=None, styling=PrimaryBtnStyling)
addUserForm  = Form(name="AddUserForm", description="Add new user form",
                    inputFields={searchInput}, styling=None)

usersDs = DataSourceElement(name="UsersDataSource", dataSourceClass=Users,
                            fields={Users_usersShowingFrom, Users_usersShowingTo, Users_usersTotal})
usersList = DataList(name="UsersDataList", description="Users table",
                     list_sources={usersDs}, styling=CardStyling)

UsersScreen = Screen(name="UsersScreen", description="AdminLTE users management page (users.html)",
                     x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium",
                     view_elements={usersSidebar, navUToDash, navUToDash2, navUToDash3, navUToStart,
                                    usersContent, usersTitle, addUserBtn, addUserForm, usersList},
                     is_main_page=False, layout=ScreenLayout)

# ── Resolve all targetScreen bindings ────────────────────────────────────────
navToDash2.targetScreen  = DashboardV2Screen
navToDash3.targetScreen  = DashboardV3Screen
navToStart.targetScreen  = StarterScreen
navToUsers.targetScreen  = UsersScreen

nav2ToDash.targetScreen  = DashboardScreen
nav2ToDash3.targetScreen = DashboardV3Screen
nav2ToStart.targetScreen = StarterScreen
nav2ToUsers.targetScreen = UsersScreen

nav3ToDash.targetScreen  = DashboardScreen
nav3ToDash2.targetScreen = DashboardV2Screen
nav3ToStart.targetScreen = StarterScreen
nav3ToUsers.targetScreen = UsersScreen

navSToDash.targetScreen  = DashboardScreen
navSToDash2.targetScreen = DashboardV2Screen
navSToDash3.targetScreen = DashboardV3Screen
navSToUsers.targetScreen = UsersScreen

navUToDash.targetScreen  = DashboardScreen
navUToDash2.targetScreen = DashboardV2Screen
navUToDash3.targetScreen = DashboardV3Screen
navUToStart.targetScreen = StarterScreen

# ── GUIModel ──────────────────────────────────────────────────────────────────
adminlte_module = Module(name="AdminLTEModule",
                         screens={DashboardScreen, DashboardV2Screen, DashboardV3Screen,
                                  StarterScreen, UsersScreen})

gui_model = GUIModel(name="AdminLTEGUIModel", package="com.adminlte",
                     versionCode="1", versionName="1.0",
                     modules={adminlte_module},
                     description="AdminLTE 5-page admin dashboard")
