class PrimaryRouter:
    def db_for_read(self, model, **hints):
        return 'primary_db'

    def db_for_write(self, model, **hints):
        return 'primary_db'

    def allow_relation(self, obj1, obj2, **hints):
      return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True