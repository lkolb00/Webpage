from django.contrib import admin
from .models import Student, Event, Club, Meal
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)
class StudentInLine(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]
    actions = [
        'activate_users',
    ]

    def activate_users(self, request, queryset):
        assert request.user.has_perm('auth.change_user')
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))
    activate_users.short_description = 'Activate Users'  # type: ignore

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('auth.change_user'):
            del actions['activate_users']
        return actions

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }
        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
    def has_delete_permission(self, request, obj=None):
        return False




#Define the admin options for the Customer table
class StudentList(admin.ModelAdmin):
    list_display = ( 'student_name', 'phone' )
    list_filter = ( 'student_name',)
    search_fields = ('student_name', )
    ordering = ['student_name']

#Define the admin options for the Service table
class EventList(admin.ModelAdmin):
    list_display = ( 'event_name', 'event_category', 'event_date')
    list_filter = ( 'event_name', 'event_date')
    search_fields = ('event_description','event_name', )
    ordering = ['event_name']

#Define the admin options for the Product table
class ClubList(admin.ModelAdmin):
    list_display = ( 'club_name', 'club_category')
    list_filter = ('club_name', 'club_category')
    search_fields = ('club_name', 'club_category')
    ordering = ['club_name']

class MealList(admin.ModelAdmin):
    list_display = ('meal_name', 'meal_description')
    list_filter = ('meal_name', 'meal_drink')
    search_fields = ('meal_name', 'meal_drink')
    ordering = ['meal_name']

admin.site.register(Student, StudentList)
admin.site.register(Event, EventList)
admin.site.register(Club, ClubList)
admin.site.register(Meal, MealList)
