class UsersRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'users' or obj2._meta.app_label == 'users':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'users':
            return db == 'users_db'
        return None


class CourseCatalogRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'course_catalog':
            return 'course_catalog_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'course_catalog':
            return 'course_catalog_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'course_catalog' or obj2._meta.app_label == 'course_catalog':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'course_catalog':
            return db == 'course_catalog_db'
        return None

class PaymentsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Payments':
            return 'Payments_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Payments':
            return 'Payments_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'Payments' or obj2._meta.app_label == 'Payments':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Payments':
            return db == 'Payments_db'
        return None
class RegistrationRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Payments':
            return 'Payments_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Payments':
            return 'Payments_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'Payments' or obj2._meta.app_label == 'Payments':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Payments':
            return db == 'Payments_db'
        return None
class AppRouter:
    app_label_to_db = {
        'course_catalog': 'course_catalog_db',
        'payments': 'payments_db',
        'registration': 'registration_db',
        'users': 'users_db',
    }

    def db_for_read(self, model, **hints):
        return self.app_label_to_db.get(model._meta.app_label, 'default')

    def db_for_write(self, model, **hints):
        return self.app_label_to_db.get(model._meta.app_label, 'default')

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.app_label_to_db:
            # Only allow migrations for the app in its designated database
            return db == self.app_label_to_db[app_label]
        # Use 'default' for other Django system apps (e.g., auth, sessions)
        return db == 'default'
