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
AddNewPostPage = Class(name="AddNewPostPage")
TablesPage = Class(name="TablesPage")
UserProfilePage = Class(name="UserProfilePage")
ErrorsPage = Class(name="ErrorsPage")
DashboardPage = Class(name="DashboardPage")

# AddNewPostPage class attributes and methods
AddNewPostPage_post_title: Property = Property(name="post_title", type=StringType)
AddNewPostPage_post_content: Property = Property(name="post_content", type=StringType)
AddNewPostPage_status: Property = Property(name="status", type=StringType)
AddNewPostPage_visibility: Property = Property(name="visibility", type=StringType)
AddNewPostPage_readability: Property = Property(name="readability", type=StringType)
AddNewPostPage_category_uncategorized: Property = Property(name="category_uncategorized", type=BooleanType)
AddNewPostPage_category_design: Property = Property(name="category_design", type=BooleanType)
AddNewPostPage_category_development: Property = Property(name="category_development", type=BooleanType)
AddNewPostPage_category_writing: Property = Property(name="category_writing", type=BooleanType)
AddNewPostPage_new_category_name: Property = Property(name="new_category_name", type=StringType)
AddNewPostPage.attributes={AddNewPostPage_status, AddNewPostPage_category_writing, AddNewPostPage_new_category_name, AddNewPostPage_post_content, AddNewPostPage_visibility, AddNewPostPage_post_title, AddNewPostPage_category_development, AddNewPostPage_readability, AddNewPostPage_category_uncategorized, AddNewPostPage_category_design}

# TablesPage class attributes and methods
TablesPage_active_users_table: Property = Property(name="active_users_table", type=StringType)
TablesPage_inactive_users_table: Property = Property(name="inactive_users_table", type=StringType)
TablesPage.attributes={TablesPage_inactive_users_table, TablesPage_active_users_table}

# UserProfilePage class attributes and methods
UserProfilePage_profile_name: Property = Property(name="profile_name", type=StringType)
UserProfilePage_profile_role: Property = Property(name="profile_role", type=StringType)
UserProfilePage_workload_percent: Property = Property(name="workload_percent", type=IntegerType)
UserProfilePage_first_name: Property = Property(name="first_name", type=StringType)
UserProfilePage_last_name: Property = Property(name="last_name", type=StringType)
UserProfilePage_email: Property = Property(name="email", type=StringType)
UserProfilePage_password: Property = Property(name="password", type=StringType)
UserProfilePage_address: Property = Property(name="address", type=StringType)
UserProfilePage_city: Property = Property(name="city", type=StringType)
UserProfilePage_state: Property = Property(name="state", type=StringType)
UserProfilePage_zip: Property = Property(name="zip", type=StringType)
UserProfilePage_account_description: Property = Property(name="account_description", type=StringType)
UserProfilePage.attributes={UserProfilePage_profile_role, UserProfilePage_state, UserProfilePage_workload_percent, UserProfilePage_password, UserProfilePage_zip, UserProfilePage_account_description, UserProfilePage_first_name, UserProfilePage_address, UserProfilePage_last_name, UserProfilePage_city, UserProfilePage_profile_name, UserProfilePage_email}

# ErrorsPage class attributes and methods
ErrorsPage_error_code: Property = Property(name="error_code", type=IntegerType)
ErrorsPage_error_title: Property = Property(name="error_title", type=StringType)
ErrorsPage_error_message: Property = Property(name="error_message", type=StringType)
ErrorsPage.attributes={ErrorsPage_error_title, ErrorsPage_error_code, ErrorsPage_error_message}

# DashboardPage class attributes and methods
DashboardPage_posts_count: Property = Property(name="posts_count", type=IntegerType)
DashboardPage_posts_change_percent: Property = Property(name="posts_change_percent", type=FloatType)
DashboardPage_pages_count: Property = Property(name="pages_count", type=IntegerType)
DashboardPage_pages_change_percent: Property = Property(name="pages_change_percent", type=FloatType)
DashboardPage_comments_count: Property = Property(name="comments_count", type=IntegerType)
DashboardPage_comments_change_percent: Property = Property(name="comments_change_percent", type=FloatType)
DashboardPage_users_count: Property = Property(name="users_count", type=IntegerType)
DashboardPage_users_change_percent: Property = Property(name="users_change_percent", type=FloatType)
DashboardPage_subscribers_count: Property = Property(name="subscribers_count", type=IntegerType)
DashboardPage_subscribers_change_percent: Property = Property(name="subscribers_change_percent", type=FloatType)
DashboardPage_new_draft_title: Property = Property(name="new_draft_title", type=StringType)
DashboardPage_new_draft_body: Property = Property(name="new_draft_body", type=StringType)
DashboardPage.attributes={DashboardPage_posts_count, DashboardPage_new_draft_body, DashboardPage_users_count, DashboardPage_users_change_percent, DashboardPage_pages_change_percent, DashboardPage_posts_change_percent, DashboardPage_subscribers_count, DashboardPage_subscribers_change_percent, DashboardPage_comments_change_percent, DashboardPage_comments_count, DashboardPage_pages_count, DashboardPage_new_draft_title}

# Relationships
DashboardPage_AddNewPostPage: BinaryAssociation = BinaryAssociation(
    name="DashboardPage_AddNewPostPage",
    ends={
        Property(name="DashboardPage", type=DashboardPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="AddNewPostPage", type=AddNewPostPage, multiplicity=Multiplicity(1, 1))
    }
)
DashboardPage_TablesPage: BinaryAssociation = BinaryAssociation(
    name="DashboardPage_TablesPage",
    ends={
        Property(name="DashboardPage", type=DashboardPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="TablesPage", type=TablesPage, multiplicity=Multiplicity(1, 1))
    }
)
DashboardPage_UserProfilePage: BinaryAssociation = BinaryAssociation(
    name="DashboardPage_UserProfilePage",
    ends={
        Property(name="DashboardPage", type=DashboardPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="UserProfilePage", type=UserProfilePage, multiplicity=Multiplicity(1, 1))
    }
)
DashboardPage_ErrorsPage: BinaryAssociation = BinaryAssociation(
    name="DashboardPage_ErrorsPage",
    ends={
        Property(name="DashboardPage", type=DashboardPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="ErrorsPage", type=ErrorsPage, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={AddNewPostPage, TablesPage, UserProfilePage, ErrorsPage, DashboardPage},
    associations={DashboardPage_AddNewPostPage, DashboardPage_TablesPage, DashboardPage_UserProfilePage, DashboardPage_ErrorsPage},
    generalizations={},
    metadata=None
)
